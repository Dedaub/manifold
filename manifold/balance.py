#!/usr/bin/env python3


from itertools import chain
from typing import Literal

from pysad.utils import hex_to_bytes

from manifold.call import Call
from manifold.constants import (
    BCHECKER_ADDRESSES,
    ERC20_BALANCE_SIGNATURE,
    NATIVE_ADDRESS,
    NATIVE_BALANCE_SIGNATURE,
    ZERO_ADDRESS,
    Network,
)
from manifold.multicall import MultiCall
from manifold.utils import batch


class BalanceRequest:
    token_address: bytes
    owner_address: bytes

    def __init__(self, token_address: str | bytes, owner_address: str | bytes) -> None:
        self.owner_address = hex_to_bytes(owner_address)
        self.token_address = hex_to_bytes(token_address)

    def is_native(self) -> bool:
        return self.token_address == NATIVE_ADDRESS


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
    batch_size: int  # size of each call batch
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
                num_conns=self.num_conns,
                num_procs=self.num_procs,
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
                        tuple(_batch),
                        input=(
                            [balance.owner_address for balance in _batch],
                            [ZERO_ADDRESS],
                        ),
                    )
                    for _batch in batch(native_balances, self.batch_size)
                ],
                1,
                require_success=False,
                chain_id=self.chain_id,
                num_conns=self.num_conns,
                num_procs=self.num_procs,
                block_number=self.block_number,
            )

            results = native.aggregate()
            balances += chain.from_iterable(
                (
                    Balance(balance.token_address, balance.owner_address, value)
                    for balance, value in zip(balances, values)
                )
                for balances, values in results.items()
            )

        return balances

    def _segment_balances(self) -> tuple[list[BalanceRequest], list[BalanceRequest]]:
        native_balances = []
        erc20_balances = []

        for balance in self.calls:
            if balance.is_native():
                native_balances.append(balance)
            else:
                erc20_balances.append(balance)

        return native_balances, erc20_balances
