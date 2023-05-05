#!/usr/bin/env python3

POPULAR_TOKENS = {
    "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2": {
        "decimals": 18,
        "symbol": "WETH",
        "token_name": "Wrapped Ether",
    },
    "0xdac17f958d2ee523a2206206994597c13d831ec7": {
        "decimals": 6,
        "symbol": "USDT",
        "token_name": "Tether USD",
    },
    "0x58b6a8a3302369daec383334672404ee733ab239": {
        "decimals": 18,
        "symbol": "LPT",
        "token_name": "Livepeer Token",
    },
    "0x4d224452801aced8b2f0aebe155379bb5d594381": {
        "decimals": 18,
        "symbol": "APE",
        "token_name": "ApeCoin",
    },
    "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0": {
        "decimals": 18,
        "symbol": "MATIC",
        "token_name": "Matic Token",
    },
    "0x514910771af9ca656af840dff83e8264ecf986ca": {
        "decimals": 18,
        "symbol": "LINK",
        "token_name": "ChainLink Token",
    },
    "0xae7ab96520de3a18e5e111b5eaab095312d7fe84": {
        "decimals": 18,
        "symbol": "stETH",
        "token_name": "Liquid staked Ether 2.0",
    },
    "0x31c8eacbffdd875c74b94b077895bd78cf1e64a3": {
        "decimals": 18,
        "symbol": "RAD",
        "token_name": "Radicle",
    },
    "0x4a220e6096b25eadb88358cb44068a3248254675": {
        "decimals": 18,
        "symbol": "QNT",
        "token_name": "Quant",
    },
    "0x4fabb145d64652a948d72533023f6e7a623c7c53": {
        "decimals": 18,
        "symbol": "BUSD",
        "token_name": "Binance USD",
    },
    "0xbe9895146f7af43049ca1c1ae358b0541ea49704": {
        "decimals": 18,
        "symbol": "cbETH",
        "token_name": "Coinbase Wrapped Staked ETH",
    },
    "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984": {
        "decimals": 18,
        "symbol": "UNI",
        "token_name": "Uniswap",
    },
    "0x6de037ef9ad2725eb40118bb1702ebb27e4aeb24": {
        "decimals": 18,
        "symbol": "RNDR",
        "token_name": "Render Token",
    },
    "0x5faa989af96af85384b8a938c2ede4a7378d9875": {
        "decimals": 18,
        "symbol": "GAL",
        "token_name": "Project Galaxy",
    },
    "0x3ecab35b64345bfc472477a653e4a3abe70532d9": {
        "decimals": 18,
        "symbol": "ENTC",
        "token_name": "ENTERBUTTON",
    },
    "0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0": {
        "decimals": 18,
        "symbol": "wstETH",
        "token_name": "Wrapped liquid staked Ether 2.0",
    },
    "0x45804880de22913dafe09f4980848ece6ecbaf78": {
        "decimals": 18,
        "symbol": "PAXG",
        "token_name": "Paxos Gold",
    },
    "0x80f0c1c49891dcfdd40b6e0f960f84e6042bcb6f": {
        "decimals": 18,
        "symbol": "DXN",
        "token_name": "DBXen Token",
    },
    "0x0f51bb10119727a7e5ea3538074fb341f56b09ad": {
        "decimals": 18,
        "symbol": "DAO",
        "token_name": "DAO Maker",
    },
    "0xd33526068d116ce69f19a9ee46f0bd304f21a51f": {
        "decimals": 18,
        "symbol": "RPL",
        "token_name": "Rocket Pool Protocol",
    },
    "0xd26114cd6ee289accf82350c8d8487fedb8a0c07": {
        "decimals": 18,
        "symbol": "OMG",
        "token_name": "OMGToken",
    },
    "0xae78736cd615f374d3085123a210448e74fc6393": {
        "decimals": 18,
        "symbol": "rETH",
        "token_name": "Rocket Pool ETH",
    },
    "0xf57e7e7c23978c3caec3c3548e3d615c346e79ff": {
        "decimals": 18,
        "symbol": "IMX",
        "token_name": "Immutable X",
    },
    "0x5a98fcbea516cf06857215779fd812ca3bef1b32": {
        "decimals": 18,
        "symbol": "LDO",
        "token_name": "Lido DAO Token",
    },
    "0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0": {
        "decimals": 18,
        "symbol": "FXS",
        "token_name": "Frax Share",
    },
    "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9": {
        "decimals": 18,
        "symbol": "AAVE",
        "token_name": "Aave Token",
    },
    "0x853d955acef822db058eb8505911ed77f175b99e": {
        "decimals": 18,
        "symbol": "FRAX",
        "token_name": "Frax",
    },
    "0xd8912c10681d8b21fd3742244f44658dba12264e": {
        "decimals": 18,
        "symbol": "PLU",
        "token_name": "Pluton",
    },
    "0x04fa0d235c4abf4bcf4787af4cf447de572ef828": {
        "decimals": 18,
        "symbol": "UMA",
        "token_name": "UMA Voting Token v1",
    },
    "0x767fe9edc9e0df98e07454847909b5e959d7ca0e": {
        "decimals": 18,
        "symbol": "ILV",
        "token_name": "Illuvium",
    },
    "0xdbdb4d16eda451d0503b854cf79d55697f90c8df": {
        "decimals": 18,
        "symbol": "ALCX",
        "token_name": "Alchemix",
    },
    "0xac3e018457b222d93114458476f3e3416abbe38f": {
        "decimals": 18,
        "symbol": "sfrxETH",
        "token_name": "Staked Frax Ether",
    },
    "0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b": {
        "decimals": 18,
        "symbol": "CVX",
        "token_name": "Convex Token",
    },
    "0x5f98805a4e8be255a32880fdec7f6728c6568ba0": {
        "decimals": 18,
        "symbol": "LUSD",
        "token_name": "LUSD Stablecoin",
    },
    "0x0000000000085d4780b73119b644ae5ecd22b376": {
        "decimals": 18,
        "symbol": "TUSD",
        "token_name": "TrueUSD",
    },
    "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2": {
        "decimals": 18,
        "symbol": None,
        "token_name": None,
    },
    "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2": {
        "decimals": 18,
        "symbol": "SUSHI",
        "token_name": "SushiToken",
    },
    "0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f": {
        "decimals": 18,
        "symbol": "SNX",
        "token_name": "Synthetix Network Token",
    },
    "0xe28b3b32b6c345a34ff64674606124dd5aceca30": {
        "decimals": 18,
        "symbol": "INJ",
        "token_name": "Injective Token",
    },
    "0x92d6c1e31e14520e676a687f0a93788b716beff5": {
        "decimals": 18,
        "symbol": "DYDX",
        "token_name": "dYdX",
    },
    "0xde30da39c46104798bb5aa3fe8b9e0e1f348163f": {
        "decimals": 18,
        "symbol": "GTC",
        "token_name": "Gitcoin",
    },
    "0xa8b919680258d369114910511cc87595aec0be6d": {
        "decimals": 18,
        "symbol": "LYXe",
        "token_name": "LUKSO Token",
    },
    "0x6dea81c8171d0ba574754ef6f8b412f2ed88c54d": {
        "decimals": 18,
        "symbol": "LQTY",
        "token_name": "LQTY",
    },
    "0xb50721bcf8d664c30412cfbc6cf7a15145234ad1": {
        "decimals": 18,
        "symbol": "ARB",
        "token_name": "Arbitrum",
    },
    "0xbb0e17ef65f82ab018d8edd776e8dd940327b28b": {
        "decimals": 18,
        "symbol": "AXS",
        "token_name": "Axie Infinity Shard",
    },
    "0x5e8422345238f34275888049021821e8e08caa1f": {
        "decimals": 18,
        "symbol": "frxETH",
        "token_name": "Frax Ether",
    },
    "0x1776e1f26f98b1a5df9cd347953a26dd3cb46671": {
        "decimals": 18,
        "symbol": "NMR",
        "token_name": "Numeraire",
    },
    "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9": {
        "decimals": 18,
        "symbol": "FTX Token",
        "token_name": "FTT",
    },
    "0x3aada3e213abf8529606924d8d1c55cbdc70bf74": {
        "decimals": 18,
        "symbol": "XMON",
        "token_name": "XMON",
    },
    "0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5": {
        "decimals": 9,
        "symbol": "OHM",
        "token_name": "Olympus",
    },
    "0xc00e94cb662c3520282e6f5717214004a7f26888": {
        "decimals": 18,
        "symbol": "COMP",
        "token_name": "Compound",
    },
    "0xc18360217d8f7ab5e7c516566761ea12ce7f9d72": {
        "decimals": 18,
        "symbol": "ENS",
        "token_name": "Ethereum Name Service",
    },
    "0x33349b282065b0284d756f0577fb39c158f935e6": {
        "decimals": 18,
        "symbol": "MPL",
        "token_name": "Maple Token",
    },
    "0xba41ddf06b7ffd89d1267b5a93bfef2424eb2003": {
        "decimals": 18,
        "symbol": "MYTH",
        "token_name": "Mythos",
    },
    "0x9e32b13ce7f2e80a01932b42553652e053d6ed8e": {
        "decimals": 18,
        "symbol": "Metis",
        "token_name": "Metis Token",
    },
    "0xc0c293ce456ff0ed870add98a0828dd4d2903dbf": {
        "decimals": 18,
        "symbol": "AURA",
        "token_name": "Aura",
    },
    "0x69af81e73a73b40adf4f3d4223cd9b1ece623074": {
        "decimals": 18,
        "symbol": "MASK",
        "token_name": "Mask Network",
    },
    "0x27c70cd1946795b66be9d954418546998b546634": {
        "decimals": 18,
        "symbol": "LEASH",
        "token_name": "DOGE KILLER",
    },
    "0xba100000625a3754423978a60c9317c58a424e3d": {
        "decimals": 18,
        "symbol": "BAL",
        "token_name": "Balancer",
    },
    "0xc55126051b22ebb829d00368f4b12bde432de5da": {
        "decimals": 18,
        "symbol": "BTRFLY",
        "token_name": "BTRFLY",
    },
    "0x030ba81f1c18d280636f32af80b9aad02cf0854e": {
        "decimals": 18,
        "symbol": "aWETH",
        "token_name": "Aave interest bearing WETH",
    },
    "0xb0b195aefa3650a6908f15cdac7d92f8a5791b0b": {
        "decimals": 18,
        "symbol": "BOB",
        "token_name": "BOB",
    },
    "0x9ae380f0272e2162340a5bb646c354271c0f5cfc": {
        "decimals": 18,
        "symbol": "CNC",
        "token_name": "Conic Finance Token",
    },
    "0x056fd409e1d7a124bd7017459dfea2f387b6d5cd": {
        "decimals": 2,
        "symbol": "GUSD",
        "token_name": "Gemini dollar",
    },
    "0xed1840223484483c0cb050e6fc344d1ebf0778a9": {
        "decimals": 18,
        "symbol": "bendWETH",
        "token_name": "Bend interest bearing WETH",
    },
    "0xb8c77482e45f1f44de1745f52c74426c631bdd52": {
        "decimals": 18,
        "symbol": "BNB",
        "token_name": "BNB",
    },
    "0xb23d80f5fefcddaa212212f028021b41ded428cf": {
        "decimals": 18,
        "symbol": "PRIME",
        "token_name": "Prime",
    },
    "0x4385328cc4d643ca98dfea734360c0f596c83449": {
        "decimals": 18,
        "symbol": "TOMI",
        "token_name": "tomi Token",
    },
    "0xd3e4ba569045546d09cf021ecc5dfe42b1d7f6e4": {
        "decimals": 18,
        "symbol": "MNW",
        "token_name": "Morpheus.Network",
    },
    "0xbcca60bb61934080951369a648fb03df4f96263c": {
        "decimals": 6,
        "symbol": "aUSDC",
        "token_name": "Aave interest bearing USDC",
    },
    "0xbbc2ae13b23d715c30720f079fcd9b4a74093505": {
        "decimals": 18,
        "symbol": "ERN",
        "token_name": "@EthernityChain $ERN Token",
    },
    "0x87dde3a3f4b629e389ce5894c9a1f34a7eec5648": {
        "decimals": 18,
        "symbol": "bendDebtWETH",
        "token_name": "Bend debt bearing WETH",
    },
    "0x152649ea73beab28c5b49b26eb48f7ead6d4c898": {
        "decimals": 18,
        "symbol": "Cake",
        "token_name": "PancakeSwap Token",
    },
    "0x6810e776880c02933d47db1b9fc05908e5386b96": {
        "decimals": 18,
        "symbol": "GNO",
        "token_name": "Gnosis Token",
    },
    "0x4d5f47fa6a74757f35c14fd3a6ef8e3c9bc514e8": {
        "decimals": 18,
        "symbol": "aEthWETH",
        "token_name": "Aave Ethereum WETH",
    },
    "0x607f4c5bb672230e8672085532f7e901544a7375": {
        "decimals": 9,
        "symbol": "RLC",
        "token_name": "iEx.ec Network Token",
    },
    "0x430ef9263e76dae63c84292c3409d61c598e9682": {
        "decimals": 18,
        "symbol": "PYR",
        "token_name": "PYR Token",
    },
    "0x0ab87046fbb341d058f17cbc4c1133f25a20a52f": {
        "decimals": 18,
        "symbol": "gOHM",
        "token_name": "Governance OHM",
    },
    "0x6c3f90f043a72fa612cbac8115ee7e52bde6e490": {
        "decimals": 18,
        "symbol": "3Crv",
        "token_name": "Curve.fi DAI/USDC/USDT",
    },
    "0xd084944d3c05cd115c09d072b9f44ba3e0e45921": {
        "decimals": 18,
        "symbol": "FOLD",
        "token_name": "Manifold Finance",
    },
    "0xf16e81dce15b08f326220742020379b855b87df9": {
        "decimals": 18,
        "symbol": "ICE",
        "token_name": "IceToken",
    },
    "0x1abaea1f7c830bd89acc67ec4af516284b1bc33c": {
        "decimals": 6,
        "symbol": "EUROC",
        "token_name": "Euro Coin",
    },
    "0x9d65ff81a3c488d585bbfb0bfe3c7707c7917f54": {
        "decimals": 18,
        "symbol": "SSV",
        "token_name": "SSV Token",
    },
    "0xaaf448d30f01b429fb6e7f9af6a8ff66e694f312": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0xd9fcd98c322942075a5c3860693e9f4f03aae07b": {
        "decimals": 18,
        "symbol": "EUL",
        "token_name": "Euler",
    },
    "0x0b38210ea11411557c13457d4da7dc6ea731b88a": {
        "decimals": 18,
        "symbol": "API3",
        "token_name": "API3",
    },
    "0xd46ba6d942050d489dbd938a2c909a5d5039a161": {
        "decimals": 9,
        "symbol": "AMPL",
        "token_name": "Ampleforth",
    },
    "0xfa5047c9c78b8877af97bdcb85db743fd7313d4a": {
        "decimals": 18,
        "symbol": "ROOK",
        "token_name": "ROOK",
    },
    "0x892a6f9df0147e5f079b0993f486f9aca3c87881": {
        "decimals": 9,
        "symbol": "xFUND",
        "token_name": "unification.com/xfund",
    },
    "0x32a7c02e79c4ea1008dd6564b35f131428673c41": {
        "decimals": 18,
        "symbol": "CRU",
        "token_name": "CRUST",
    },
    "0xec67005c4e498ec7f55e092bd1d35cbc47c91892": {
        "decimals": 18,
        "symbol": "MLN",
        "token_name": "Melon Token",
    },
    "0xa117000000f279d81a1d3cc75430faa017fa5a2e": {
        "decimals": 18,
        "symbol": "ANT",
        "token_name": "Aragon Network Token",
    },
    "0xd31a59c85ae9d8edefec411d448f90841571b89c": {
        "decimals": 9,
        "symbol": "SOL",
        "token_name": "Wrapped SOL",
    },
    "0x30d20208d987713f46dfd34ef128bb16c404d10f": {
        "decimals": 18,
        "symbol": "SD",
        "token_name": "Stader",
    },
    "0xfca59cd816ab1ead66534d82bc21e7515ce441cf": {
        "decimals": 18,
        "symbol": "RARI",
        "token_name": "Rarible",
    },
    "0xa9b1eb5908cfc3cdf91f9b8b3a74108598009096": {
        "decimals": 18,
        "symbol": "Auction",
        "token_name": "Bounce Token",
    },
    "0x6100dd79fcaa88420750dcee3f735d168abcb771": {
        "decimals": 18,
        "symbol": "SOON",
        "token_name": "NONbeta",
    },
    "0x2e9d63788249371f1dfc918a52f8d799f4a38c94": {
        "decimals": 18,
        "symbol": "TOKE",
        "token_name": "Tokemak",
    },
    "0x72953a5c32413614d24c29c84a66ae4b59581bbf": {
        "decimals": 18,
        "symbol": "CLEV",
        "token_name": "CLever Token",
    },
    "0xcb84d72e61e383767c4dfeb2d8ff7f4fb89abc6e": {
        "decimals": 18,
        "symbol": "VEGA",
        "token_name": "VEGA",
    },
    "0xfcf8eda095e37a41e002e266daad7efc1579bc0a": {
        "decimals": 18,
        "symbol": "FLEX",
        "token_name": "FLEX Coin",
    },
    "0x7e77dcb127f99ece88230a64db8d595f31f1b068": {
        "decimals": 18,
        "symbol": "sILV2",
        "token_name": "Escrowed Illuvium 2",
    },
    "0x582d872a1b094fc48f5de31d3b73f2d9be47def1": {
        "decimals": 9,
        "symbol": "TONCOIN",
        "token_name": "Wrapped TON Coin",
    },
    "0x221657776846890989a759ba2973e427dff5c9bb": {
        "decimals": 18,
        "symbol": "REPv2",
        "token_name": "Reputation",
    },
    "0x2ebd53d035150f328bd754d6dc66b99b0edb89aa": {
        "decimals": 18,
        "symbol": "MET",
        "token_name": "Metronome2",
    },
    "0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68": {
        "decimals": 18,
        "symbol": "INV",
        "token_name": "Inverse DAO",
    },
    "0x77e06c9eccf2e797fd462a92b6d7642ef85b0a44": {
        "decimals": 9,
        "symbol": "wTAO",
        "token_name": "Wrapped TAO",
    },
    "0x9b2b931d6ab97b6a887b2c5d8529537e6fe73ebe": {
        "decimals": 9,
        "symbol": "AllIn",
        "token_name": "All In",
    },
    "0x81f8f0bb1cb2a06649e51913a151f0e7ef6fa321": {
        "decimals": 18,
        "symbol": "VITA",
        "token_name": "VitaDAO Token",
    },
    "0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0": {
        "decimals": 18,
        "symbol": "TRB",
        "token_name": "Tellor Tributes",
    },
    "0x845c0179060362f071ff5c7f1d2703617a480f3e": {
        "decimals": 18,
        "symbol": "VERSE-X",
        "token_name": "Verse Exchange",
    },
    "0x3472a5a71965499acd81997a54bba8d852c6e53d": {
        "decimals": 18,
        "symbol": "BADGER",
        "token_name": "Badger",
    },
    "0xb6ca7399b4f9ca56fc27cbff44f4d2e4eef1fc81": {
        "decimals": 18,
        "symbol": "MUSE",
        "token_name": "Muse",
    },
    "0x429881672b9ae42b8eba0e26cd9c73711b891ca5": {
        "decimals": 18,
        "symbol": "PICKLE",
        "token_name": "PickleToken",
    },
    "0x6a091a3406e0073c3cd6340122143009adac0eda": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x7659ce147d0e714454073a5dd7003544234b6aa0": {
        "decimals": 18,
        "symbol": "XCAD",
        "token_name": "XCAD Token",
    },
    "0x3ed3b47dd13ec9a98b44e6204a523e766b225811": {
        "decimals": 6,
        "symbol": "aUSDT",
        "token_name": "Aave interest bearing USDT",
    },
    "0x1a7e4e63778b4f12a199c062f3efdd288afcbce8": {
        "decimals": 18,
        "symbol": "agEUR",
        "token_name": "agEUR",
    },
    "0x95b3497bbcccc46a8f45f5cf54b0878b39f8d96c": {
        "decimals": 18,
        "symbol": "UNIDX",
        "token_name": "UniDex",
    },
    "0x3a856d4effa670c54585a5d523e96513e148e95d": {
        "decimals": 18,
        "symbol": "TRIAS",
        "token_name": "Trias Token",
    },
    "0x4c11249814f11b9346808179cf06e71ac328c1b5": {
        "decimals": 18,
        "symbol": "ORAI",
        "token_name": "Oraichain Token",
    },
    "0xd9c2d319cd7e6177336b0a9c93c21cb48d84fb54": {
        "decimals": 18,
        "symbol": "HAPI",
        "token_name": "HAPI",
    },
    "0x1e4746dc744503b53b4a082cb3607b169a289090": {
        "decimals": 18,
        "symbol": "IPOR",
        "token_name": "IPOR Token",
    },
    "0xc2544a32872a91f4a553b404c6950e89de901fdb": {
        "decimals": 18,
        "symbol": "FPIS",
        "token_name": "Frax Price Index Share",
    },
    "0xfe2e637202056d30016725477c5da089ab0a043a": {
        "decimals": 18,
        "symbol": "sETH2",
        "token_name": "StakeWise Staked ETH2",
    },
    "0x40fd72257597aa14c7231a7b1aaa29fce868f677": {
        "decimals": 18,
        "symbol": "XOR",
        "token_name": "Sora Token",
    },
    "0x16eccfdbb4ee1a85a33f3a9b21175cd7ae753db4": {
        "decimals": 18,
        "symbol": "ROUTE",
        "token_name": "Route",
    },
    "0x1ceb5cb57c4d4e2b2433641b95dd330a33185a44": {
        "decimals": 18,
        "symbol": "KP3R",
        "token_name": "Keep3rV1",
    },
    "0xf63b34710400cad3e044cffdcab00a0f32e33ecf": {
        "decimals": 18,
        "symbol": "variableDebtWETH",
        "token_name": "Aave variable debt bearing WETH",
    },
    "0xf1b99e3e573a1a9c5e6b2ce818b617f0e664e86b": {
        "decimals": 18,
        "symbol": "oSQTH",
        "token_name": "Opyn Squeeth",
    },
    "0xba11d00c5f74255f56a5e366f4f77f5a186d7f55": {
        "decimals": 18,
        "symbol": "BAND",
        "token_name": "BandToken",
    },
    "0x616e8bfa43f920657b3497dbf40d6b1a02d4608d": {
        "decimals": 18,
        "symbol": "auraBAL",
        "token_name": "Aura BAL",
    },
    "0x5c6ee304399dbdb9c8ef030ab642b10820db8f56": {
        "decimals": 18,
        "symbol": "B-80BAL-20WETH",
        "token_name": "Balancer 80 BAL 20 WETH",
    },
    "0x71ab77b7dbb4fa7e017bc15090b2163221420282": {
        "decimals": 18,
        "symbol": "HIGH",
        "token_name": "Highstreet token",
    },
    "0x823e1b82ce1dc147bbdb25a203f046afab1ce918": {
        "decimals": 18,
        "symbol": "COIL",
        "token_name": "Coil",
    },
    "0x531842cebbdd378f8ee36d171d6cc9c4fcf475ec": {
        "decimals": 6,
        "symbol": "variableDebtUSDT",
        "token_name": "Aave variable debt bearing USDT",
    },
    "0x227c7df69d3ed1ae7574a1a7685fded90292eb48": {
        "decimals": 18,
        "symbol": "MILADY",
        "token_name": "Milady Maker",
    },
    "0x34f0915a5f15a66eba86f6a58be1a471fb7836a7": {
        "decimals": 12,
        "symbol": "PLSD",
        "token_name": "PulseDogecoin",
    },
    "0xb39185e33e8c28e0bb3dbbce24da5dea6379ae91": {
        "decimals": 18,
        "symbol": "PHUNK",
        "token_name": "CryptoPhunks",
    },
    "0x7d647b1a0dcd5525e9c6b3d14be58f27674f8c95": {
        "decimals": 18,
        "symbol": "BYTES",
        "token_name": "BYTES",
    },
    "0x87f92191e14d970f919268045a57f7be84559cea": {
        "decimals": 18,
        "symbol": "vDebtWETH",
        "token_name": "ParaSpace Variable Debt Token WETH",
    },
    "0xa1d0e215a23d7030842fc67ce582a6afa3ccab83": {
        "decimals": 18,
        "symbol": "YFII",
        "token_name": "YFII.finance",
    },
    "0x0100546f2cd4c9d97f798ffc9755e47865ff7ee6": {
        "decimals": 18,
        "symbol": "alETH",
        "token_name": "Alchemix ETH",
    },
    "0x0391d2021f89dc339f60fff84546ea23e337750f": {
        "decimals": 18,
        "symbol": "BOND",
        "token_name": "BarnBridge Governance Token",
    },
    "0xdc0327d50e6c73db2f8117760592c8bbf1cdcf38": {
        "decimals": 18,
        "symbol": "STRNGR",
        "token_name": "Stronger",
    },
    "0x8f3470a7388c05ee4e7af3d01d8c722b0ff52374": {
        "decimals": 18,
        "symbol": "VERI",
        "token_name": "Veritaseum",
    },
    "0xa0246c9032bc3a600820415ae600c6388619a14d": {
        "decimals": 18,
        "symbol": "FARM",
        "token_name": "FARM Reward Token",
    },
    "0xe95a203b1a91a908f9b9ce46459d101078c2c3cb": {
        "decimals": 18,
        "symbol": "ankrETH",
        "token_name": "Ankr Staked ETH",
    },
    "0x77fba179c79de5b7653f68b5039af940ada60ce0": {
        "decimals": 18,
        "symbol": "FORTH",
        "token_name": "Ampleforth Governance",
    },
    "0xf433089366899d83a9f26a773d59ec7ecf30355e": {
        "decimals": 8,
        "symbol": "MTL",
        "token_name": "Metal",
    },
    "0x485d17a6f1b8780392d53d64751824253011a260": {
        "decimals": 8,
        "symbol": "TIME",
        "token_name": "ChronoTech Token",
    },
    "0x498c00e1ccc2afff80f6cc6144eaeb95c46cc3b5": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x65ef703f5594d2573eb71aaf55bc0cb548492df4": {
        "decimals": 18,
        "symbol": "MULTI",
        "token_name": "Multichain",
    },
    "0x111111517e4929d3dcbdfa7cce55d30d4b6bc4d6": {
        "decimals": 18,
        "symbol": "ICHI",
        "token_name": "ICHI",
    },
    "0x6f259637dcd74c767781e37bc6133cd6a68aa161": {
        "decimals": 18,
        "symbol": "HT",
        "token_name": "HuobiToken",
    },
    "0xc6dddb5bc6e61e0841c54f3e723ae1f3a807260b": {
        "decimals": 18,
        "symbol": "URUS",
        "token_name": "Aurox Token",
    },
    "0x57ab1ec28d129707052df4df418d58a2d46d5f51": {
        "decimals": 18,
        "symbol": "sUSD",
        "token_name": "Synth sUSD",
    },
    "0x96e61422b6a9ba0e068b6c5add4ffabc6a4aae27": {
        "decimals": 18,
        "symbol": "ibEUR",
        "token_name": "Iron Bank EUR",
    },
    "0xdb25f211ab05b1c97d595516f45794528a807ad8": {
        "decimals": 2,
        "symbol": "EURS",
        "token_name": "STASIS EURS Token",
    },
    "0xac51066d7bec65dc4589368da368b212745d63e8": {
        "decimals": 6,
        "symbol": "ALICE",
        "token_name": "ALICE",
    },
    "0xba58444c8050ed9385b7417533a73644036d21eb": {
        "decimals": 18,
        "symbol": "LOGT",
        "token_name": " Lord of Dragons Governance Token",
    },
    "0xcc802c45b55581713cecd1eb17be9ab7fccb0844": {
        "decimals": 18,
        "symbol": "BHNY",
        "token_name": "SBU Honey",
    },
    "0x045da4bfe02b320f4403674b3b7d121737727a36": {
        "decimals": 18,
        "symbol": "DCHF",
        "token_name": "Defi Franc",
    },
    "0x1982b2f5814301d4e9a8b0201555376e62f82428": {
        "decimals": 18,
        "symbol": "aSTETH",
        "token_name": "Aave interest bearing STETH",
    },
    "0x3f382dbd960e3a9bbceae22651e88158d2791550": {
        "decimals": 18,
        "symbol": "GHST",
        "token_name": "Aavegotchi GHST Token",
    },
    "0x9559aaa82d9649c7a7b220e7c461d2e74c9a3593": {
        "decimals": 18,
        "symbol": "rETH",
        "token_name": "StaFi",
    },
    "0x1494ca1f11d487c2bbe4543e90080aeba4ba3c2b": {
        "decimals": 18,
        "symbol": "DPI",
        "token_name": "DefiPulse Index",
    },
    "0x6c3c78838c761c6ac7be9f59fe808ea2a6e4379d": {
        "decimals": 18,
        "symbol": "variableDebtDAI",
        "token_name": "Aave variable debt bearing DAI",
    },
    "0xadb2437e6f65682b85f814fbc12fec0508a7b1d0": {
        "decimals": 18,
        "symbol": "UNCX",
        "token_name": "UniCrypt",
    },
    "0xc4c7ea4fab34bd9fb9a5e1b1a98df76e26e6407c": {
        "decimals": 18,
        "symbol": "COCOS",
        "token_name": "CocosTokenV2",
    },
    "0xf89060c99853bb52eaf5f2247d007d73de660252": {
        "decimals": 18,
        "symbol": "WBESC",
        "token_name": "Wrapped BESC from BESC",
    },
    "0x11eef04c884e24d9b7b4760e7476d06ddf797f36": {
        "decimals": 18,
        "symbol": "MX",
        "token_name": "MX Token",
    },
    "0x6df1c1e379bc5a00a7b4c6e67a203333772f45a8": {
        "decimals": 6,
        "symbol": "variableDebtEthUSDT",
        "token_name": "Aave Ethereum Variable Debt USDT",
    },
    "0xc581b735a1688071a1746c968e0798d642ede491": {
        "decimals": 6,
        "symbol": "EURT",
        "token_name": "Euro Tether",
    },
    "0xea51d7853eefb32b6ee06b1c12e6dcca88be0ffe": {
        "decimals": 18,
        "symbol": "variableDebtEthWETH",
        "token_name": "Aave Ethereum Variable Debt WETH",
    },
    "0x87de305311d5788e8da38d19bb427645b09cb4e5": {
        "decimals": 18,
        "symbol": "VRX",
        "token_name": "Verox",
    },
    "0xb95bd0793bcc5524af358ffaae3e38c3903c7626": {
        "decimals": 18,
        "symbol": "uDAI",
        "token_name": "UwU interest bearing DAI",
    },
    "0xdf801468a808a32656d2ed2d2d80b72a129739f4": {
        "decimals": 8,
        "symbol": "CUBE",
        "token_name": "Somnium Space Cubes",
    },
    "0x72e364f2abdc788b7e918bc238b21f109cd634d7": {
        "decimals": 18,
        "symbol": "MVI",
        "token_name": "Metaverse Index",
    },
    "0x77777feddddffc19ff86db637967013e6c6a116c": {
        "decimals": 18,
        "symbol": "TORN",
        "token_name": "TornadoCash",
    },
    "0xedb171c18ce90b633db442f2a6f72874093b49ef": {
        "decimals": 18,
        "symbol": "WAMPL",
        "token_name": "Wrapped Ampleforth",
    },
    "0x8a854288a5976036a725879164ca3e91d30c6a1b": {
        "decimals": 18,
        "symbol": "GET",
        "token_name": "GET",
    },
    "0x7de91b204c1c737bcee6f000aaa6569cf7061cb7": {
        "decimals": 9,
        "symbol": "XRT",
        "token_name": "Robonomics",
    },
    "0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5": {
        "decimals": 8,
        "symbol": "cETH",
        "token_name": "Compound Ether",
    },
    "0xaa6e8127831c9de45ae56bb1b0d4d4da6e5665bd": {
        "decimals": 18,
        "symbol": "ETH2x-FLI",
        "token_name": "ETH 2x Flexible Leverage Index",
    },
    "0xb59490ab09a0f526cc7305822ac65f2ab12f9723": {
        "decimals": 18,
        "symbol": "LIT",
        "token_name": "Litentry",
    },
    "0xb753428af26e81097e7fd17f40c88aaa3e04902c": {
        "decimals": 18,
        "symbol": "SFI",
        "token_name": "Spice",
    },
    "0x35f6b052c598d933d69a4eec4d04c73a191fe6c2": {
        "decimals": 18,
        "symbol": "aSNX",
        "token_name": "Aave interest bearing SNX",
    },
    "0xabe580e7ee158da464b51ee1a83ac0289622e6be": {
        "decimals": 18,
        "symbol": "XFT",
        "token_name": "Offshift",
    },
    "0x11ebe21e9d7bf541a18e1e3ac94939018ce88f0b": {
        "decimals": 18,
        "symbol": "pitchFXS",
        "token_name": "Pitch FXS",
    },
    "0x4a08cf0a7bca217c24b9ee99c0395052f3707d68": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x68749665ff8d2d112fa859aa293f07a622782f38": {
        "decimals": 6,
        "symbol": "XAUt",
        "token_name": "Tether Gold",
    },
    "0x4e352cf164e64adcbad318c3a1e222e9eba4ce42": {
        "decimals": 18,
        "symbol": "MCB",
        "token_name": "MCDEX Token",
    },
    "0x55c08ca52497e2f1534b59e2917bf524d4765257": {
        "decimals": 18,
        "symbol": "UwU",
        "token_name": "UwU Lend",
    },
    "0x35bd01fc9d6d5d81ca9e055db88dc49aa2c699a8": {
        "decimals": 18,
        "symbol": "FWB",
        "token_name": "Friends With Benefits Pro",
    },
    "0x6243d8cea23066d098a15582d81a598b4e8391f4": {
        "decimals": 18,
        "symbol": "FLX",
        "token_name": "Flex Ungovernance Token",
    },
    "0xbc4171f45ef0ef66e76f979df021a34b46dcc81d": {
        "decimals": 18,
        "symbol": "DORA",
        "token_name": "Dorayaki",
    },
    "0x559ebe4e206e6b4d50e9bd3008cda7ce640c52cb": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x0b925ed163218f6662a35e0f0371ac234f9e9371": {
        "decimals": 18,
        "symbol": "aEthwstETH",
        "token_name": "Aave Ethereum wstETH",
    },
    "0xbd2949f67dcdc549c6ebe98696449fa79d988a9f": {
        "decimals": 18,
        "symbol": "eMTRG",
        "token_name": "Meter Governance mapped by Meter.io",
    },
    "0x8798249c2e607446efb7ad49ec89dd1865ff4272": {
        "decimals": 18,
        "symbol": "xSUSHI",
        "token_name": "SushiBar",
    },
    "0x8c1bed5b9a0928467c9b1341da1d7bd5e10b6549": {
        "decimals": 18,
        "symbol": "LsETH",
        "token_name": "Liquid Staked ETH",
    },
    "0x101cc05f4a51c0319f570d5e146a8c625198e636": {
        "decimals": 18,
        "symbol": "aTUSD",
        "token_name": "Aave interest bearing TUSD",
    },
    "0xf66cd2f8755a21d3c8683a10269f795c0532dd58": {
        "decimals": 18,
        "symbol": "CoreDAO",
        "token_name": "CORE DAO",
    },
    "0x836a808d4828586a69364065a1e064609f5078c7": {
        "decimals": 18,
        "symbol": "pETH",
        "token_name": "JPEG’d ETH",
    },
    "0x0954906da0bf32d5479e25f46056d22f08464cab": {
        "decimals": 18,
        "symbol": "INDEX",
        "token_name": "Index",
    },
    "0xa2847348b58ced0ca58d23c7e9106a49f1427df6": {
        "decimals": 18,
        "symbol": "cvxFPIS",
        "token_name": "Convex FPIS",
    },
    "0xd075e95423c5c4ba1e122cae0f4cdfa19b82881b": {
        "decimals": 18,
        "symbol": "wPE",
        "token_name": "OPES Finance",
    },
    "0xaf988aff99d3d0cb870812c325c588d8d8cb7de8": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x75231f58b43240c9718dd58b4967c5114342a86c": {
        "decimals": 18,
        "symbol": "OKB",
        "token_name": "OKB",
    },
    "0x9ea3b5b4ec044b70375236a281986106457b20ef": {
        "decimals": 18,
        "symbol": "DELTA",
        "token_name": "DELTA.financial - deep DeFi derivatives",
    },
    "0x418d75f65a02b3d53b2418fb8e1fe493759c7605": {
        "decimals": 18,
        "symbol": "WBNB",
        "token_name": "Wrapped BNB",
    },
    "0xc4c346edc55504574cceb00aa1091d22404a4bc3": {
        "decimals": 18,
        "symbol": "MEZZ",
        "token_name": "MEZZ Token",
    },
    "0x7c9f4c87d911613fe9ca58b579f737911aad2d43": {
        "decimals": 18,
        "symbol": "WMATIC",
        "token_name": "Wrapped Matic",
    },
    "0x24a6a37576377f63f194caa5f518a60f45b42921": {
        "decimals": 18,
        "symbol": "BANK",
        "token_name": "Float Bank",
    },
    "0xaa4b6506493582f169c9329ac0da99fff23c2911": {
        "decimals": 18,
        "symbol": "pWETH",
        "token_name": "ParaSpace Derivative Token WETH",
    },
    "0x6f40d4a6237c257fff2db00fa0510deeecd303eb": {
        "decimals": 18,
        "symbol": "INST",
        "token_name": "Instadapp",
    },
    "0xcf8d0c70c850859266f5c338b38f9d663181c314": {
        "decimals": 18,
        "symbol": "variableDebtEthDAI",
        "token_name": "Aave Ethereum Variable Debt DAI",
    },
    "0x471ea49dd8e60e697f4cac262b5fafcc307506e4": {
        "decimals": 10,
        "symbol": "xcRMRK",
        "token_name": "xcRMRK",
    },
    "0x7a2bc711e19ba6aff6ce8246c546e8c4b4944dfd": {
        "decimals": 8,
        "symbol": "WAXE",
        "token_name": "WAX Economic Token",
    },
    "0xd8e3fb3b08eba982f2754988d70d57edc0055ae6": {
        "decimals": 9,
        "symbol": "ZORA",
        "token_name": "Zoracles",
    },
    "0x82698aecc9e28e9bb27608bd52cf57f704bd1b83": {
        "decimals": 18,
        "symbol": "bb-a-USDC",
        "token_name": "Balancer Aave Boosted Pool (USDC)",
    },
    "0xfc82bb4ba86045af6f327323a46e80412b91b27d": {
        "decimals": 18,
        "symbol": "PROM",
        "token_name": "Token Prometeus Network",
    },
    "0x1b5036bec1b82d44d52fa953a370b3c6cd9328b5": {
        "decimals": 18,
        "symbol": "ELAN",
        "token_name": "Elan",
    },
    "0x0d88ed6e74bbfd96b831231638b66c05571e824f": {
        "decimals": 18,
        "symbol": None,
        "token_name": "",
    },
    "0xba485b556399123261a5f9c95d413b4f93107407": {
        "decimals": 18,
        "symbol": "graviAURA",
        "token_name": "Gravitationally Bound AURA",
    },
    "0x333a4823466879eef910a04d473505da62142069": {
        "decimals": 18,
        "symbol": "NATION",
        "token_name": "Nation3",
    },
    "0x7c07f7abe10ce8e33dc6c5ad68fe033085256a84": {
        "decimals": 18,
        "symbol": "icETH",
        "token_name": "Interest Compounding ETH Index",
    },
    "0x94b86ca6f7a495930fe7f552eb9e4cbb5ef2b736": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0xb4272071ecadd69d933adcd19ca99fe80664fc08": {
        "decimals": 18,
        "symbol": "XCHF",
        "token_name": "CryptoFranc",
    },
    "0x34b6f33a5d88fca1b8f78a510bc81673611a68f0": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xfc98e825a2264d890f9a1e68ed50e1526abccacd": {
        "decimals": 18,
        "symbol": "MCO2",
        "token_name": "Moss Carbon Credit",
    },
    "0x570febdf89c07f256c75686caca215289bb11cfc": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xd3e31f8aac930e354283ca3efda1e22525f98af1": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x232fb065d9d24c34708eedbf03724f2e95abe768": {
        "decimals": 18,
        "symbol": "SHEESHA",
        "token_name": "Sheesha Finance",
    },
    "0x90de74265a416e1393a450752175aed98fe11517": {
        "decimals": 18,
        "symbol": "UDT",
        "token_name": "Unlock Discount Token",
    },
    "0xcc9ee9483f662091a1de4795249e24ac0ac2630f": {
        "decimals": 18,
        "symbol": "aEthrETH",
        "token_name": "Aave Ethereum rETH",
    },
    "0xa258c4606ca8206d8aa700ce2143d7db854d168c": {
        "decimals": 18,
        "symbol": "yvWETH",
        "token_name": "WETH yVault",
    },
    "0x37c997b35c619c21323f3518b9357914e8b99525": {
        "decimals": 18,
        "symbol": "PILOT",
        "token_name": "Unipilot",
    },
    "0xfeef77d3f69374f66429c91d732a244f074bdf74": {
        "decimals": 18,
        "symbol": "cvxFXS",
        "token_name": "Convex FXS",
    },
    "0xccf4429db6322d5c611ee964527d42e5d685dd6a": {
        "decimals": 8,
        "symbol": "cWBTC",
        "token_name": "Compound Wrapped BTC",
    },
    "0xcaeaf8381d4b20b43afa42061d6f80319a8881f6": {
        "decimals": 8,
        "symbol": "R34P",
        "token_name": "R34P",
    },
    "0xde5ed76e7c05ec5e4572cfc88d1acea165109e44": {
        "decimals": 18,
        "symbol": "DEUS",
        "token_name": "DEUS",
    },
    "0x4a2b4f76ab77c7ee3820f16967741209d0a8779e": {
        "decimals": 18,
        "symbol": "CLP",
        "token_name": "Convergence LP Token",
    },
    "0x73c69d24ad28e2d43d03cbf35f79fe26ebde1011": {
        "decimals": 18,
        "symbol": "ARCH",
        "token_name": "ARCH",
    },
    "0xf4cd3d3fda8d7fd6c5a500203e38640a70bf9577": {
        "decimals": 18,
        "symbol": "Yf-DAI",
        "token_name": "YfDAI.finance",
    },
    "0xf59257e961883636290411c11ec5ae622d19455e": {
        "decimals": 9,
        "symbol": "FLOOR",
        "token_name": "Floor",
    },
    "0x5e8c8a7243651db1384c0ddfdbe39761e8e7e51a": {
        "decimals": 18,
        "symbol": "aEthLINK",
        "token_name": "Aave Ethereum LINK",
    },
    "0x4a86c01d67965f8cb3d0aaa2c655705e64097c31": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x70401dfd142a16dc7031c56e862fc88cb9537ce0": {
        "decimals": 18,
        "symbol": "BIRD",
        "token_name": "Bird.Money",
    },
    "0x6c28aef8977c9b773996d0e8376d2ee379446f2f": {
        "decimals": 18,
        "symbol": "QUICK",
        "token_name": "Quickswap",
    },
    "0xfb19075d77a0f111796fb259819830f4780f1429": {
        "decimals": 6,
        "symbol": "FB",
        "token_name": "Fenerbahce Token",
    },
    "0x8e964e35a76103af4c7d7318e1b1a82c682ae296": {
        "decimals": 18,
        "symbol": "FLZ",
        "token_name": "Fellaz Token",
    },
    "0x0b498ff89709d3838a063f1dfa463091f9801c2b": {
        "decimals": 18,
        "symbol": "BTC2x-FLI",
        "token_name": "BTC 2x Flexible Leverage Index",
    },
    "0x0d438f3b5175bebc262bf23753c1e53d03432bde": {
        "decimals": 18,
        "symbol": "wNXM",
        "token_name": "Wrapped NXM",
    },
    "0x441761326490cacf7af299725b6292597ee822c2": {
        "decimals": 18,
        "symbol": "UNFI",
        "token_name": "UNFI",
    },
    "0x15a8e38942f9e353bec8812763fb3c104c89ecf4": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x667102bd3413bfeaa3dffb48fa8288819e480a88": {
        "decimals": 8,
        "symbol": "TKX",
        "token_name": "Tokenize Emblem",
    },
    "0xb0c7a3ba49c7a6eaba6cd4a96c55a1391070ac9a": {
        "decimals": 18,
        "symbol": "MAGIC",
        "token_name": "MAGIC",
    },
    "0xefb47fcfcad4f96c83d4ca676842fb03ef20a477": {
        "decimals": 18,
        "symbol": "SSLP",
        "token_name": "ShibaSwap LP Token",
    },
    "0xc15e41eb55af2c0f7c34fb150a688f672d4b1be2": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xc3f279090a47e80990fe3a9c30d24cb117ef91a8": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x88acdd2a6425c3faae4bc9650fd7e27e0bebb7ab": {
        "decimals": 18,
        "symbol": "⚗️",
        "token_name": "Alchemist",
    },
    "0xe66747a101bff2dba3697199dcce5b743b454759": {
        "decimals": 18,
        "symbol": "GT",
        "token_name": "GateChainToken",
    },
    "0x9af15d7b8776fa296019979e70a5be53c714a7ec": {
        "decimals": 18,
        "symbol": "EVN",
        "token_name": "Evn Token",
    },
    "0x2a9bdcff37ab68b95a53435adfd8892e86084f93": {
        "decimals": 18,
        "symbol": "AQT",
        "token_name": "Alpha Quark Token",
    },
    "0x1637e4e9941d55703a7a5e7807d6ada3f7dcd61b": {
        "decimals": 18,
        "symbol": "XINV",
        "token_name": "xINV",
    },
    "0x6b4c7a5e3f0b99fcd83e9c089bddd6c7fce5c611": {
        "decimals": 18,
        "symbol": "MM",
        "token_name": "Million",
    },
    "0x49b4f92431c5b8cf260f983c4d3ed28e1fd0b991": {
        "decimals": 18,
        "symbol": "JOJO",
        "token_name": "JoJos Adventure",
    },
    "0x0ff5a8451a839f5f0bb3562689d9a44089738d11": {
        "decimals": 18,
        "symbol": "rDPX",
        "token_name": "Dopex Rebate Token",
    },
    "0xa914a9b9e03b6af84f9c6bd2e0e8d27d405695db": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x9ff68f61ca5eb0c6606dc517a9d44001e564bb66": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x341c05c0e9b33c0e38d64de76516b2ce970bb3be": {
        "decimals": 18,
        "symbol": "dsETH",
        "token_name": "Diversified Staked ETH Index (dsETH)",
    },
    "0x5a7e6c8204a1359db9aacab7ba5fc309b7981efd": {
        "decimals": 18,
        "symbol": "anonUSD",
        "token_name": "anonUSD",
    },
    "0x82917fb0dd65b0e5c85eea66e4f5c1ed484bc629": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x4dd28568d05f09b02220b09c2cb307bfd837cb95": {
        "decimals": 18,
        "symbol": "PRINTS",
        "token_name": "Fingerprints",
    },
    "0x470e8de2ebaef52014a47cb5e6af86884947f08c": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xffe136de12a2cd95f64cef9f36414c93e9003959": {
        "decimals": 18,
        "symbol": "DUCK",
        "token_name": "SupDucks",
    },
    "0xda30f261a962d5aae94c9ecd170544600d193766": {
        "decimals": 18,
        "symbol": "ORBR",
        "token_name": "Orbler",
    },
    "0xb3ad645db386d7f6d753b2b9c3f4b853da6890b8": {
        "decimals": 18,
        "symbol": "CTR",
        "token_name": "Concentrator Token",
    },
    "0xde4ee8057785a7e8e800db58f9784845a5c2cbd6": {
        "decimals": 18,
        "symbol": "DEXE",
        "token_name": "Dexe",
    },
    "0x9ee91f9f426fa633d227f7a9b000e28b9dfd8599": {
        "decimals": 18,
        "symbol": "stMATIC",
        "token_name": "Staked MATIC",
    },
    "0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b": {
        "decimals": 18,
        "symbol": "NXM",
        "token_name": "NXM",
    },
    "0x89509aa1d14a8e1e5364ec4c3b041213bcdbe08d": {
        "decimals": 18,
        "symbol": "ZURR",
        "token_name": "ZURRENCY",
    },
    "0xaffcdd96531bcd66faed95fc61e443d08f79efef": {
        "decimals": 5,
        "symbol": "PMGT",
        "token_name": "Perth Mint Gold Token",
    },
    "0x97bbbc5d96875fb78d2f14b7ff8d7a3a74106f17": {
        "decimals": 18,
        "symbol": "ASTRAFER",
        "token_name": "Astrafer",
    },
    "0xc3d088842dcf02c13699f936bb83dfbbc6f721ab": {
        "decimals": 18,
        "symbol": "vETH",
        "token_name": "Voucher Ethereum",
    },
    "0xda816459f1ab5631232fe5e97a05bbbb94970c95": {
        "decimals": 18,
        "symbol": "yvDAI",
        "token_name": "DAI yVault",
    },
    "0x7a5ce6abd131ea6b148a022cb76fc180ae3315a6": {
        "decimals": 18,
        "symbol": "bALPHA",
        "token_name": "bAlpha",
    },
    "0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3": {
        "decimals": 18,
        "symbol": "LEO",
        "token_name": "Bitfinex LEO Token",
    },
    "0x2e7b0d4f9b2eaf782ed3d160e3a0a4b1a7930ada": {
        "decimals": 18,
        "symbol": "CERES",
        "token_name": "Ceres",
    },
    "0x2f4eb47a1b1f4488c71fc10e39a4aa56af33dd49": {
        "decimals": 18,
        "symbol": "UNCL",
        "token_name": "UNCL",
    },
    "0x000000007a58f5f58e697e51ab0357bc9e260a04": {
        "decimals": 18,
        "symbol": "CNV",
        "token_name": "Concave",
    },
    "0x74232704659ef37c08995e386a2e26cc27a8d7b1": {
        "decimals": 18,
        "symbol": "STRK",
        "token_name": "Strike Token",
    },
    "0xac0c8da4a4748d8d821a0973d00b157aa78c473d": {
        "decimals": 18,
        "symbol": "YFO",
        "token_name": "YFIONE",
    },
    "0x03ab458634910aad20ef5f1c8ee96f1d6ac54919": {
        "decimals": 18,
        "symbol": "RAI",
        "token_name": "Rai Reflex Index",
    },
    "0x321c2fe4446c7c963dc41dd58879af648838f98d": {
        "decimals": 18,
        "symbol": "CTX",
        "token_name": "Cryptex",
    },
    "0x798d1be841a82a273720ce31c822c61a67a601c3": {
        "decimals": 9,
        "symbol": "DIGG",
        "token_name": "Digg",
    },
    "0x06026f4c1f180fb51e1c1ed723949823c3d1c6eb": {
        "decimals": 6,
        "symbol": "pUSDT",
        "token_name": "ParaSpace Derivative Token USDT",
    },
    "0xbb39009067c304d760dd5bf36a09f40906116885": {
        "decimals": 18,
        "symbol": "vDebtFRAX",
        "token_name": "ParaSpace Variable Debt Token FRAX",
    },
    "0xb9d7cb55f463405cdfbe4e90a6d2df01c2b92bf1": {
        "decimals": 18,
        "symbol": "aUNI",
        "token_name": "Aave interest bearing UNI",
    },
    "0xc3d03e4f041fd4cd388c549ee2a29a9e5075882f": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x33652e48e4b74d18520f11bfe58edd2ed2cec5a2": {
        "decimals": 18,
        "symbol": "variableDebtEthLUSD",
        "token_name": "Aave Ethereum Variable Debt LUSD",
    },
    "0x01c0eb1f8c6f1c1bf74ae028697ce7aa2a8b0e92": {
        "decimals": 18,
        "symbol": "variableDebtTUSD",
        "token_name": "Aave variable debt bearing TUSD",
    },
    "0x20bc832ca081b91433ff6c17f85701b6e92486c5": {
        "decimals": 18,
        "symbol": "rETH2",
        "token_name": "StakeWise Reward ETH2",
    },
    "0x05767d9ef41dc40689678ffca0608878fb3de906": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x00a35fd824c717879bf370e70ac6868b95870dfb": {
        "decimals": 18,
        "symbol": "IB",
        "token_name": "IronBank",
    },
    "0x795065dcc9f64b5614c407a6efdc400da6221fb0": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0xb63b606ac810a52cca15e44bb630fd42d8d1d83d": {
        "decimals": 8,
        "symbol": "MCO",
        "token_name": "Monaco",
    },
    "0x60ef1e0bf9218cdc1769a43c4b0b111ed38bb418": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x47110d43175f7f2c2425e7d15792acc5817eb44f": {
        "decimals": 18,
        "symbol": "GMI",
        "token_name": "Bankless DeFi Innovation Index",
    },
    "0x3231cb76718cdef2155fc47b5286d82e6eda273f": {
        "decimals": 18,
        "symbol": "EURe",
        "token_name": "Monerium EUR emoney",
    },
    "0xf99d58e463a2e07e5692127302c20a191861b4d6": {
        "decimals": 18,
        "symbol": "ANY",
        "token_name": "Anyswap",
    },
    "0xa354f35829ae975e850e23e9615b11da1b3dc4de": {
        "decimals": 6,
        "symbol": "yvUSDC",
        "token_name": "USDC yVault",
    },
    "0xaf95d3a7a25f831dc2b9a6704554435957b51ec2": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x68037790a0229e9ce6eaa8a99ea92964106c4703": {
        "decimals": 18,
        "symbol": "PAR",
        "token_name": "PAR Stablecoin",
    },
    "0x275f5ad03be0fa221b4c6649b8aee09a42d9412a": {
        "decimals": 18,
        "symbol": "MONA",
        "token_name": "Monavale",
    },
    "0xee586e7eaad39207f0549bc65f19e336942c992f": {
        "decimals": 18,
        "symbol": "cEUR",
        "token_name": "Celo Euro",
    },
    "0x9ce115f0341ae5dabc8b477b74e83db2018a6f42": {
        "decimals": 18,
        "symbol": "HAIR",
        "token_name": "HairDAO Token",
    },
    "0xda3706c9a099077e6bc389d1baf918565212a54d": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x86b4dbe5d203e634a12364c0e428fa242a3fba98": {
        "decimals": 18,
        "symbol": "GBPT",
        "token_name": "poundtoken",
    },
    "0x1b8568fbb47708e9e9d31ff303254f748805bf21": {
        "decimals": 18,
        "symbol": "SCX",
        "token_name": "Scarcity",
    },
    "0x602414a63c90801dc4337ee440b3454a6d2c275b": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x3322f41dfa379b6d3050c1e271b0b435b3ee3303": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x85f138bfee4ef8e540890cfb48f620571d67eda3": {
        "decimals": 18,
        "symbol": "WAVAX",
        "token_name": "Wrapped AVAX",
    },
    "0x3e04863dba602713bb5d0edbf7db7c3a9a2b6027": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x4527a3b4a8a150403090a99b87effc96f2195047": {
        "decimals": 8,
        "symbol": "P2PS",
        "token_name": "P2P Solutions Foundation",
    },
    "0x663242d053057f317a773d7c262b700616d0b9a0": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x8d1ce361eb68e9e05573443c407d4a3bed23b033": {
        "decimals": 18,
        "symbol": "DEFI++",
        "token_name": "PieDAO DEFI++",
    },
    "0x61eb53ee427ab4e007d78a9134aacb3101a2dc23": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x5996c0bc398d37046a76d69c92e285f23d61bf17": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x31503dcb60119a812fee820bb7042752019f2355": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x642431623ae5d73c19fc931aaea0d4677303880c": {
        "decimals": 18,
        "symbol": "vAMM-SOLID/WETH",
        "token_name": "VolatileV2 AMM - SOLID/WETH",
    },
    "0x269db91fc3c7fcc275c2e6f22e5552504512811c": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0xb6909b960dbbe7392d405429eb2b3649752b4838": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x0bec54c89a7d9f15c4e7faa8d47adedf374462ed": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0xe4f726adc8e89c6a6017f01eada77865db22da14": {
        "decimals": 18,
        "symbol": "BCP",
        "token_name": "PieDAO Balanced Crypto Pie",
    },
    "0x7c5a5d535871e9a3c7fd3a76d7d995792c537b57": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x788b6d2b37aa51d916f2837ae25b05f0e61339d1": {
        "decimals": 9,
        "symbol": "MVD",
        "token_name": "Metavault DAO",
    },
    "0x3d3f13f2529ec3c84b2940155effbf9b39a8f3ec": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x336ef4e633b1117dca08c1a57f4139c62c32c935": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x76ec974feaf0293f64cf8643e0f42dea5b71689b": {
        "decimals": 18,
        "symbol": "SSLP",
        "token_name": "ShibaSwap LP Token",
    },
    "0xed92bfe08de542bbb40fdbe0a27ca66313c0c457": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x99b975590364dfdea0ed8550d0d862c78e07c43d": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x22b15c7ee1186a7c7cffb2d942e20fc228f6e4ed": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x41bfba56b9ba48d0a83775d89c247180617266bc": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x2f956b2f801c6dad74e87e7f45c94f6283bf0f45": {
        "decimals": 6,
        "symbol": "iUSDC",
        "token_name": "dForce USDC",
    },
    "0xae8593dd575fe29a9745056aa91c4b746eee62c8": {
        "decimals": 18,
        "symbol": "variableDebtEthrETH",
        "token_name": "Aave Ethereum Variable Debt rETH",
    },
    "0x23878914efe38d27c4d67ab83ed1b93a74d4086a": {
        "decimals": 6,
        "symbol": "aEthUSDT",
        "token_name": "Aave Ethereum USDT",
    },
    "0xa0d52b957420b366176cc6862db5b7973f9a45d2": {
        "decimals": 18,
        "symbol": "SSLP",
        "token_name": "ShibaSwap LP Token",
    },
    "0xdb06a76733528761eda47d356647297bc35a98bd": {
        "decimals": 18,
        "symbol": "SLP",
        "token_name": "SushiSwap LP Token",
    },
    "0x3da932456d082cba208feb0b096d49b202bf89c8": {
        "decimals": 18,
        "symbol": "DEGOV2",
        "token_name": "dego.finance",
    },
    "0x6c5024cd4f8a59110119c56f8933403a539555eb": {
        "decimals": 18,
        "symbol": "aSUSD",
        "token_name": "Aave interest bearing SUSD",
    },
    "0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359": {
        "decimals": 18,
        "symbol": None,
        "token_name": None,
    },
    "0xf29ae508698bdef169b89834f76704c3b205aedf": {
        "decimals": 18,
        "symbol": "yvSNX",
        "token_name": "SNX yVault",
    },
    "0x2be5e8c109e2197d077d13a82daead6a9b3433c5": {
        "decimals": 18,
        "symbol": "TON",
        "token_name": "Tokamak Network Token",
    },
    "0x34612903db071e888a4dadcaa416d3ee263a87b9": {
        "decimals": 18,
        "symbol": "arte",
        "token_name": "ethart",
    },
    "0x2f4eb100552ef93840d5adc30560e5513dfffacb": {
        "decimals": 18,
        "symbol": "bb-a-USDT",
        "token_name": "Balancer Aave Boosted Pool (USDT)",
    },
    "0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a": {
        "decimals": 11,
        "symbol": "ADS",
        "token_name": "Adshares",
    },
    "0xe803178b48a0e560c2b19f3b3d4e504f79d229ce": {
        "decimals": 18,
        "symbol": "BOBC",
        "token_name": "BOBC",
    },
    "0x21fe646d1ed0733336f2d4d9b2fe67790a6099d9": {
        "decimals": 6,
        "symbol": "saUSDT",
        "token_name": "Static Aave interest bearing USDT",
    },
    "0x8d96b4ab6c741a4c8679ae323a100d74f085ba8f": {
        "decimals": 18,
        "symbol": "BZR",
        "token_name": "BAZAARS",
    },
    "0x69fa8e7f6bf1ca1fb0de61e1366f7412b827cc51": {
        "decimals": 9,
        "symbol": "NRCH",
        "token_name": "EnreachDAO",
    },
    "0x908d6032b34576bbb5447c4c3e9042a77aedc17f": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x7cdc560cc66126a5eb721e444abc30eb85408f7a": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x26cc6a87cc9c97fd7d52fa1dbfde0ede2714da61": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x977b6fc5de62598b08c85ac8cf2b745874e8b78c": {
        "decimals": 18,
        "symbol": "aEthcbETH",
        "token_name": "Aave Ethereum cbETH",
    },
    "0x131157c6760f78f7ddf877c0019eba175ba4b6f6": {
        "decimals": 18,
        "symbol": "BigSB",
        "token_name": "BigShortBets",
    },
    "0xd3d2e2692501a5c9ca623199d38826e513033a17": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xa06bc25b5805d5f8d82847d191cb4af5a3e873e0": {
        "decimals": 18,
        "symbol": "aLINK",
        "token_name": "Aave interest bearing LINK",
    },
    "0xfe8f19b17ffef0fdbfe2671f248903055afaa8ca": {
        "decimals": 18,
        "symbol": "variableDebtFRAX",
        "token_name": "Aave variable debt bearing FRAX",
    },
    "0x5f0e628b693018f639d10e4a4f59bd4d8b2b6b44": {
        "decimals": 18,
        "symbol": "WHITE",
        "token_name": "Whiteheart Token",
    },
    "0xeef9f339514298c6a857efcfc1a762af84438dee": {
        "decimals": 18,
        "symbol": "HEZ",
        "token_name": "Hermez Network Token",
    },
    "0x1571ed0bed4d987fe2b498ddbae7dfa19519f651": {
        "decimals": 18,
        "symbol": "iFARM",
        "token_name": "iFARM",
    },
    "0xf59ae934f6fe444afc309586cc60a84a0f89aaea": {
        "decimals": 18,
        "symbol": "PDEX",
        "token_name": "Polkadex",
    },
    "0x25647e01bd0967c1b9599fa3521939871d1d0888": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xfbbe9b1142c699512545f47937ee6fae0e4b0aa9": {
        "decimals": 18,
        "symbol": "EDDA",
        "token_name": "EDDA",
    },
    "0x383518188c0c6d7730d91b2c03a03c837814a899": {
        "decimals": 9,
        "symbol": "OHM",
        "token_name": "Olympus",
    },
    "0xe6fd75ff38adca4b97fbcd938c86b98772431867": {
        "decimals": 18,
        "symbol": "ELA",
        "token_name": "ELA on Ethereum",
    },
    "0x0acc0fee1d86d2cd5af372615bf59b298d50cd69": {
        "decimals": 18,
        "symbol": "ILSI",
        "token_name": "Invest Like Stakeborg Index",
    },
    "0xbab761277f52fff80e35a961b4c63e95c733ddbf": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x67fadbd9bf8899d7c578db22d7af5e2e500e13e5": {
        "decimals": 18,
        "symbol": "uWETH",
        "token_name": "UwU interest bearing WETH",
    },
    "0xe5a3229ccb22b6484594973a03a3851dcd948756": {
        "decimals": 18,
        "symbol": "RAE",
        "token_name": "RAE Token",
    },
    "0x1e6bb68acec8fefbd87d192be09bb274170a0548": {
        "decimals": 9,
        "symbol": "aAMPL",
        "token_name": "Aave interest bearing AMPL",
    },
    "0xcf4236db746dbc1855a4d095aaf58da9b030491e": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xa700b4eb416be35b2911fd5dee80678ff64ff6c9": {
        "decimals": 18,
        "symbol": "aEthAAVE",
        "token_name": "Aave Ethereum AAVE",
    },
    "0xebd754bbbf9b4b6ea9535bd041044e8e5aacc498": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x0e85fb1be698e777f2185350b4a52e5ee8df51a6": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xf03a7eb46d01d9ecaa104558c732cf82f6b6b645": {
        "decimals": 18,
        "symbol": "MaticX",
        "token_name": "Liquid Staking Matic",
    },
    "0x1cdd2eab61112697626f7b4bb0e23da4febf7b7c": {
        "decimals": 6,
        "symbol": "USDT",
        "token_name": "USDT",
    },
    "0x2779cfdf67d45875f3ed89cd7654547ef2dded0d": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x3bd2035d08363a8cfdab70a41b0faad3510492dc": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x51d5c5d784334a4b52a07ac13d9db79cbefa1642": {
        "decimals": 6,
        "symbol": "sUSDC",
        "token_name": "Sturdy interest bearing USDC",
    },
    "0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x4e977830ba4bd783c0bb7f15d3e243f73ff57121": {
        "decimals": 18,
        "symbol": "stableDebtWETH",
        "token_name": "Aave stable debt bearing WETH",
    },
    "0x60c384e226b120d93f3e0f4c502957b2b9c32b15": {
        "decimals": 6,
        "symbol": "saUSDC",
        "token_name": "Static Aave interest bearing USDC",
    },
    "0xd4937682df3c8aef4fe912a96a74121c0829e664": {
        "decimals": 18,
        "symbol": "aFRAX",
        "token_name": "Aave interest bearing FRAX",
    },
    "0x8a458a9dc9048e005d22849f470891b840296619": {
        "decimals": 18,
        "symbol": "aEthMKR",
        "token_name": "Aave Ethereum MKR",
    },
    "0x2516e7b3f76294e03c42aa4c5b5b4dce9c436fb8": {
        "decimals": 18,
        "symbol": "aEthBAL",
        "token_name": "Aave Ethereum BAL",
    },
    "0xa361718326c15715591c299427c62086f69923d9": {
        "decimals": 18,
        "symbol": "aBUSD",
        "token_name": "Aave interest bearing BUSD",
    },
    "0xa1d65e8fb6e87b60feccbc582f7f97804b725521": {
        "decimals": 18,
        "symbol": "DXD",
        "token_name": "DXdao",
    },
    "0x2b1d36f5b61addaf7da7ebbd11b35fd8cfb0de31": {
        "decimals": 18,
        "symbol": "ITP",
        "token_name": "Interport Token",
    },
    "0x4688a8b1f292fdab17e9a90c8bc379dc1dbd8713": {
        "decimals": 18,
        "symbol": "COVER",
        "token_name": "Cover Protocol Governance Token",
    },
    "0xcbc1aa6961b28cccb11e1cddd84ad8b42ec920b1": {
        "decimals": 4,
        "symbol": "ZEUS",
        "token_name": "ZEUS10000",
    },
    "0x5ca3cec889ee6e2e0295c79cfbc057cfeba78cc6": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x2ba592f78db6436527729929aaf6c908497cb200": {
        "decimals": 18,
        "symbol": "CREAM",
        "token_name": "Cream",
    },
    "0x75311ee016c82e7770e4aca73a0d142f96ddb969": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x9abe34021128c17de3c2180a02932eb5e1bb18ef": {
        "decimals": 18,
        "symbol": "variableDebtLUSD",
        "token_name": "UwU variable debt bearing LUSD",
    },
    "0x018008bfb33d285247a21d44e50697654f754e63": {
        "decimals": 18,
        "symbol": "aEthDAI",
        "token_name": "Aave Ethereum DAI",
    },
    "0x60c7aea107ea3cdab21455e187cfb7e54e09b760": {
        "decimals": 18,
        "symbol": "MEME",
        "token_name": "MEME",
    },
    "0x220b71671b649c03714da9c621285943f3cbcdc6": {
        "decimals": 18,
        "symbol": "DIS",
        "token_name": "TosDis",
    },
    "0x8c07e1dfede38b1908698988b4202a87e0d7a0f7": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xfb5453340c03db5ade474b27e68b6a9c6b2823eb": {
        "decimals": 18,
        "symbol": "ROBOT",
        "token_name": "MetaFactory",
    },
    "0xd5525d397898e5502075ea5e830d8914f6f0affe": {
        "decimals": 8,
        "symbol": "MEME",
        "token_name": "MEME",
    },
    "0x8328c886cd4176759bfc4a6a8f9c6973cfee3d65": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x3fe6a295459fae07df8a0cecc36f37160fe86aa9": {
        "decimals": 18,
        "symbol": "aEthLUSD",
        "token_name": "Aave Ethereum LUSD",
    },
    "0x003b3109d25b55bba1518c507a8e5be94f551175": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x7f38d60d94652072b2c44a18c0e14a481ec3c0dd": {
        "decimals": 18,
        "symbol": "stableDebtTUSD",
        "token_name": "Aave stable debt bearing TUSD",
    },
    "0xf136d7b0b7ae5b86d21e7b78dfa95375a7360f19": {
        "decimals": 18,
        "symbol": "TOSHI",
        "token_name": "Toshi Token",
    },
    "0x641927e970222b10b2e8cdbc96b1b4f427316f16": {
        "decimals": 18,
        "symbol": "MEEB",
        "token_name": "Meebits",
    },
    "0xadfa5fa0c51d11b54c8a0b6a15f47987bd500086": {
        "decimals": 18,
        "symbol": "uLUSD",
        "token_name": "UwU interest bearing LUSD",
    },
    "0xc8af46fdc7a8a286aed762a1a9f3f4c3e30af912": {
        "decimals": 18,
        "symbol": "pAPE",
        "token_name": "ParaSpace Derivative Token APE",
    },
    "0xf7970499814654cd13cb7b6e7634a12a7a8a9abc": {
        "decimals": 18,
        "symbol": "TOM",
        "token_name": "TOM",
    },
    "0x10bc518c32fbae5e38ecb50a612160571bd81e44": {
        "decimals": 8,
        "symbol": "VRO",
        "token_name": "veraone",
    },
    "0xed279fdd11ca84beef15af5d39bb4d4bee23f0ca": {
        "decimals": 18,
        "symbol": "LUSD3CRV-f",
        "token_name": "Curve.fi Factory USD Metapool: Liquity",
    },
    "0x1533f61facb7cc3a632b12ea9f55d3fbb57309e0": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x0b85b3000bef3e26e01428d1b525a532ea7513b8": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x276d2b35b4204e8c3a5c2b9031ca63e72acb00de": {
        "decimals": 8,
        "symbol": "tWETH",
        "token_name": "Tonpound Wrapped ETH",
    },
    "0x0557df767419296474c3f551bb0a0ed4c2dd3380": {
        "decimals": 5,
        "symbol": "UPXAU",
        "token_name": "Universal Gold",
    },
    "0xbc562bf2c1445707e5f8df66dbf8eee60cc49a59": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x3f4fa4937e72991367dc32687bc3278f095e7eaa": {
        "decimals": 18,
        "symbol": "variableDebtAmmDAI",
        "token_name": "Aave AMM Market variable debt AmmDAI",
    },
    "0x6a8fee0e33cb65a7e8d21badca62e87639ef74b3": {
        "decimals": 18,
        "symbol": "PDX",
        "token_name": "PDXCoin",
    },
    "0x2e8f4bdbe3d47d7d7de490437aea9915d930f1a3": {
        "decimals": 18,
        "symbol": "aUSDP",
        "token_name": "Aave interest bearing USDP",
    },
    "0xc53342fd7575f572b0ff4569e31941a5b821ac76": {
        "decimals": 18,
        "symbol": "ETHV",
        "token_name": "ETH Volatility Index",
    },
    "0x73c9275c3a2dd84b5741fd59aebf102c91eb033f": {
        "decimals": 18,
        "symbol": "BTRS",
        "token_name": "BitBall Treasure",
    },
    "0x811beed0119b4afce20d2583eb608c6f7af1954f": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x471a3c3d1fe3518ac12670763711753f2c33c8ca": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x7a1080fb2ee96759f597b55bc3616b7c6516743d": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x2e2364966267b5d7d2ce6cd9a9b5bd19d9c7c6a9": {
        "decimals": 18,
        "symbol": "VOICE",
        "token_name": "Voice Token",
    },
    "0x0642026e7f0b6ccac5925b4e7fa61384250e1701": {
        "decimals": 18,
        "symbol": "H2O",
        "token_name": "H2O",
    },
    "0xa2085073878152ac3090ea13d1e41bd69e60dc99": {
        "decimals": 18,
        "symbol": "ELG",
        "token_name": "EscoinToken",
    },
    "0xa978d807614c3bfb0f90bc282019b2898c617880": {
        "decimals": 8,
        "symbol": "anStETH",
        "token_name": "Anchor stETH",
    },
    "0xf6d2224916ddfbbab6e6bd0d1b7034f4ae0cab18": {
        "decimals": 18,
        "symbol": "aEthUNI",
        "token_name": "Aave Ethereum UNI",
    },
    "0x96c645d3d3706f793ef52c19bbace441900ed47d": {
        "decimals": 0,
        "symbol": "MPS",
        "token_name": "MtPelerin Shares",
    },
    "0x3d5f3b3bb9b23c5bf1154091009d8465ae4d85ab": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xc7b4c17861357b8abb91f25581e7263e08dcb59c": {
        "decimals": 18,
        "symbol": "aEthSNX",
        "token_name": "Aave Ethereum SNX",
    },
    "0xa0d69e286b938e21cbf7e51d71f6a4c8918f482f": {
        "decimals": 18,
        "symbol": "eUSD",
        "token_name": "Electronic Dollar",
    },
    "0x9c14bf7a0275a521835d2788ff3a2c1eee9eacb3": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x56c6aac504e32e97957a7af6c8398e74edbed0db": {
        "decimals": 6,
        "symbol": "vDebtUSDT",
        "token_name": "ParaSpace Variable Debt Token USDT",
    },
    "0x3802c218221390025bceabbad5d8c59f40eb74b8": {
        "decimals": 18,
        "symbol": "GETH",
        "token_name": "Guarded Ether",
    },
    "0x0550e82ab7f5c2e2b0e89a89e601ed68ce51b375": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xf17a3fe536f8f7847f1385ec1bc967b2ca9cae8d": {
        "decimals": 18,
        "symbol": "AMKT",
        "token_name": "Alongside Crypto Market Index",
    },
    "0x7945b0a6674b175695e5d1d08ae1e6f13744abb0": {
        "decimals": 18,
        "symbol": "BaoUSD",
        "token_name": "BaoUSD",
    },
    "0x2336c10a1d3100343fa9911a2c57b77c333599a3": {
        "decimals": 18,
        "symbol": "tMATIC",
        "token_name": "tender MATIC",
    },
    "0xffc97d72e13e01096502cb8eb52dee56f74dad7b": {
        "decimals": 18,
        "symbol": "aAAVE",
        "token_name": "Aave interest bearing AAVE",
    },
    "0x32e2b981d163c36ef4964b9c205b1336684fdeaf": {
        "decimals": 18,
        "symbol": "vDebtAPE",
        "token_name": "ParaSpace Variable Debt Token APE",
    },
    "0xed40834a13129509a89be39a9be9c0e96a0ddd71": {
        "decimals": 18,
        "symbol": "WARP",
        "token_name": "Warp Token",
    },
    "0x6139240a5907e4ce74673257c320ea366c521aea": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x7b6abc75cf6c8abe52e047e11240d1aa9ed784e3": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0x9865a84c47c5a6c69ad7bae7e59d5a5a08679409": {
        "decimals": 18,
        "symbol": "UNI-V2",
        "token_name": "Uniswap V2",
    },
    "0xeec2be5c91ae7f8a338e1e5f3b5de49d07afdc81": {
        "decimals": 18,
        "symbol": "DPX",
        "token_name": "Dopex Governance Token",
    },
    "0x4228f8895c7dda20227f6a5c6751b8ebf19a6ba8": {
        "decimals": 18,
        "symbol": "variableDebtEthLINK",
        "token_name": "Aave Ethereum Variable Debt LINK",
    },
    "0xd5a14081a34d256711b02bbef17e567da48e80b5": {
        "decimals": 9,
        "symbol": "wUSDR",
        "token_name": "Wrapped USDR",
    },
    "0xe5feeac09d36b18b3fa757e5cf3f8da6b8e27f4c": {
        "decimals": 18,
        "symbol": "NFTI",
        "token_name": "NFT INDEX",
    },
    "0x6d765cbe5bc922694afe112c140b8878b9fb0390": {
        "decimals": 18,
        "symbol": "yvSUSHI",
        "token_name": "SUSHI yVault",
    },
    "0xc96113eed8cab59cd8a66813bcb0ceb29f06d2e4": {
        "decimals": 18,
        "symbol": "variableDebtEthwstETH",
        "token_name": "Aave Ethereum Variable Debt wstETH",
    },
}
