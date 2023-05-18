#!/usr/bin/env python3


import asyncio
import multiprocessing as mp
import warnings
from itertools import chain
from math import ceil
from multiprocessing.pool import Pool
from operator import methodcaller
from typing import Any, Generic, Iterable, Literal, cast

import eth_retry
import eth_retry.eth_retry
from aiohttp import ClientSession, ClientTimeout, TCPConnector
from parse import Result, parse  # type: ignore
from pysad.utils import hex_to_bytes

from manifold.call import Call, THashable
from manifold.constants import AGGREGATE_SIGNATURE, MULTICALL_MAP
from manifold.pool import SingletonPool
from manifold.rpc import JSONRPCErrorCode
from manifold.signature import Signature
from manifold.utils import batch

eth_retry.eth_retry.MIN_SLEEP_TIME = 5
eth_retry.eth_retry.MAX_SLEEP_TIME = 10
eth_retry.eth_retry.MAX_RETRIES = 5


class MultiCall(Generic[THashable]):
    rpc_url: str
    calls: list[Call[THashable]]
    batch_size: int  # size of each multicall batch
    num_procs: int  # number of processes to handle abi encoding/decoding
    signature: Signature
    address: bytes  # address of the multicall contract
    require_success: bool  # require all calls to succeed
    block_number: int | Literal["latest"]

    def __init__(
        self,
        rpc_url: str,
        calls: list[Call[THashable]],
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

    def aggregate(self) -> dict[THashable, Any]:
        pool: SingletonPool | Pool

        if self.num_procs > 1:
            # using fork server to avoid memory copies
            ctx = mp.get_context("forkserver")
            pool = ctx.Pool(self.num_procs)
        else:
            pool = SingletonPool()

        with pool as p:
            call_batches = batch(self.calls, ceil(len(self.calls) / self.num_procs))
            decoded_results = p.map(self.multicall_worker, call_batches)
            # step 7: process outputs
            return dict(chain.from_iterable(decoded_results))

    def multicall_worker(
        self, calls: list[Call[THashable]]
    ) -> list[tuple[THashable, Any]]:
        raw_calls = [call.prepare() for call in calls]
        batches = list(batch(raw_calls, self.batch_size))
        multicalls = [self.construct_multicall(batch) for batch in batches]
        loop = asyncio.new_event_loop()
        raw_results = loop.run_until_complete(self.execute_calls(batches, multicalls))
        decoded_results = [
            call.decode_output(*result)
            for call, result in zip(calls, chain.from_iterable(raw_results))
        ]
        return decoded_results

    async def execute_calls(
        self, batches: list[list[tuple[bytes, bytes]]], multicalls: list[bytes]
    ):
        async with self.create_http_client() as http_client:
            raw_results = await asyncio.gather(
                *[
                    self._eth_call(http_client, calldata)  # type: ignore
                    for calldata in multicalls
                ]
            )

            error_bitmap = [not isinstance(x, bytes) for x in raw_results]
            multicall_raw_results = (
                self.decode_multicall(r)
                for r, e in zip(raw_results, error_bitmap)
                if not e
            )
            failed_batches = (
                batch for batch, error in zip(batches, error_bitmap) if error
            )

            fallback_raw_results = await asyncio.gather(
                *[
                    asyncio.gather(
                        *[
                            self._eth_call(http_client, calldata, target)
                            for target, calldata in batch
                        ]
                    )
                    for batch in failed_batches
                ]
            )

            fallback_raw_results = (
                [(isinstance(call, bytes), call) for call in batch]
                for batch in fallback_raw_results
            )

            raw_results = [
                next(fallback_raw_results) if error else next(multicall_raw_results)
                for error in error_bitmap
            ]

            return raw_results

    def create_http_client(self) -> ClientSession:
        timeout = ClientTimeout(
            total=None, connect=None, sock_connect=None, sock_read=None
        )
        connector = TCPConnector(limit=self.num_conns // self.num_procs)
        http_client = ClientSession(connector=connector, timeout=timeout)
        return http_client

    def construct_multicall(self, inputs: Iterable[tuple[bytes, bytes]]) -> bytes:
        return self.signature.selector + self.signature.encode_input(
            (self.require_success, inputs)
        )

    def decode_multicall(self, output: bytes) -> list[tuple[bool, bytes]]:
        return self.signature.decode_output(output)[0]

    # @eth_retry.auto_retry
    async def _eth_call(
        self, http_client: ClientSession, calldata: bytes, target: bytes | None = None
    ) -> bytes | tuple[JSONRPCErrorCode, str]:
        target = target or self.address
        async with http_client.post(
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
                if (
                    lengths := parse(
                        "call retuned result on length {} exceeding limit {}", message
                    )
                ) is not None:
                    lengths = cast(Result, lengths)
                    returned, allowed = lengths[0], lengths[1]
                    warnings.warn(
                        f"Multicall return length ({returned}) exceeds maximum return length ({allowed}), adjust your batch size to prevent fallback calls"
                    )
                return code, message

            return bytes.fromhex(data["result"][2:])


def bluebird(method: str, params: tuple, call: Call):
    return methodcaller(method, *params)(call)
