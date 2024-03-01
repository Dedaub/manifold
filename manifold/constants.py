#!/usr/bin/env python3

from collections import defaultdict
from enum import IntEnum

NATIVE_ADDRESS = b"\xee" * 20


class Network(IntEnum):
    Mainnet = 1
    Ropsten = 3
    Rinkeby = 4
    Gorli = 5
    Optimism = 10
    CostonTestnet = 16
    ThundercoreTestnet = 18
    SongbirdCanaryNetwork = 19
    Cronos = 25
    RSK = 30
    RSKTestnet = 31
    Kovan = 42
    Bsc = 56
    OKC = 66
    OptimismKovan = 69
    BscTestnet = 97
    Gnosis = 100
    Velas = 106
    Thundercore = 108
    Coston2Testnet = 114
    Fuse = 122
    Heco = 128
    Polygon = 137
    Fantom = 250
    Boba = 288
    KCC = 321
    OptimismGorli = 420
    Astar = 592
    Metis = 1088
    Moonbeam = 1284
    Moonriver = 1285
    MoonbaseAlphaTestnet = 1287
    Milkomeda = 2001
    Kava = 2222
    FantomTestnet = 4002
    Canto = 7700
    Klaytn = 8217
    EvmosTestnet = 9000
    Evmos = 9001
    Arbitrum = 42161
    Celo = 42220
    Oasis = 42262
    AvalancheFuji = 43113
    Avax = 43114
    GodwokenTestnet = 71401
    Godwoken = 71402
    Base = 8453
    Mumbai = 80001
    Blast = 81457
    ArbitrumRinkeby = 421611
    ArbitrumGorli = 421613
    Sepolia = 11155111
    Aurora = 1313161554
    Harmony = 1666600000


MULTICALL2_ADDRESSES: dict[int, str] = {
    Network.Mainnet: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Kovan: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Rinkeby: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Gorli: "0x5ba1e12693dc8f9c48aad8770482f4739beed696",
    Network.Gnosis: "0x9903f30c1469d8A2f415D4E8184C93BD26992573",
    Network.Polygon: "0xc8E51042792d7405184DfCa245F2d27B94D013b6",
    Network.Bsc: "0xfF6FD90A470Aaa0c1B8A54681746b07AcdFedc9B",
    Network.Fantom: "0xBAD2B082e2212DE4B065F636CA4e5e0717623d18",
    Network.Moonriver: "0xB44a9B6905aF7c801311e8F4E76932ee959c663C",
    Network.Arbitrum: "0x842eC2c7D803033Edf55E478F461FC547Bc54EB2",
    Network.Avax: "0xdf2122931FEb939FB8Cf4e67Ea752D1125e18858",
    Network.Heco: "0xd1F3BE686D64e1EA33fcF64980b65847aA43D79C",
    Network.Aurora: "0xe0e3887b158F7F9c80c835a61ED809389BC08d1b",
    Network.Cronos: "0x5e954f5972EC6BFc7dECd75779F10d848230345F",
    Network.Optimism: "0x2DC0E2aa608532Da689e89e237dF582B783E552C",
    Network.OptimismKovan: "0x2DC0E2aa608532Da689e89e237dF582B783E552C",
    Network.Kava: "0x45be772faE4a9F31401dfF4738E5DC7DD439aC0b",
}


# based on https://github.com/mds1/multicall#readme
class multicalldict(defaultdict[Network, str]):
    """
    Return the standard Multicall3 address for all networks by default.
    If any network uses a different address, this can be overriden.
    """

    def __missing__(self, __key: Network) -> str:
        try:
            Network(__key)
        except ValueError:
            raise ValueError(f"{__key} is not a supported chain id")

        return "0xcA11bde05977b3631167028862bE2a173976CA11"


MULTICALL3_ADDRESSES = multicalldict()

# Always take latest if available
MULTICALL_MAP: dict[int, str] = MULTICALL2_ADDRESSES | MULTICALL3_ADDRESSES
AGGREGATE_SIGNATURE = "tryAggregate(bool,(address,bytes)[])((bool,bytes)[])"

ERC20_BALANCE_SIGNATURE = "balanceOf(address)(uint256)"
ETH_BALANCE_SIGNATURE = "getEthBalance(address)(uint256)"
