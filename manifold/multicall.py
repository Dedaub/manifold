#!/usr/bin/env python3


import asyncio
import multiprocessing as mp
from contextlib import asynccontextmanager
from itertools import chain
from math import ceil
from multiprocessing.pool import Pool, ThreadPool
from typing import Any, AsyncGenerator, Generic, Iterable, Literal, Type, TypeVar, cast

import msgspec
from aiohttp import ClientSession, ClientTimeout, TCPConnector
from aiohttp.typedefs import LooseHeaders
from msgspec import Struct
from pysad.utils import hex_to_bytes

from manifold.call import Call, THashable
from manifold.constants import AGGREGATE_SIGNATURE, MULTICALL_MAP
from manifold.log import get_logger
from manifold.rpc import HTTPException, JSONRPCError, JSONRPCErrorCode
from manifold.signature import Signature
from manifold.utils import batch

log = get_logger()


class Bytes(bytes):
    @classmethod
    def validate(cls, val: Any):
        return cls(bytes.fromhex(val.removeprefix("0x")))


def dec_hook(type: Type, obj: Any) -> Any:
    # `type` here is the value of the custom type annotation being decoded.
    if type is Bytes:
        return type.validate(obj)
    else:
        # Raise a TypeError for other types
        raise TypeError(f"Objects of type {type} are not supported")


class RPCError(Struct, gc=False):
    code: int
    message: str


class CallResponse(Struct, gc=False):
    result: Bytes | None = None
    error: RPCError | None = None


