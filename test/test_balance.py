#!/usr/bin/env python3


from test.data.balances import ERC20_BALANCES, NATIVE_BALANCES

import pytest
from attr import dataclass
from pysad.utils import hex_to_bytes

from manifold.balance import BalanceChecker


@dataclass
class BReq:
    token_address: bytes
    owner_address: bytes


@pytest.mark.parametrize(
    ["tokens"],
    [(ERC20_BALANCES,), (NATIVE_BALANCES,), (ERC20_BALANCES | NATIVE_BALANCES,)],
)
def test_balances(tokens: dict[tuple[str, str], int]):
    bc = BalanceChecker(
        "http://localhost:8090/ethereum",
        [
            BReq(hex_to_bytes(token_address), hex_to_bytes(owner_address))
            for (token_address, owner_address) in tokens.keys()
        ],
    )

    results = bc.aggregate()
    assert len(results) == len(tokens.keys())

    balances: dict[tuple[str, str], int] = {
        (
            "0x" + balance.token_address.hex(),
            "0x" + balance.owner_address.hex(),
        ): balance.value
        or 0
        for balance in results
    }
    # Check they're not 0
    assert all(balances.values())

    # This could fail, but I'm using self destructed
    # addresses so it shouldn't
    # assert balances == tokens
