#!/usr/bin/env python3

from itertools import chain
from random import randbytes
from test.data.tokens import POPULAR_TOKENS
from typing import Any, Literal, cast

import pytest
from pysad.utils import hex_to_bytes

from manifold.call import Call
from manifold.multicall import MultiCall
from manifold.rpc import JSONRPCError

CALLS = cast(
    list[Call[tuple[str, Literal["decimals", "symbol", "token_name"]]]],
    list(
        chain.from_iterable(
            (
                Call(
                    token_address,
                    "decimals()(uint8)",
                    (token_address, "decimals"),
                ),
                Call(
                    token_address,
                    "symbol()(string)",
                    (token_address, "symbol"),
                ),
                Call(
                    token_address,
                    "name()(string)",
                    (token_address, "token_name"),
                ),
            )
            for token_address in POPULAR_TOKENS.keys()
        )
    ),
)


@pytest.mark.parametrize(
    ["num_procs", "batch_divisor"],
    [(1, 1), (1, 4), (1, 8), (2, 2), (3, 2), (4, 1), (8, 1)],
)
def test_multicall(num_procs: int, batch_divisor: int):
    calls = CALLS
    multicall = MultiCall(
        "http://localhost:8090/ethereum",
        calls,
        batch_size=len(calls) // batch_divisor,
        num_procs=num_procs,
    )
    results = multicall.aggregate()
    assert len(results) == len(calls)
    tokens: dict[str, dict[str, Any]] = {}
    for (token, key), value in results.items():
        tokens[token] = tokens.get(token, {}) | {key: value}


def test_block_hash():
    calls = CALLS
    multicall = MultiCall(
        "http://localhost:8090/ethereum",
        calls,
        batch_size=len(calls) // 4,
        block_id=hex_to_bytes(
            "0xf14f9892a9fe7fb38b0d9b43310c10887f00a93e1808dbce8370df9f7c18a541"
        ),
    )
    results = multicall.aggregate()
    assert len(results) == len(calls)

    tokens: dict[str, dict[str, Any]] = {}
    for (token, key), value in results.items():
        tokens[token] = tokens.get(token, {}) | {key: value}


def test_block_hash_fail():
    calls = CALLS
    multicall = MultiCall(
        "http://localhost:8090/ethereum",
        calls,
        batch_size=len(calls) // 4,
        block_id=randbytes(32),
    )
    with pytest.raises(JSONRPCError):
        multicall.aggregate()
