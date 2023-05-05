#!/usr/bin/env python3

from itertools import chain
from test.data.tokens import POPULAR_TOKENS
from typing import Any, cast

import pytest

from manifold.call import Call
from manifold.multicall import MultiCall


@pytest.mark.parametrize(
    ["num_procs", "batch_divisor"], [(1, 4), (2, 2), (3, 2), (4, 1)]
)
def test_multicall(num_procs: int, batch_divisor: int):
    calls = list(
        chain.from_iterable(
            (
                Call(
                    token_address,
                    "decimals()(uint8)",
                    (),
                    (token_address, "decimals"),
                ),
                Call(
                    token_address,
                    "symbol()(string)",
                    (),
                    (token_address, "symbol"),
                ),
                Call(
                    token_address,
                    "name()(string)",
                    (),
                    (token_address, "token_name"),
                ),
            )
            for token_address in POPULAR_TOKENS.keys()
        )
    )
    multicall = MultiCall(
        "http://localhost:8090/ethereum", calls, batch_size=len(calls) // 4, num_procs=1
    )
    results = cast(dict[tuple[str, str], Any], multicall.aggregate())
    assert len(results) == len(calls)
    tokens = {}
    for (token, key), value in results.items():
        tokens[token] = tokens.get(token, {}) | {key: value}
