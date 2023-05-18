#!/usr/bin/env python3


from collections.abc import Iterable
from itertools import chain
from typing import Literal, TypeVar

from pysad.utils import hex_to_bytes

from manifold.call import Call
from manifold.constants import (
    BCHECKER_ADDRESSES,
    ERC20_BALANCE_SIGNATURE,
    NATIVE_BALANCE_SIGNATURE,
    Network,
)
from manifold.multicall import MultiCall

ZERO_ADDRESS = b"\x00" * 20
NATIVE_ADDRESS = ZERO_ADDRESS = b"\xee" * 20


T = TypeVar("T")


class BalanceRequest:
    token_address: bytes
    owner_address: bytes

    def __init__(self, token_address: str | bytes, owner_address: str | bytes) -> None:
        self.token_address = hex_to_bytes(token_address)
        self.owner_address = (
            _address
            if (_address := hex_to_bytes(owner_address)) != ZERO_ADDRESS
            else NATIVE_ADDRESS
        )

    def is_native(self) -> bool:
        return self.owner_address == NATIVE_ADDRESS


class Balance(BalanceRequest):
    value: int

    def __init__(
        self, token_address: str | bytes, owner_address: str | bytes, value: int | None
    ) -> None:
        super().__init__(token_address, owner_address)
        self.value = value if value is not None else 0


class BalanceChecker:
    rpc_url: str
    calls: list[BalanceRequest]
    batch_size: int  # size of each multicall batch
    num_procs: int  # number of processes to handle abi encoding/decoding
    chain_id: int
    block_number: int | Literal["latest"]

    def __init__(
        self,
        rpc_url: str,
        calls: list[BalanceRequest],
        batch_size: int = 1000,
        chain_id: int = 1,
        num_conns: int = 10,  # number of connections opened with the node
        num_procs: int = 1,
        block_number: int | Literal["latest"] = "latest",
    ) -> None:
        self.rpc_url = rpc_url
        self.calls = calls
        self.chain_id = chain_id

        self.num_conns = num_conns
        self.num_procs = num_procs

        self.batch_size = batch_size
        self.block_number = block_number

        self.address = hex_to_bytes(BCHECKER_ADDRESSES[Network(chain_id)])

    def aggregate(self) -> list[Balance]:
        native_balances, erc20_balances = self._segment_balances()
        balances: list[Balance] = []

        if len(erc20_balances):
            erc20 = MultiCall(
                self.rpc_url,
                [
                    Call(
                        balance.token_address,
                        ERC20_BALANCE_SIGNATURE,
                        (balance.token_address, balance.owner_address),
                        input=(balance.owner_address,),
                    )
                    for balance in erc20_balances
                ],
                self.batch_size,
                require_success=False,
                chain_id=self.chain_id,
                block_number=self.block_number,
            )

            balances += [
                Balance(token_address, owner_address, value)
                for (
                    token_address,
                    owner_address,
                ), value in erc20.aggregate().items()
            ]

        if len(native_balances):
            native = MultiCall(
                self.rpc_url,
                [
                    Call(
                        self.address,
                        NATIVE_BALANCE_SIGNATURE,
                        tuple(batch),
                        input=(
                            [ZERO_ADDRESS] * len(batch),
                            [balance.owner_address for balance in batch],
                        ),
                    )
                    for batch in self._batch(native_balances)
                ],
                require_success=False,
                chain_id=self.chain_id,
                block_number=self.block_number,
            )

            balances += chain.from_iterable(
                (
                    Balance(balance.token_address, balance.owner_address, value)
                    for balance, value in zip(balances, values)
                )
                for balances, values in native.aggregate().items()
            )

        return balances

    def _batch(self, items: list[T]) -> Iterable[list[T]]:
        pos: int = 0
        while pos < len(items):
            yield items[pos : min(pos + self.batch_size, len(items))]
            pos += self.batch_size

    def _segment_balances(self) -> tuple[list[BalanceRequest], list[BalanceRequest]]:
        native_balances = []
        erc20_balances = []

        for balance in self.calls:
            if balance.is_native():
                native_balances.append(balance)
            else:
                erc20_balances.append(balance)

        return native_balances, erc20_balances
