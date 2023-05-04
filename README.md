# Manifold

Manifold is a utility library for web3 developers designed to wrap around the excellent `Multicall` contracts. The goal of Manifold is to provide a simple and clean python client to support web3 app developers.

## Origins

Manifold started as an internal project at [Dedaub](https://dedaub.com/) as we found the existing `multicall.py` to be somewhat limiting and heavy.

### `throw`/`invalid`

Until the creation of `revert` in [EIP140](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-140.md) Solidity would rely on the `throw` keyword (later designated as `invalid` in [EIP141](`https://github.com/ethereum/EIPs/blob/master/EIPS/eip-141.md`)) to abort transactions, whilst both opcodes achieve the same goal `throw`/`invalid` will also consume all of the gas allocated to the call. This becomes problematic for uses in ETL (Extract Load Tranform) projects, where the contract being called may `throw` (ex: calling an optional interface method like `symbol`).

To solve this issue Manifold implements an `eth_call` fallback mechanism to ensure that `multicall` batches which would previously have failed due to `out-of-gas` exceptions (caused by a `throw` in the fallback function) are given a second opportunity to complete.
