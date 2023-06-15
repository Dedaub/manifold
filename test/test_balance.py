#!/usr/bin/env python3


from random import randbytes
from test.data.balances import ERC20_BALANCES, NATIVE_BALANCES

import pytest
from attr import dataclass
from pysad.utils import hex_to_bytes

from manifold.balance import BalanceChecker
from manifold.rpc import JSONRPCError


@dataclass(hash=True)
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


def test_balances_hash():
    bc = BalanceChecker(
        "http://localhost:8090/ethereum",
        [
            BReq(hex_to_bytes(token_address), hex_to_bytes(owner_address))
            for (token_address, owner_address) in ERC20_BALANCES.keys()
        ],
        block_id=hex_to_bytes(
            "0xf14f9892a9fe7fb38b0d9b43310c10887f00a93e1808dbce8370df9f7c18a541"
        ),
    )

    results = bc.aggregate()
    assert len(results) == len(ERC20_BALANCES.keys())

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


def test_balances_hash_fail():
    bc = BalanceChecker(
        "http://localhost:8090/ethereum",
        [
            BReq(hex_to_bytes(token_address), hex_to_bytes(owner_address))
            for (token_address, owner_address) in ERC20_BALANCES.keys()
        ],
        block_id=randbytes(32),
    )

    with pytest.raises(JSONRPCError):
        bc.aggregate()
