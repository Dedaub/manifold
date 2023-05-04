#!/usr/bin/env python3


import asyncio
import multiprocessing as mp
from contextlib import nullcontext
from itertools import repeat
from multiprocessing.pool import Pool
from operator import methodcaller
from typing import Any, Literal

import eth_retry
import eth_retry.eth_retry
from aiohttp import ClientSession, ClientTimeout, TCPConnector
from pysad.utils import hex_to_bytes

from manifold.call import Call
from manifold.constants import AGGREGATE_SIGNATURE, MULTICALL_MAP
from manifold.pool import SingletonPool
from manifold.rpc import JSONRPCErrorCode
from manifold.signature import Signature

eth_retry.eth_retry.MIN_SLEEP_TIME = 5
eth_retry.eth_retry.MAX_SLEEP_TIME = 10
eth_retry.eth_retry.MAX_RETRIES = 5


class MultiCall:
    rpc_url: str
    calls: list[Call]
    batch_size: int  # size of each multicall batch
    num_procs: int  # number of processes to handle abi encoding/decoding
    signature: Signature
    address: bytes  # address of the multicall contract
    require_success: bool  # require all calls to succeed
    block_number: int | Literal["latest"]

    def __init__(
        self,
        rpc_url: str,
        calls: list[Call],
        batch_size: int = 1000,
        require_success: bool = False,
        chain_id: int = 1,
        num_conns: int = 10,  # number of connections opened with the node
        num_procs: int = 1,
        block_number: int | Literal["latest"] = "latest",
    ) -> None:
        self.rpc_url = rpc_url
        self.calls = calls

        self.num_conns = num_conns
        self.num_procs = num_procs

        self.batch_size = batch_size
        self.require_success = require_success
        self.block_number = block_number

        self.signature = Signature(AGGREGATE_SIGNATURE)
        self.address = hex_to_bytes(MULTICALL_MAP[chain_id])

        timeout = ClientTimeout(
            total=None, connect=None, sock_connect=None, sock_read=None
        )
        connector = TCPConnector(limit=self.num_conns)
        self.http_client = ClientSession(connector=connector, timeout=timeout)

    async def aggregate(self) -> dict[str, Any]:
        pool: nullcontext[SingletonPool] | Pool

        if self.num_procs > 1:
            # using fork server to avoid memory copies
            ctx = mp.get_context("forkserver")
            pool = ctx.Pool(self.num_procs)
        else:
            pool = nullcontext(SingletonPool())
            pass

        with pool as p:
            # step 1: encode individual calls in parallel
            calls: list[tuple[bytes, bytes]] = p.map(
                methodcaller("prepare"), self.calls
            )
            # step 2: batch calls and construct multicall calldatas
            call_batches = self._batch_calls(calls)
            multicalls = p.map(self.construct_multicall, call_batches)

            # step 3: perform eth_calls and aggregate results
            raw_results = await asyncio.gather(
                *[self._eth_call(calldata) for calldata in multicalls]
            )

            # step 4: filter out failed batches
            error_bitmap = [not isinstance(x, bytes) for x in raw_results]
            multicall_decoded_results = p.map(
                self.decode_multicall, (r for r in raw_results if isinstance(r, bytes))
            )
            failed_batches = [
                batch for batch, error in zip(call_batches, error_bitmap) if error
            ]

            # step 5: fallback to standard `eth_call` for failed batches
            fallback_decoded_results = await asyncio.gather(
                *[
                    asyncio.gather(
                        *[
                            (True, call_result)
                            if isinstance(
                                (call_result := self._eth_call(calldata, target)), bytes
                            )
                            else (False, call_result)
                            for calldata, target in batch
                        ]
                    )
                    for batch in failed_batches
                ]
            )

            # step 6: merge call sets
            decoded_results = [
                fallback_decoded_results.pop(0)
                if error
                else multicall_decoded_results.pop(0)
                for error in error_bitmap
            ]

            # step 7: process outputs
            return dict(
                p.starmap(
                    bluebird, zip(repeat("decode_output"), decoded_results, calls)
                )
            )

    def _batch_calls(
        self, calls: list[tuple[bytes, bytes]]
    ) -> list[list[tuple[bytes, bytes]]]:
        return [
            calls[i : i + self.batch_size]
            for i in range(0, len(calls), self.batch_size)
        ]

    def construct_multicall(self, inputs: list[tuple[bytes, bytes]]) -> bytes:
        return self.signature.encode_input((self.require_success, inputs))

    def decode_multicall(self, output: bytes) -> list[tuple[bool, bytes]]:
        return self.signature.decode_output(output)[0]

    @eth_retry.auto_retry
    async def _eth_call(
        self, calldata: bytes, target: bytes | None = None
    ) -> bytes | tuple[JSONRPCErrorCode, str]:
        target = target or self.address
        async with self.http_client.post(
            self.rpc_url,
            json={
                "method": "eth_call",
                "params": [
                    {"to": f"0x{target.hex()}", "data": f"0x{calldata.hex()}"},
                    self.block_number,
                ],
                "id": 1,
                "jsonrpc": "2.0",
            },
        ) as resp:
            if resp.status != 200:
                raise RuntimeError("`eth_call` failed for unknown reason")

            data = await resp.json()
            if "error" in data:
                error = data["error"]
                code, message = error["code"], error["message"]
                return code, message

            return bytes.fromhex(data["result"][2:])


def bluebird(method: str, params: tuple, call: Call):
    return methodcaller(method, *params)(call)