class MultiCall(Generic[THashable]):
    rpc_url: str
    calls: list[Call[THashable]]
    batch_size: int  # size of each multicall batch
    num_procs: int  # number of processes to handle abi encoding/decoding
    signature: Signature
    address: bytes  # address of the multicall contract
    require_success: bool  # require all calls to succeed
    block_id: int | Literal["latest"] | bytes

    def __init__(
        self,
        rpc_url: str,
        calls: list[Call[THashable]],
        batch_size: int = 1000,
        require_success: bool = False,
        chain_id: int = 1,
        num_conns: int = 10,  # number of connections opened with the node
        num_procs: int = 1,
        block_id: int | Literal["latest"] | bytes = "latest",
        extra_http_headers: LooseHeaders | None = None,
    ) -> None:
        self.rpc_url = rpc_url
        self.calls = calls

        self.num_conns = num_conns
        self.num_procs = num_procs

        self.batch_size = batch_size
        self.require_success = require_success
        self.block_id = block_id

        self.signature = Signature(AGGREGATE_SIGNATURE)
        self.address = hex_to_bytes(MULTICALL_MAP[chain_id])

        self.extra_http_headers = extra_http_headers

    def aggregate(self) -> dict[THashable, Any]:
        pool: ThreadPool | Pool

        if self.num_procs > 1:
            # using fork server to avoid memory copies
            ctx = mp.get_context("forkserver")
            pool = ctx.Pool(self.num_procs)
        else:
            pool = ThreadPool(1)

        with pool as p:
            if len(self.calls) == 0:
                return {}

            call_batches = batch(self.calls, ceil(len(self.calls) / self.num_procs))
            decoded_results = p.map(self.multicall_worker, call_batches)
            log.debug("Returning Results")
            return dict(chain.from_iterable(decoded_results))

    def multicall_worker(
        self, calls: list[Call[THashable]]
    ) -> list[tuple[THashable, Any]]:
        loop = asyncio.new_event_loop()
        ret = loop.run_until_complete(self._multicall_worker(calls))
        loop.close()
        return ret

    async def _multicall_worker(self, calls: list[Call[THashable]]):
        log.debug("Batching Calls")
        call_batches = list(batch(calls, self.batch_size))

        log.debug("Encoding Calldata")
        calldata_batches = [
            [call.prepare() for call in calls] for calls in call_batches
        ]
        log.debug("Constructing Multicalls")
        multicalls = [self.construct_multicall(batch) for batch in calldata_batches]

        ret: list[tuple[THashable, Any]] = []
        async with self.create_http_client(
            headers=self.extra_http_headers
        ) as http_client:
            log.debug("Issuing Multicalls")
            raw_results = await self._bulk_call(http_client, multicalls)

            failed_calls: list[Call[THashable]] = []
            failed_calldatas: list[tuple[bytes, bytes]] = []

            log.debug("Decoding Multicalls")
            for i, (_result, _cbatch) in enumerate(zip(raw_results, call_batches)):
                if _result.result is not None:
                    calls_results = self.decode_multicall(_result.result)
                    ret += [
                        _call.decode_output(*_call_result)
                        for _call, _call_result in zip(_cbatch, calls_results)
                    ]
                else:
                    if (
                        isinstance(self.block_id, bytes)
                        and cast(RPCError, _result.error).code
                        == JSONRPCErrorCode.INVALID_INPUT
                        and cast(RPCError, _result.error).message != "out of gas"
                    ):
                        raise JSONRPCError(_result.error.code, _result.error.message)  # type: ignore

                    failed_calls += _cbatch
                    failed_calldatas += calldata_batches[i]

            if len(failed_calls) == 0:
                return ret

            log.debug("Processing Failed Multicalls")

            raw_results = await self._bulk_call(
                http_client, *swap(tuple(zip(*failed_calldatas)))
            )
            for _result, _call in zip(raw_results, failed_calls):
                ret.append(
                    _call.decode_output(
                        *(
                            (True, cast(bytes, _result.result))
                            if _result.result is not None
                            else (False, b"")
                        )
                    )
                )

            return ret

    @asynccontextmanager
    async def create_http_client(
        self, headers: LooseHeaders | None = None
    ) -> AsyncGenerator[ClientSession, None]:
        timeout = ClientTimeout(
            total=None, connect=None, sock_connect=None, sock_read=None
        )
        connector = TCPConnector(limit=self.num_conns // self.num_procs)

        http_client = ClientSession(
            connector=connector, timeout=timeout, headers=headers
        )

        try:
            yield http_client
        except Exception as e:
            await http_client.close()

            raise e
        finally:
            await http_client.close()

    def construct_multicall(self, inputs: Iterable[tuple[bytes, bytes]]) -> bytes:
        return self.signature.selector + self.signature.encode_input(
            (self.require_success, inputs)
        )

    def decode_multicall(self, output: bytes) -> list[tuple[bool, bytes]]:
        return self.signature.decode_output(output)[0]

    async def _bulk_call(
        self,
        http_client: ClientSession,
        calldatas: Iterable[bytes],
        targets: Iterable[bytes] | None = None,
    ) -> list[CallResponse]:
        raw_results: list[bytes]
        if targets is None:
            raw_results = await asyncio.gather(
                *(self._eth_call(http_client, calldata) for calldata in calldatas)
            )
        else:
            raw_results = await asyncio.gather(
                *(
                    self._eth_call(http_client, calldata, target)
                    for calldata, target in zip(calldatas, targets)
                )
            )

        decoder = msgspec.json.Decoder(CallResponse, dec_hook=dec_hook)

        results: list[CallResponse] = []
        for result in raw_results:
            results.append(decoder.decode(result))

        return results

    async def _eth_call(
        self, http_client: ClientSession, calldata: bytes, target: bytes | None = None
    ) -> bytes:
        target = target or self.address
        async with http_client.post(
            self.rpc_url,
            json={
                "method": "eth_call",
                "params": [
                    {"to": f"0x{target.hex()}", "data": f"0x{calldata.hex()}"},
                    self.block_id
                    if isinstance(self.block_id, (str, int))
                    else "0x" + self.block_id.hex(),
                ],
                "id": 1,
                "jsonrpc": "2.0",
            },
        ) as resp:
            if resp.status != 200:
                text = await resp.text()
                raise HTTPException(status_code=resp.status, text=text)

            return await resp.read()


TX = TypeVar("TX")
TY = TypeVar("TY")


def swap(v: tuple[TX, TY]) -> tuple[TY, TX]:
    x, y = v
    return y, x
