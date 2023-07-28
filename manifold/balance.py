#!/usr/bin/env python3

from itertools import chain
from typing import Literal, Protocol

from msgspec import Struct
from pysad.utils import hex_to_bytes

from manifold.call import Call
from manifold.constants import (
    BCHECKER_ADDRESSES,
    ERC20_BALANCE_SIGNATURE,
    ETH_BALANCE_SIGNATURE,
    NATIVE_ADDRESS,
    NATIVE_BALANCE_SIGNATURE,
    ZERO_ADDRESS,
    MULTICALL_MAP,
    Network,
)
from manifold.log import get_logger
from manifold.multicall import MultiCall
from manifold.utils import batch

log = get_logger()


class BalanceRequest(Protocol):
    token_address: bytes
    owner_address: bytes


class Balance(Struct, gc=False):
    token_address: bytes
    owner_address: bytes
    value: int | None = None


class BalanceChecker:
    rpc_url: str
    calls: list[BalanceRequest]
    batch_size: int  # size of each call batch
    num_procs: int  # number of processes to handle abi encoding/decoding
    chain_id: int
    block_id: int | Literal["latest"] | bytes

    def __init__(
        self,
        rpc_url: str,
        calls: list[BalanceRequest],
        batch_size: int = 1000,
        chain_id: int = 1,
        num_conns: int = 10,  # number of connections opened with the node
        num_procs: int = 1,
        block_id: int | Literal["latest"] | bytes = "latest",
    ) -> None:
        self.rpc_url = rpc_url
        self.calls = calls
        self.chain_id = chain_id

        self.num_conns = num_conns
        self.num_procs = num_procs

        self.batch_size = batch_size
        self.block_id = block_id

        self.address = hex_to_bytes(BCHECKER_ADDRESSES[Network(chain_id)])

    def aggregate(self) -> list[Balance]:
        native_balances, erc20_balances = self._segment_balances()
        balances: list[Balance] = []

        if len(erc20_balances):
            log.debug(f"Processing ERC20 balances [{len(erc20_balances)}]")
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
                block_id=self.block_id,
            )

            balances += [
                Balance(token_address, owner_address, value)
                for (
                    token_address,
                    owner_address,
                ), value in erc20.aggregate().items()
            ]

        if len(native_balances):
            log.debug(f"Processing Native balances [{len(native_balances)}]")
            native = MultiCall(
                self.rpc_url,
                [
                    Call(
                        MULTICALL_MAP[Network(self.chain_id)],
                        ETH_BALANCE_SIGNATURE,
                        (balance.token_address, balance.owner_address),
                        input=(balance.owner_address,),
                    )
                    for balance in native_balances
                ],
                1000,
                require_success=False,
                chain_id=self.chain_id,
                num_conns=self.num_conns,
                num_procs=self.num_procs,
                block_id=self.block_id,
            )

            balances += [
                Balance(token_address, owner_address, value)
                for (
                    token_address,
                    owner_address,
                ), value in native.aggregate().items()
            ]

        return balances

    def _is_native(self, balance: BalanceRequest) -> bool:
        return balance.token_address == NATIVE_ADDRESS

    def _segment_balances(self) -> tuple[list[BalanceRequest], list[BalanceRequest]]:
        native_balances = []
        erc20_balances = []

        for balance in self.calls:
            if self._is_native(balance):
                native_balances.append(balance)
            else:
                erc20_balances.append(balance)

        return native_balances, erc20_balances
