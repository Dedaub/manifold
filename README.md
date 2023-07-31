# Manifold

Manifold is a utility library for web3 developers designed to wrap around the excellent `Multicall` contracts. The goal of Manifold is to provide a simple and clean python client to support web3 app developers.

## Origins

Manifold started as an internal project at [Dedaub](https://dedaub.com/) as we found the existing `multicall.py` to be somewhat limiting and heavy.

### `throw`/`invalid`

Until the creation of `revert` in [EIP140](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-140.md) Solidity would rely on the `throw` keyword (later designated as `invalid` in [EIP141](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-141.md)) to abort transactions, whilst both opcodes achieve the same goal `throw`/`invalid` will also consume all of the gas allocated to the call. This becomes problematic for uses in ETL (Extract Load Tranform) projects, where the contract being called may `throw` (ex: calling an optional interface method like `symbol`).

To solve this issue Manifold implements an `eth_call` fallback mechanism to ensure that `multicall` batches which would previously have failed due to `out-of-gas` exceptions (caused by a `throw` in the fallback function) are given a second opportunity to complete.

## Usage

Overall `manifold` should be pretty easy to use, the general workflow is as follows. 

```python
calls: list[Call[Literal["decimals", "symbol", "token_name"]]] = [
    Call(
        "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",    # target address
        "decimals()(uint8)",                             # function signature (with optional return)
        ("decimals",),                                   # output label (used to identify the call, generally the func name and address)
    ),
    Call(
        "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        "symbol()(string)",
        ("symbol",),
    ),
    Call(
        "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        "name()(string)",
        ("token_name",),
    ),
]

multicall = MultiCall(
    "http://localhost:8090/ethereum",         # RPC-URL
    calls,                                    
    batch_size=1,                             # Size of each multicall batch
    num_procs=1,                              # Number of processes to use (multiprocessing)
)

# Generics allow us to infer the keys of this mapping to be "decimals", "symbol", or "token_name"
weth: dict[Literal["decimals", "symbol", "token_name"], Any] = multicall.aggregate() 
```

The library takes a list of call objects which each contain all the information relevant to one call; its target, signature, return label, and an optional return processing function. Following this you create a `Multicall` object which handles batching the calls with fallbacks, and optionally processes batches in seperate processes to circumvent possible cpu bottlenecks related to ABI encoding or post-processing. Under the hood the `Multicall` object connects to the rpc using an `asyncio-http` client to parallelize rpc requests, which can be configured via a `num_conns` kwarg.

## Balance Checker

One of the important use cases for this library was extracting balance information on-mass, whether that be for ERC20 tokens or native (ETH, FTM, ...) tokens. As such we created a small addition to this library called `BalanceChecker` which takes a list of `BalanceRequest` and returns a list of `Balance`.

```python
bc = BalanceChecker(
    "http://localhost:8090/ethereum",
    [
        BReq(token_address, owner_address)
        for (token_address, owner_address) in tokens.keys()
    ],
)

balances: dict[tuple[str, str], int] = {
    (
        "0x" + balance.token_address.hex(),
        "0x" + balance.owner_address.hex(),
    ): balance.value or 0
    for balance in bc.aggregate()
}
```

Under the hood the `BalanceChecker` will segment the `BalanceRequest`s into erc20 and native requests, dispatching the native balance calls to the `getEthBalance` function in `Multicall3` and the erc20 to the respective contract. A small optimisation here is that balance requests to the zero-address are performed together, as many ERC20 tokens give special semantic meaning to these addresses and can cause batches to fail.
