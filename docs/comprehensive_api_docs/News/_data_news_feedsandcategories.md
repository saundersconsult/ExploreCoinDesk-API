# News Feeds and Categories

**Endpoint**: `/data/news/feedsandcategories`  
**Category**: News  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/News/newsFeedAndCategoriesEndpoint](https://developers.coindesk.com/documentation/legacy/News/newsFeedAndCategoriesEndpoint)

## Description

Get combined feeds and categories list

## Parameters

No parameters required.

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/news/feedsandcategories"
```

### Python

```python
import requests

# Endpoint: /data/news/feedsandcategories
url = "https://min-api.cryptocompare.com/data/news/feedsandcategories"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/news/feedsandcategories
const url = "https://min-api.cryptocompare.com/data/news/feedsandcategories";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Success",
  "Message": "",
  "HasWarning": false,
  "Type": 100,
  "RateLimit": {},
  "Data": {
    "Categories": [
      {
        "categoryName": "1INCH",
        "wordsAssociatedWithCategory": [
          "1INCH"
        ],
        "includedPhrases": [
          "1INCH NETWORK"
        ]
      },
      {
        "categoryName": "AAVE",
        "wordsAssociatedWithCategory": [
          "AAVE"
        ],
        "includedPhrases": [
          "AAVE PROTOCOL"
        ]
      },
      {
        "categoryName": "ADA",
        "wordsAssociatedWithCategory": [
          "ADA",
          "Cardano",
          "cardano"
        ]
      },
      {
        "categoryName": "ADMINISTRATIVE EVENTS",
        "wordsAssociatedWithCategory": [
          "contract-migration",
          "REBRAND",
          "REBASE",
          "RENAME",
          "Rebrand",
          "rebrand",
          "Rename",
          "rename"
        ],
        "excludedPhrases": [
          "STOCK TICKER"
        ],
        "includedPhrases": [
          "CHAIN MIGRATION",
          "CHAIN MIGRATED",
          "CONTRACT ADDRESS UPDATE",
          "CONTRACT MIGRATION",
          "CONTRACT MIGRATED",
          "DESTINATION CHAIN",
          "NEW CONTRACT ADDRESS",
          "NETWORK CONTROL CHANGE",
          "GOVERNANCE CHANGE",
          "REVERSE TOKEN SPLIT",
          "TOKEN CONSOLIDATION",
          "TOKEN REVERSE SPLIT",
          "TICKER CHANGE",
          "TICKER CHANGED",
          "SYMBOL CHANGE",
          "SYMBOL CHANGED",
          "TICKER UPDATE",
          "SYMBOL UPDATE",
          "TOKEN MERGE",
          "TOKEN MERGED",
          "TOKEN SPLIT",
          "TOKEN SPLITTED",
          "TOKEN DIVIDED",
          "TOKEN SPLIT-UP",
          "TOKEN SPLIT UP"
        ]
      },
      {
        "categoryName": "AEVO",
        "wordsAssociatedWithCategory": [
          "AEVO"
        ],
        "includedPhrases": [
          "AEVO TOKEN"
        ]
      },
      {
        "categoryName": "AGX",
        "wordsAssociatedWithCategory": [
          "AGX",
          "SingularityNET",
          "singularityNET"
        ]
      },
      {
        "categoryName": "AIOZ",
        "wordsAssociatedWithCategory": [
          "AIOZ"
        ],
        "includedPhrases": [
          "AIOZ NETWORK"
        ]
      },
      {
        "categoryName": "AIRDROP",
        "wordsAssociatedWithCategory": [
          "airdrop",
          "Airdrop"
        ],
        "includedPhrases": [
          "TOKEN AIRDROP",
          "COIN AIRDROP",
          "FREE TOKEN DISTRIBUTION",
          "TOKEN GIVEAWAY",
          "COIN GIVEAWAY"
        ]
      },
      {
        "categoryName": "AKT",
        "wordsAssociatedWithCategory": [
          "AKT"
        ],
        "includedPhrases": [
          "AKASH NETWORK"
        ]
      },
      {
        "categoryName": "ALGO",
        "wordsAssociatedWithCategory": [
          "ALGO",
          "Algorand"
        ]
      },
      {
        "categoryName": "ALTCOIN",
        "wordsAssociatedWithCategory": [
          "Altcoin",
          "Altcoins",
          "altcoin",
          "altcoins"
        ]
      },
      {
        "categoryName": "APE",
        "wordsAssociatedWithCategory": [
          "APE",
          "Apecoin"
        ]
      },
      {
        "categoryName": "APT",
        "wordsAssociatedWithCategory": [
          "APT",
          "Aptos",
          "aptos"
        ]
      },
      {
        "categoryName": "AR",
        "wordsAssociatedWithCategory": [
          "AR",
          "Arweave",
          "arweave"
        ]
      },
      {
        "categoryName": "ARB",
        "wordsAssociatedWithCategory": [
          "ARB",
          "Arbitrum",
          "arbitrum"
        ]
      },
      {
        "categoryName": "ARKM",
        "wordsAssociatedWithCategory": [
          "ARKM",
          "Arkham",
          "arkham"
        ],
        "includedPhrases": [
          "ARKHAM NETWORK"
        ]
      },
      {
        "categoryName": "ASIA",
        "wordsAssociatedWithCategory": [
          "Asia",
          "China",
          "Korea",
          "Japan",
          "Hong",
          "Singapore",
          "Taiwan"
        ]
      },
      {
        "categoryName": "ASTR",
        "wordsAssociatedWithCategory": [
          "ASTR"
        ],
        "includedPhrases": [
          "ASTAR NETWORK"
        ]
      },
      {
        "categoryName": "ATOM",
        "wordsAssociatedWithCategory": [
          "ATOM"
        ],
        "excludedPhrases": [
          "ATOMIC COIN"
        ],
        "includedPhrases": [
          "COSMOS SDK"
        ]
      },
      {
        "categoryName": "AVAX",
        "wordsAssociatedWithCategory": [
          "AVAX"
        ],
        "includedPhrases": [
          "AVALANCHE FOUNDATION"
        ]
      },
      {
        "categoryName": "AXL",
        "wordsAssociatedWithCategory": [
          "AXL"
        ],
        "includedPhrases": [
          "AXELAR NETWORK"
        ]
      },
      {
        "categoryName": "AXS",
        "wordsAssociatedWithCategory": [
          "AXS"
        ],
        "includedPhrases": [
          "AXIE INFINITY"
        ]
      },
      {
        "categoryName": "BAL",
        "wordsAssociatedWithCategory": [
          "BAL",
          "Balancer"
        ],
        "includedPhrases": [
          "BALANCER PROTOCOL"
        ]
      },
      {
        "categoryName": "BAT",
        "wordsAssociatedWithCategory": [
          "BAT"
        ],
        "includedPhrases": [
          "BASIC ATTENTION TOKEN"
        ]
      },
      {
        "categoryName": "BCH",
        "wordsAssociatedWithCategory": [
          "BCH",
          "Bitcoincash",
          "bitcoincash"
        ],
        "includedPhrases": [
          "BITCOIN CASH"
        ]
      },
      {
        "categoryName": "BEAM",
        "wordsAssociatedWithCategory": [
          "BEAM"
        ],
        "includedPhrases": [
          "BEAM NETWORK"
        ]
      },
      {
        "categoryName": "BGB",
        "wordsAssociatedWithCategory": [
          "BGB"
        ],
        "includedPhrases": [
          "BITGET TOKEN"
        ]
      },
      {
        "categoryName": "BITTENSOR",
        "wordsAssociatedWithCategory": [
          "TAO",
          "Bittensor",
          "bittensor"
        ]
      },
      {
        "categoryName": "BLOCKCHAIN",
        "wordsAssociatedWithCategory": [
          "Blockchain",
          "blockchain",
          "Protocol",
          "protocol",
          "Scaling",
          "scaling"
        ]
      },
      {
        "categoryName": "BLUR",
        "wordsAssociatedWithCategory": [
          "BLUR"
        ],
        "includedPhrases": [
          "BLUR TOKEN"
        ]
      },
      {
        "categoryName": "BNB",
        "wordsAssociatedWithCategory": [
          "BNB",
          "Binance",
          "binance"
        ]
      },
      {
        "categoryName": "BNX",
        "wordsAssociatedWithCategory": [
          "BNX",
          "Binaryx",
          "bynarix"
        ]
      },
      {
        "categoryName": "BOME",
        "wordsAssociatedWithCategory": [
          "BOME"
        ],
        "includedPhrases": [
          "BOME TOKEN"
        ]
      },
      {
        "categoryName": "BONK",
        "wordsAssociatedWithCategory": [
          "BONK"
        ],
        "includedPhrases": [
          "BONK TOKEN"
        ]
      },
      {
        "categoryName": "BRETT",
        "wordsAssociatedWithCategory": [
          "BRETT"
        ],
        "includedPhrases": [
          "BRETT COIN"
        ]
      },
      {
        "categoryName": "BSV",
        "wordsAssociatedWithCategory": [
          "BSV"
        ],
        "includedPhrases": [
          "BITCON SV"
        ]
      },
      {
        "categoryName": "BTC",
        "wordsAssociatedWithCategory": [
          "BTC",
          "Bitcoin",
          "bitcoin"
        ],
        "excludedPhrases": [
          "BITCOIN CASH"
        ],
        "includedPhrases": [
          "SATOSHI NAKAMOTO"
        ]
      },
      {
        "categoryName": "BTG",
        "wordsAssociatedWithCategory": [
          "BTG"
        ],
        "includedPhrases": [
          "BITCOIN GOLD"
        ]
      },
      {
        "categoryName": "BTT",
        "wordsAssociatedWithCategory": [
          "BTT"
        ],
        "includedPhrases": [
          "BITTORRENT TOKEN"
        ]
      },
      {
        "categoryName": "BUSINESS",
        "wordsAssociatedWithCategory": [
          "Business",
          "business",
          "Investor",
          "investor",
          "investors",
          "Investors",
          "revenue",
          "Revenue",
          "Profit",
          "profit",
          "enterprise",
          "Enterprise",
          "Commerce",
          "commerce",
          "stock",
          "Stock"
        ]
      },
      {
        "categoryName": "CAKE",
        "wordsAssociatedWithCategory": [
          "CAKE",
          "Pancakeswap",
          "pancakeswap"
        ]
      },
      {
        "categoryName": "CFX",
        "wordsAssociatedWithCategory": [
          "CFX",
          "Conflux",
          "conflux"
        ],
        "includedPhrases": [
          "CONFLUX FOUNDATION"
        ]
      },
      {
        "categoryName": "CHZ",
        "wordsAssociatedWithCategory": [
          "CHZ"
        ],
        "includedPhrases": [
          "CHILIZ CHAIN"
        ]
      },
      {
        "categoryName": "CKB",
        "wordsAssociatedWithCategory": [
          "CKB"
        ],
        "includedPhrases": [
          "NERVOS NETWORK"
        ]
      },
      {
        "categoryName": "COMMODITY",
        "wordsAssociatedWithCategory": [
          "Oil",
          "oil",
          "oil-backed",
          "Oil-backed",
          "Commodity",
          "Commodities"
        ]
      },
      {
        "categoryName": "COMP",
        "wordsAssociatedWithCategory": [
          "COMP",
          "cETH",
          "cTokens"
        ],
        "includedPhrases": [
          "COMPOUND PROTOCOL"
        ]
      },
      {
        "categoryName": "CORE",
        "wordsAssociatedWithCategory": [
          "CORE"
        ],
        "includedPhrases": [
          "CORE DAO"
        ]
      },
      {
        "categoryName": "CRO",
        "wordsAssociatedWithCategory": [
          "CRO",
          "Cronos",
          "cronos"
        ]
      },
      {
        "categoryName": "CRV",
        "wordsAssociatedWithCategory": [
          "CRV"
        ],
        "includedPhrases": [
          "CURVE DAO"
        ]
      },
      {
        "categoryName": "CRYPTOCURRENCY",
        "wordsAssociatedWithCategory": [
          "crypto",
          "cryptocurrency",
          "cryptocurrencies",
          "Aave",
          "AAVE",
          "ADA",
          "ALGO",
          "Algorand",
          "APT",
          "Aptos",
          "ARB",
          "Arbitrum",
          "Avalanche",
          "AVAX",
          "BCH",
          "BGB",
          "Binance",
          "BingX",
          "Bitcoin",
          "bitcoin",
          "Bitfinex",
          "Bitget",
          "Bithumb",
          "BitMart",
          "Bitstamp",
          "Bittensor",
          "BNB",
          "BONK",
          "BTC",
          "Bybit",
          "Cardano",
          "Chainlink",
          "Coinbase",
          "CRO",
          "Cronos",
          "Curve",
          "Dai",
          "DAI",
          "DOGE",
          "Dogecoin",
          "DOT",
          "ENA",
          "ETC",
          "ETH",
          "Ethena",
          "Ethereum",
          "ethereum",
          "Gate",
          "HBAR",
          "Hedera",
          "HTX",
          "HYPE",
          "Hyperliquid",
          "ICP",
          "KAS",
          "Kaspa",
          "Kraken",
          "KuCoin",
          "LBank",
          "LEO",
          "LINK",
          "Litecoin",
          "LTC",
          "Mantle",
          "MEXC",
          "Monero",
          "NEAR",
          "OKB",
          "OKX",
          "Ondo",
          "ONDO",
          "PancakeSwap",
          "PENGU",
          "PEPE",
          "Pepe",
          "PI",
          "POL",
          "Polkadot",
          "Polygon",
          "Raydium",
          "SHIB",
          "SOL",
          "Solana",
          "Stellar",
          "Sui",
          "SUI",
          "TAO",
          "Tether",
          "TON",
          "Toncoin",
          "TRON",
          "TRX",
          "UNI",
          "Uniswap",
          "Upbit",
          "USD1",
          "USDC",
          "USDE",
          "USDS",
          "USDT",
          "VeChain",
          "WBT",
          "XLM",
          "XMR",
          "XRP",
          "Ripple",
          "Crypto.com",
          "WhiteBIT",
          "cryptocompare.com",
          "coindesk.com",
          "coinedition.com",
          "bitcoinist.com",
          "bitcoin.com",
          "cointelegraph.com",
          "newsbtc.com",
          "trustnodes.com",
          "nulltx.com",
          "cryptopotato.com",
          "blokt.com",
          "ambcrypto.com",
          "cryptonewsz.com",
          "diariobitcoin.com",
          "cryptopolitan.com",
          "decrypt.co",
          "cryptocoin.news",
          "zycrypto.com",
          "cryptonews.com",
          "blockworks.co",
          "thecoinrise.com",
          "finbold.com",
          "u.today",
          "thecryptobasic.com",
          "bitdegree.org",
          "timestabloid.com",
          "chainwire.org",
          "invezz.com/cryptocurrency/",
          "cryptodaily.co.uk",
          "coinotag.com",
          "cointurk.com",
          "cointurk.news",
          "coinpaprika.com",
          "bitcoinsistemi.com",
          "btcpulse.com",
          "coinpaper.com",
          "cryptointelligence.co.uk",
          "blog.kraken.com",
          "blog.bitfinex.com",
          "blog.huobi.com",
          "bloomberg.com/crypto",
          "bitzo.com"
        ],
        "excludedPhrases": [
          "CRYPTO QUOTE PUZZLE",
          "CRYPTOGRAM PUZZLE",
          "CRYPTOGRAPHY COMPETITION",
          "ENCRYPTION TECHNOLOGY",
          "CRYPTOGRAPHY CONFERENCE",
          "CRYPTOGRAPHY METHOD"
        ],
        "includedPhrases": [
          "DIGITAL ASSET",
          "DIGITAL ASSETS",
          "TOKEN SALE",
          "TOKEN LAUNCH",
          "TOKEN LISTING",
          "INITIAL COIN OFFERING",
          "INITIAL DEX OFFERING",
          "SECURITY TOKEN OFFERING",
          "DECENTRALIZED EXCHANGE",
          "DECENTRALIZED FINANCE",
          "NON-FUNGIBLE TOKEN",
          "METAVERSE PLATFORM",
          "METAVERSE PROJECT",
          "NEAR PROTOCOL",
          "CONVEX FINANCE",
          "YEARN FINANCE",
          "KYBER NETWORK",
          "PUDGY PENGUINS",
          "WORLD LIBERTY FINANCIAL",
          "SHIBA INU",
          "PI TOKEN",
          "ETHENA USDE"
        ]
      },
      {
        "categoryName": "DAI",
        "wordsAssociatedWithCategory": [
          "DAI"
        ]
      },
      {
        "categoryName": "DASH",
        "wordsAssociatedWithCategory": [
          "DASH",
          "Digitalcash",
          "digitalcash"
        ]
      },
      {
        "categoryName": "DIGITAL ASSET TREASURY",
        "wordsAssociatedWithCategory": [
          "treasury",
          "Treasury",
          "treasuries",
          "Treasuries"
        ],
        "excludedPhrases": [
          "US TREASURY",
          "TREASURY YIELDS",
          "TREASURY CURVE",
          "TREASURY FUTURES"
        ]
      },
      {
        "categoryName": "DOGE",
        "wordsAssociatedWithCategory": [
          "DOGE",
          "Dogecoin",
          "dogecoin"
        ]
      },
      {
        "categoryName": "DOT",
        "wordsAssociatedWithCategory": [
          "DOT",
          "Polkadot",
          "polkadot"
        ]
      },
      {
        "categoryName": "DYDX",
        "wordsAssociatedWithCategory": [
          "DYDX"
        ],
        "includedPhrases": [
          "DYDX EXCHANGE"
        ]
      },
      {
        "categoryName": "EGLD",
        "wordsAssociatedWithCategory": [
          "EGLD",
          "MultiversX",
          "multiversX"
        ]
      },
      {
        "categoryName": "ENA",
        "wordsAssociatedWithCategory": [
          "ENA"
        ],
        "includedPhrases": [
          "ETHENA LABS"
        ]
      },
      {
        "categoryName": "ENJ",
        "wordsAssociatedWithCategory": [
          "ENJ",
          "Enjin",
          "enjin"
        ]
      },
      {
        "categoryName": "ENS",
        "wordsAssociatedWithCategory": [
          "ENS"
        ],
        "includedPhrases": [
          "ETHEREUM NAME SERVICE"
        ]
      },
      {
        "categoryName": "ETC",
        "wordsAssociatedWithCategory": [
          "ETC"
        ],
        "includedPhrases": [
          "ETHEREUM CLASSIC"
        ]
      },
      {
        "categoryName": "ETH",
        "wordsAssociatedWithCategory": [
          "ETH",
          "Ethereum",
          "ethereum",
          "Vitalik",
          "vitalik"
        ],
        "excludedPhrases": [
          "ETHEREUM CLASSIC"
        ]
      },
      {
        "categoryName": "ETHFI",
        "wordsAssociatedWithCategory": [
          "ETHFI"
        ],
        "includedPhrases": [
          "ETHERFI PROTOCOL"
        ]
      },
      {
        "categoryName": "EXCHANGE",
        "wordsAssociatedWithCategory": [
          "Exchange",
          "exchange",
          "bitfinex",
          "poloniex",
          "binance",
          "kraken",
          "coinbase",
          "bybit",
          "upbit",
          "gate.io",
          "huobi",
          "kucoin",
          "bitget",
          "crypto.com",
          "Bitfinex",
          "Poloniex",
          "Binance",
          "Kraken",
          "Coinbase",
          "Bybit",
          "Upbit",
          "Gate.io",
          "Huobi",
          "Kucoin",
          "Bitget",
          "Crypto.com"
        ],
        "includedPhrases": [
          "GEMINI EXCHANGE",
          "GEMINI.COM"
        ]
      },
      {
        "categoryName": "FDUSD",
        "wordsAssociatedWithCategory": [
          "FDUSD"
        ]
      },
      {
        "categoryName": "FET",
        "wordsAssociatedWithCategory": [
          "FET"
        ],
        "includedPhrases": [
          "FETCH.AI"
        ]
      },
      {
        "categoryName": "FIAT",
        "wordsAssociatedWithCategory": [
          "Fiat",
          "fiat",
          "Reserve",
          "reserve",
          "Gold",
          "gold",
          "Gold-backed",
          "gold-backed",
          "bank",
          "Bank",
          "Dollar",
          "Euro",
          "Yen",
          "Pound"
        ]
      },
      {
        "categoryName": "FIL",
        "wordsAssociatedWithCategory": [
          "FIL",
          "Filecoin",
          "filecoin"
        ]
      },
      {
        "categoryName": "FLOKI",
        "wordsAssociatedWithCategory": [
          "FLOKI"
        ],
        "includedPhrases": [
          "FLOKI COIN"
        ]
      },
      {
        "categoryName": "FLOW",
        "wordsAssociatedWithCategory": [
          "FLOW"
        ],
        "includedPhrases": [
          "FLOW BLOCKCHAIN"
        ]
      },
      {
        "categoryName": "FLR",
        "wordsAssociatedWithCategory": [
          "FLR"
        ],
        "includedPhrases": [
          "FLARE NETWORK"
        ]
      },
      {
        "categoryName": "FORKS",
        "wordsAssociatedWithCategory": [
          "softfork",
          "Softfork",
          "hardfork",
          "Hardfork"
        ],
        "includedPhrases": [
          "SOFT FORK",
          "PROTOCOL UPGRADE",
          "BACKWARD-COMPATIBLE UPGRADE",
          "HARD FORK",
          "CHAIN SPLIT"
        ]
      },
      {
        "categoryName": "FTM",
        "wordsAssociatedWithCategory": [
          "FTM"
        ],
        "includedPhrases": [
          "FANTOM FOUNDATION"
        ]
      },
      {
        "categoryName": "FTT",
        "wordsAssociatedWithCategory": [
          "FTT"
        ],
        "includedPhrases": [
          "FTX TOKEN"
        ]
      },
      {
        "categoryName": "GALA",
        "wordsAssociatedWithCategory": [
          "GALA"
        ],
        "includedPhrases": [
          "GALA GAMES"
        ]
      },
      {
        "categoryName": "GMO",
        "wordsAssociatedWithCategory": [
          "GMO",
          "Gnosisdao",
          "gnosisdao",
          "gnosisDAO",
          "GnosisDAO"
        ]
      },
      {
        "categoryName": "GRT",
        "wordsAssociatedWithCategory": [
          "GRT"
        ],
        "includedPhrases": [
          "GRAPH FOUNDATION"
        ]
      },
      {
        "categoryName": "GT",
        "wordsAssociatedWithCategory": [
          "GT"
        ],
        "includedPhrases": [
          "GATE TOKEN"
        ]
      },
      {
        "categoryName": "HBAR",
        "wordsAssociatedWithCategory": [
          "HBAR"
        ],
        "includedPhrases": [
          "HEDERA COUNCIL"
        ]
      },
      {
        "categoryName": "HNT",
        "wordsAssociatedWithCategory": [
          "HNT"
        ],
        "includedPhrases": [
          "HELIUM FOUNDATION"
        ]
      },
      {
        "categoryName": "ICP",
        "wordsAssociatedWithCategory": [
          "ICP"
        ],
        "includedPhrases": [
          "INTERNET COMPUTER PROTOCOL"
        ]
      },
      {
        "categoryName": "IMX",
        "wordsAssociatedWithCategory": [
          "IMX",
          "ImmutableX",
          "immutableX"
        ]
      },
      {
        "categoryName": "INJ",
        "wordsAssociatedWithCategory": [
          "INJ"
        ],
        "includedPhrases": [
          "INJECTIVE PROTOCOL"
        ]
      },
      {
        "categoryName": "IOTA",
        "wordsAssociatedWithCategory": [
          "IOTA"
        ],
        "includedPhrases": [
          "IOTA FOUNDATION"
        ]
      },
      {
        "categoryName": "IOTX",
        "wordsAssociatedWithCategory": [
          "IOTX"
        ],
        "includedPhrases": [
          "IOTEX PROTOCOL"
        ]
      },
      {
        "categoryName": "JASMY",
        "wordsAssociatedWithCategory": [
          "JASMY"
        ],
        "includedPhrases": [
          "JASMY COIN"
        ]
      },
      {
        "categoryName": "JUP",
        "wordsAssociatedWithCategory": [
          "JUP"
        ],
        "includedPhrases": [
          "JUPITER AGGREGATOR"
        ]
      },
      {
        "categoryName": "KASPA",
        "wordsAssociatedWithCategory": [
          "KASPA"
        ],
        "includedPhrases": [
          "KASPA PROTOCOL"
        ]
      },
      {
        "categoryName": "KAVA",
        "wordsAssociatedWithCategory": [
          "KAVA"
        ],
        "includedPhrases": [
          "KAVA LEND"
        ]
      },
      {
        "categoryName": "KLAY",
        "wordsAssociatedWithCategory": [
          "KLAY"
        ],
        "includedPhrases": [
          "KLAYTN FOUNDATION"
        ]
      },
      {
        "categoryName": "KNC",
        "wordsAssociatedWithCategory": [
          "KNC"
        ],
        "includedPhrases": [
          "KYBER NETWORK",
          "KYBERNETWORK"
        ]
      },
      {
        "categoryName": "KSC",
        "wordsAssociatedWithCategory": [
          "KSC"
        ],
        "includedPhrases": [
          "KUCOIN EXCHANGE"
        ]
      },
      {
        "categoryName": "LDO",
        "wordsAssociatedWithCategory": [
          "LDO"
        ],
        "includedPhrases": [
          "LIDO DAO"
        ]
      },
      {
        "categoryName": "LEO",
        "wordsAssociatedWithCategory": [
          "LEO"
        ],
        "includedPhrases": [
          "UNUS SED LEO"
        ]
      },
      {
        "categoryName": "LINK",
        "wordsAssociatedWithCategory": [
          "LINK",
          "Chainlink",
          "chainlink"
        ]
      },
      {
        "categoryName": "LPT",
        "wordsAssociatedWithCategory": [
          "LPT"
        ],
        "includedPhrases": [
          "LIVEPEER NETWORK"
        ]
      },
      {
        "categoryName": "LRC",
        "wordsAssociatedWithCategory": [
          "LRC",
          "Loopring",
          "loopring"
        ]
      },
      {
        "categoryName": "LTC",
        "wordsAssociatedWithCategory": [
          "LTC",
          "Litecoin",
          "litecoin"
        ]
      },
      {
        "categoryName": "LUNA",
        "wordsAssociatedWithCategory": [
          "LUNA",
          "TERRA",
          "UST"
        ],
        "excludedPhrases": [
          "LUNC",
          "LUNA CLASSIC"
        ],
        "includedPhrases": [
          "TERRAFORM LABS"
        ]
      },
      {
        "categoryName": "LUNC",
        "wordsAssociatedWithCategory": [
          "LUNC"
        ],
        "includedPhrases": [
          "TERRA CLASSIC",
          "LUNA CLASSIC"
        ]
      },
      {
        "categoryName": "MACROECONOMICS",
        "wordsAssociatedWithCategory": [
          "inflation",
          "Inflation",
          "deflation",
          "Deflation",
          "stagflation",
          "Stagflation",
          "recession",
          "Recession",
          "slowdown",
          "CPI",
          "PPI",
          "PCE",
          "GDP",
          "PMI",
          "jobless",
          "Jobless",
          "unemployment",
          "Unemployment",
          "treasury",
          "Treasury",
          "DXY",
          "QE",
          "QT",
          "taper",
          "stimulus",
          "Stimulus",
          "deficit",
          "Deficit",
          "downgrade",
          "tariff",
          "Tariff",
          "tariffs",
          "Tariffs",
          "sanction",
          "sanctions",
          "WTI",
          "FED",
          "FOMC",
          "ECB",
          "BOE",
          "BOJ",
          "PBOC"
        ],
        "excludedPhrases": [
          "DOLLAR TREE",
          "DOLLAR GENERAL",
          "DOLLAR STORE",
          "FEDERAL EXPRESS",
          "PIXELS PER INCH",
          "PPI DISPLAY",
          "PPI RESOLUTION",
          "CPU CPI",
          "QT FRAMEWORK",
          "QT CREATOR",
          "QT GUI"
        ],
        "includedPhrases": [
          "CONSUMER PRICE INDEX",
          "PRODUCER PRICE INDEX",
          "CORE PCE",
          "NON-FARM PAYROLLS",
          "JOBS REPORT",
          "INITIAL JOBLESS CLAIMS",
          "INTEREST-RATE HIKE",
          "RATE CUT",
          "YIELD-CURVE INVERSION",
          "QUANTITATIVE EASING",
          "QUANTITATIVE TIGHTENING",
          "FISCAL STIMULUS",
          "GOVERNMENT SHUTDOWN",
          "DEBT-CEILING STANDOFF",
          "CREDIT-RATING DOWNGRADE",
          "TRADE TARIFFS",
          "TRADE SANCTIONS",
          "GLOBAL SUPPLY-CHAIN",
          "MIDDLE EAST CONFLICT",
          "UKRAINE WAR",
          "OIL PRODUCTION CUT",
          "OPEC+ MEETING",
          "DOLLAR INDEX STRENGTH",
          "FX INTERVENTION",
          "MONETARY POLICY MEETING",
          "CENTRAL-BANK DECISION",
          "INFLATION EXPECTATIONS",
          "CORE INFLATION",
          "HEADLINE INFLATION",
          "IMPORT/EXPORT DATA",
          "BALANCE OF TRADE",
          "MANUFACTURING PMI",
          "SERVICES PMI",
          "FEDERAL RESERVE",
          "CENTRAL BANK",
          "TRADE WAR"
        ]
      },
      {
        "categoryName": "MANA",
        "wordsAssociatedWithCategory": [
          "MANA",
          "Decentraland",
          "decentraland"
        ],
        "excludedPhrases": [
          "GENESIS MANA"
        ]
      },
      {
        "categoryName": "MARKET",
        "wordsAssociatedWithCategory": [
          "index",
          "Index",
          "Prices",
          "prices",
          "market",
          "Market",
          "markets",
          "Markets",
          "analysis",
          "Analysis"
        ]
      },
      {
        "categoryName": "MATIC",
        "wordsAssociatedWithCategory": [
          "MATIC",
          "Polygon"
        ]
      },
      {
        "categoryName": "MEME",
        "wordsAssociatedWithCategory": [
          "MEME",
          "Memeland"
        ]
      },
      {
        "categoryName": "MIGRATION",
        "wordsAssociatedWithCategory": [
          "contract-migration"
        ],
        "includedPhrases": [
          "CHAIN MIGRATION",
          "CHAIN MIGRATED",
          "CONTRACT ADDRESS UPDATE",
          "CONTRACT MIGRATION",
          "CONTRACT MIGRATED",
          "DESTINATION CHAIN",
          "NEW CONTRACT ADDRESS"
        ]
      },
      {
        "categoryName": "MINA",
        "wordsAssociatedWithCategory": [
          "MINA"
        ],
        "includedPhrases": [
          "MINA PROTOCOL"
        ]
      },
      {
        "categoryName": "MINING",
        "wordsAssociatedWithCategory": [
          "Mining",
          "mining",
          "Hashrate",
          "hashrate",
          "Hashing",
          "hashing",
          "Pools",
          "pools",
          "Reward",
          "reward"
        ]
      },
      {
        "categoryName": "MKR",
        "wordsAssociatedWithCategory": [
          "MKR",
          "MakerDAO",
          "makerDAO"
        ]
      },
      {
        "categoryName": "MNT",
        "wordsAssociatedWithCategory": [
          "MNT"
        ]
      },
      {
        "categoryName": "MOG",
        "wordsAssociatedWithCategory": [
          "MOG"
        ],
        "includedPhrases": [
          "MOG COIN"
        ]
      },
      {
        "categoryName": "MX",
        "wordsAssociatedWithCategory": [
          "MX"
        ],
        "includedPhrases": [
          "MX TOKEN"
        ]
      },
      {
        "categoryName": "NEAR",
        "wordsAssociatedWithCategory": [
          "NEAR"
        ],
        "includedPhrases": [
          "NEAR PROTOCOL"
        ]
      },
      {
        "categoryName": "NEO",
        "wordsAssociatedWithCategory": [
          "NEO"
        ],
        "includedPhrases": [
          "NEO BLOCKCHAIN"
        ]
      },
      {
        "categoryName": "NEXO",
        "wordsAssociatedWithCategory": [
          "NEXO"
        ],
        "includedPhrases": [
          "NEXO EXCHANGE"
        ]
      },
      {
        "categoryName": "NOT",
        "wordsAssociatedWithCategory": [
          "NOTCOIN",
          "Notcoin",
          "notcoin"
        ]
      },
      {
        "categoryName": "OKB",
        "wordsAssociatedWithCategory": [
          "OKB"
        ]
      },
      {
        "categoryName": "OM",
        "wordsAssociatedWithCategory": [
          "OM"
        ],
        "includedPhrases": [
          "MANTRA FOUNDATION"
        ]
      },
      {
        "categoryName": "ONDO",
        "wordsAssociatedWithCategory": [
          "ONDO"
        ],
        "includedPhrases": [
          "ONDO FINANCE"
        ]
      },
      {
        "categoryName": "OP",
        "wordsAssociatedWithCategory": [
          "OP"
        ]
      },
      {
        "categoryName": "ORDI",
        "wordsAssociatedWithCategory": [
          "ORDI"
        ],
        "includedPhrases": [
          "ORDINALS PLATFORM"
        ]
      },
      {
        "categoryName": "OTHER"
      },
      {
        "categoryName": "PAXG",
        "wordsAssociatedWithCategory": [
          "PAXG"
        ],
        "includedPhrases": [
          "PAXOS GOLD"
        ]
      },
      {
        "categoryName": "PENDLE",
        "wordsAssociatedWithCategory": [
          "PENDLE"
        ],
        "includedPhrases": [
          "PENDLE FINANCE"
        ]
      },
      {
        "categoryName": "PEOPLE",
        "wordsAssociatedWithCategory": [
          "PEOPLE",
          "ConstitutionalDAO",
          "constitutionalDAO"
        ]
      },
      {
        "categoryName": "PEPE",
        "wordsAssociatedWithCategory": [
          "PEPE"
        ]
      },
      {
        "categoryName": "PYTH",
        "wordsAssociatedWithCategory": [
          "PYTH"
        ],
        "includedPhrases": [
          "PYTH NETWORK"
        ]
      },
      {
        "categoryName": "PYUSD",
        "wordsAssociatedWithCategory": [
          "PYUSD"
        ],
        "includedPhrases": [
          "PAYPAL USD"
        ]
      },
      {
        "categoryName": "QNT",
        "wordsAssociatedWithCategory": [
          "QNT"
        ],
        "includedPhrases": [
          "QUANT NETWORK"
        ]
      },
      {
        "categoryName": "RAI",
        "wordsAssociatedWithCategory": [
          "RAI"
        ],
        "includedPhrases": [
          "REFLEXER LABS"
        ]
      },
      {
        "categoryName": "RAY",
        "wordsAssociatedWithCategory": [
          "RAY",
          "Raydium",
          "raydium"
        ]
      },
      {
        "categoryName": "REGULATION",
        "wordsAssociatedWithCategory": [
          "Regulation",
          "regulation",
          "Legal",
          "legal",
          "Law",
          "law",
          "tax",
          "Tax",
          "Taxes",
          "taxes",
          "senate",
          "Senate",
          "Legislation",
          "legislation",
          "President",
          "president",
          "treasury",
          "Treasury",
          "SEC",
          "BOE"
        ]
      },
      {
        "categoryName": "REN",
        "wordsAssociatedWithCategory": [
          "REN",
          "RenVM",
          "renVM",
          "Renbridge",
          "renbridge"
        ]
      },
      {
        "categoryName": "RESEARCH",
        "wordsAssociatedWithCategory": [
          "research",
          "Research"
        ]
      },
      {
        "categoryName": "REVERSE TOKEN SPLIT",
        "wordsAssociatedWithCategory": [
          "reverse-split",
          "Reverse-split",
          "REVERSE-SPLIT"
        ],
        "excludedPhrases": [
          "FORWARD SPLIT",
          "STOCK SPLIT",
          "STANDARD SPLIT",
          "NORMAL SPLIT"
        ],
        "includedPhrases": [
          "REVERSE TOKEN SPLIT",
          "TOKEN CONSOLIDATION",
          "TOKEN REVERSE SPLIT",
          "REVERSE COIN SPLIT"
        ]
      },
      {
        "categoryName": "RNDR",
        "wordsAssociatedWithCategory": [
          "RNDR"
        ],
        "includedPhrases": [
          "RENDER FOUNDATION"
        ]
      },
      {
        "categoryName": "RON",
        "wordsAssociatedWithCategory": [
          "RON"
        ],
        "includedPhrases": [
          "RONIN BLOCKCHAIN"
        ]
      },
      {
        "categoryName": "ROSE",
        "wordsAssociatedWithCategory": [
          "ROSE"
        ],
        "includedPhrases": [
          "OASIS PROTOCOL"
        ]
      },
      {
        "categoryName": "RPL",
        "wordsAssociatedWithCategory": [
          "RPL"
        ],
        "includedPhrases": [
          "ROCKET POOL"
        ]
      },
      {
        "categoryName": "RUNE",
        "wordsAssociatedWithCategory": [
          "RUNE",
          "Thorchain",
          "thorchain"
        ]
      },
      {
        "categoryName": "SAFE",
        "wordsAssociatedWithCategory": [
          "SAFE"
        ],
        "includedPhrases": [
          "SAFE SMART ACCOUNTS"
        ]
      },
      {
        "categoryName": "SAND",
        "wordsAssociatedWithCategory": [
          "SAND"
        ],
        "includedPhrases": [
          "SANDBOX FOUNDATION"
        ]
      },
      {
        "categoryName": "SECURITY INCIDENTS",
        "wordsAssociatedWithCategory": [
          "hack",
          "Hack",
          "HACK",
          "hacked",
          "HACKED",
          "Hacked",
          "exploit",
          "EXPLOIT",
          "Exploit",
          "Vulnerability",
          "VULNERABILITY",
          "vulnerability",
          "rugpull",
          "RUGPULL",
          "Rugpull",
          "rug-pull"
        ],
        "excludedPhrases": [
          "LIFE HACK",
          "GROWTH HACK"
        ],
        "includedPhrases": [
          "PRIVATE KEY COMPROMISED",
          "EXIT SCAM",
          "FLASH LOAN ATTACK",
          "REENTRANCY ATTACK",
          "FUNDS STOLEN",
          "FUNDS DRAINED",
          "WALLET COMPROMISED",
          "SMART CONTRACT BREACH",
          "SECURITY BREACH"
        ]
      },
      {
        "categoryName": "SEI",
        "wordsAssociatedWithCategory": [
          "SEI"
        ],
        "includedPhrases": [
          "SEI NETWORK"
        ]
      },
      {
        "categoryName": "SHIB",
        "wordsAssociatedWithCategory": [
          "SHIB"
        ],
        "includedPhrases": [
          "SHIBA INU"
        ]
      },
      {
        "categoryName": "SNX",
        "wordsAssociatedWithCategory": [
          "SNX"
        ],
        "includedPhrases": [
          "SYNTHETIX ECOSYSTEM"
        ]
      },
      {
        "categoryName": "SOL",
        "wordsAssociatedWithCategory": [
          "SOL",
          "Solana",
          "solana"
        ]
      },
      {
        "categoryName": "SPONSORED",
        "wordsAssociatedWithCategory": [
          "Sponsored",
          "sponsored",
          "featured",
          "Featured"
        ],
        "includedPhrases": [
          "PRESS RELEASE",
          "PRESS RELEASES"
        ]
      },
      {
        "categoryName": "SSV",
        "wordsAssociatedWithCategory": [
          "SSV"
        ],
        "includedPhrases": [
          "SSV NETWORK"
        ]
      },
      {
        "categoryName": "STRK",
        "wordsAssociatedWithCategory": [
          "STRK"
        ],
        "includedPhrases": [
          "STARKNET FOUNDATION"
        ]
      },
      {
        "categoryName": "STX",
        "wordsAssociatedWithCategory": [
          "STX"
        ],
        "includedPhrases": [
          "STACKS FOUNDATION"
        ]
      },
      {
        "categoryName": "SUI",
        "wordsAssociatedWithCategory": [
          "SUI"
        ],
        "includedPhrases": [
          "SUI BLOCKCHAIN",
          "SUI FOUNDATION"
        ]
      },
      {
        "categoryName": "SUSHI",
        "wordsAssociatedWithCategory": [
          "SUSHI",
          "Sushiswap",
          "sushiswap"
        ]
      },
      {
        "categoryName": "TECHNOLOGY",
        "wordsAssociatedWithCategory": [
          "Software",
          "software",
          "technology",
          "Technology",
          "TECH"
        ]
      },
      {
        "categoryName": "TFUEL",
        "wordsAssociatedWithCategory": [
          "TFUEL"
        ],
        "includedPhrases": [
          "THETA FUEL"
        ]
      },
      {
        "categoryName": "THETA",
        "wordsAssociatedWithCategory": [
          "THETA"
        ],
        "includedPhrases": [
          "THETA NETWORK"
        ]
      },
      {
        "categoryName": "TIA",
        "wordsAssociatedWithCategory": [
          "TIA",
          "Celestia",
          "celestia"
        ]
      },
      {
        "categoryName": "TICKER CHANGE",
        "wordsAssociatedWithCategory": [
          "REBRAND",
          "rebrand",
          "Rebrand",
          "rename",
          "Rename",
          "RENAME"
        ],
        "excludedPhrases": [
          "STOCK TICKER"
        ],
        "includedPhrases": [
          "TICKER CHANGE",
          "TICKER CHANGED",
          "SYMBOL CHANGE",
          "SYMBOL CHANGED",
          "TICKER UPDATE",
          "SYMBOL UPDATE"
        ]
      },
      {
        "categoryName": "TOKEN LISTING AND DELISTING",
        "wordsAssociatedWithCategory": [
          "tokenlisting"
        ],
        "includedPhrases": [
          "TOKEN LISTING",
          "COIN LISTING",
          "NEW TOKEN LISTED",
          "NEW COIN LISTED",
          "TOKEN ADDED",
          "COIN ADDED",
          "TOKEN DELISTING",
          "TOKEN REMOVED",
          "TOKEN DELISTED"
        ]
      },
      {
        "categoryName": "TOKEN SALE",
        "wordsAssociatedWithCategory": [
          "ICO"
        ],
        "includedPhrases": [
          "INITIAL COIN OFFERING",
          "TOKEN SALE",
          "TOKEN OFFERING",
          "COIN OFFERING",
          "INITIAL TOKEN SALE"
        ]
      },
      {
        "categoryName": "TOKEN SPLIT",
        "wordsAssociatedWithCategory": [
          "REBASE",
          "Rebase",
          "rebase"
        ],
        "excludedPhrases": [
          "PROFIT SPLIT",
          "REVENUE SPLIT",
          "FEE SPLIT",
          "LIQUIDITY SPLIT",
          "AIRDROP SPLIT",
          "REWARD SPLIT",
          "DIVIDEND SPLIT"
        ],
        "includedPhrases": [
          "TOKEN SPLIT",
          "TOKEN SPLITTED",
          "TOKEN DIVIDED",
          "TOKEN SPLIT-UP",
          "TOKEN SPLIT UP"
        ]
      },
      {
        "categoryName": "TON",
        "wordsAssociatedWithCategory": [
          "TON"
        ]
      },
      {
        "categoryName": "TRADING",
        "wordsAssociatedWithCategory": [
          "Technical",
          "technical",
          "trading",
          "Trading",
          "Fundamentals",
          "fundamentals",
          "Price",
          "price",
          "Bull",
          "bull",
          "bear",
          "Bear",
          "Bullish",
          "bullish",
          "Bearish",
          "bearish",
          "Rally",
          "rally"
        ]
      },
      {
        "categoryName": "TRX",
        "wordsAssociatedWithCategory": [
          "TRX",
          "TronDAO",
          "tronDAO"
        ]
      },
      {
        "categoryName": "TUSD",
        "wordsAssociatedWithCategory": [
          "TUSD",
          "TrueUSD",
          "trueUSD"
        ]
      },
      {
        "categoryName": "TWT",
        "wordsAssociatedWithCategory": [
          "TWT"
        ],
        "includedPhrases": [
          "TRUST WALLET TOKEN"
        ]
      },
      {
        "categoryName": "UMA",
        "wordsAssociatedWithCategory": [
          "UMA"
        ],
        "includedPhrases": [
          "Universal Market Access"
        ]
      },
      {
        "categoryName": "UNI",
        "wordsAssociatedWithCategory": [
          "UNI",
          "Uniswap",
          "uniswap"
        ]
      },
      {
        "categoryName": "USDC",
        "wordsAssociatedWithCategory": [
          "USDC"
        ]
      },
      {
        "categoryName": "USDD",
        "wordsAssociatedWithCategory": [
          "USDD"
        ],
        "includedPhrases": [
          "USDD STABLECOIN"
        ]
      },
      {
        "categoryName": "USDT",
        "wordsAssociatedWithCategory": [
          "USDT",
          "Tether",
          "tether"
        ]
      },
      {
        "categoryName": "VET",
        "wordsAssociatedWithCategory": [
          "VET",
          "Vechain",
          "vechain"
        ]
      },
      {
        "categoryName": "WALLET",
        "wordsAssociatedWithCategory": [
          "Ledger",
          "ledger",
          "Trezor",
          "trezor",
          "Keepkey",
          "keepkey",
          "Coinomi",
          "coinomi",
          "Jaxx",
          "Myetherwallet",
          "myeterhwallet",
          "metamask",
          "Metamask"
        ]
      },
      {
        "categoryName": "WIF",
        "wordsAssociatedWithCategory": [
          "WIF"
        ]
      },
      {
        "categoryName": "WLD",
        "wordsAssociatedWithCategory": [
          "WLD",
          "Worldcoin",
          "worldcoin"
        ]
      },
      {
        "categoryName": "WOO",
        "wordsAssociatedWithCategory": [
          "WOO"
        ],
        "includedPhrases": [
          "WOO NETWORK"
        ]
      },
      {
        "categoryName": "XAUT",
        "wordsAssociatedWithCategory": [
          "XAUt"
        ],
        "includedPhrases": [
          "TETHER GOLD"
        ]
      },
      {
        "categoryName": "XDC",
        "wordsAssociatedWithCategory": [
          "XDC"
        ],
        "includedPhrases": [
          "XDC NETWORK"
        ]
      },
      {
        "categoryName": "XEC",
        "wordsAssociatedWithCategory": [
          "XEC"
        ],
        "includedPhrases": [
          "ECASH FOUNDATION"
        ]
      },
      {
        "categoryName": "XLM",
        "wordsAssociatedWithCategory": [
          "XLM"
        ],
        "includedPhrases": [
          "STELLAR NETWORK"
        ]
      },
      {
        "categoryName": "XMR",
        "wordsAssociatedWithCategory": [
          "XMR",
          "Monero",
          "monero"
        ]
      },
      {
        "categoryName": "XRP",
        "wordsAssociatedWithCategory": [
          "XRP"
        ],
        "includedPhrases": [
          "RIPPLE FOUNDATION"
        ]
      },
      {
        "categoryName": "XTZ",
        "wordsAssociatedWithCategory": [
          "XTZ"
        ],
        "includedPhrases": [
          "TEZOS BLOCKCHAIN"
        ]
      },
      {
        "categoryName": "YFI",
        "wordsAssociatedWithCategory": [
          "YFI"
        ],
        "includedPhrases": [
          "YEARN FINANCE",
          "YEARN.FINANCE"
        ]
      },
      {
        "categoryName": "ZEC",
        "wordsAssociatedWithCategory": [
          "ZEC",
          "Zcash",
          "zcash"
        ]
      },
      {
        "categoryName": "ZK",
        "wordsAssociatedWithCategory": [
          "ZK",
          "Zksync",
          "zksync",
          "ZKsync"
        ]
      },
      {
        "categoryName": "ZRX",
        "wordsAssociatedWithCategory": [
          "ZRX"
        ],
        "includedPhrases": [
          "0X"
        ]
      }
    ],
    "Feeds": [
      {
        "key": "coindesk",
        "name": "CoinDesk",
        "img": "https://resources.cryptocompare.com/news/5/default.png",
        "lang": "EN"
      },
      {
        "key": "coindesk_es",
        "name": "CoinDesk",
        "img": "https://resources.cryptocompare.com/news/105/default.png",
        "lang": "ES"
      },
      {
        "key": "bitcoinmagazine",
        "name": "Bitcoin Magazine",
        "img": "https://images.cryptocompare.com/news/default/bitcoinmagazine.png",
        "lang": "EN"
      },
      {
        "key": "coingape",
        "name": "CoinGape",
        "img": "https://images.cryptocompare.com/news/default/coingape.png",
        "lang": "EN"
      },
      {
        "key": "blockworks",
        "name": "Blockworks",
        "img": "https://images.cryptocompare.com/news/default/blockworks.png",
        "lang": "EN"
      },
      {
        "key": "dailyhodl",
        "name": "The Daily Hodl",
        "img": "https://images.cryptocompare.com/news/default/dailyhodl.png",
        "lang": "EN"
      },
      {
        "key": "cryptoslate",
        "name": "CryptoSlate",
        "img": "https://images.cryptocompare.com/news/default/cryptoslate.png",
        "lang": "EN"
      },
      {
        "key": "decrypt",
        "name": "Decrypt",
        "img": "https://images.cryptocompare.com/news/default/decrypt.png",
        "lang": "EN"
      },
      {
        "key": "cryptopotato",
        "name": "Crypto Potato",
        "img": "https://images.cryptocompare.com/news/default/cryptopotato.png",
        "lang": "EN"
      },
      {
        "key": "cryptobriefing",
        "name": "Crypto Briefing",
        "img": "https://images.cryptocompare.com/news/default/cryptobriefing.png",
        "lang": "EN"
      },
      {
        "key": "theblock",
        "name": "TheBlock",
        "img": "https://images.cryptocompare.com/news/default/theblock.png",
        "lang": "EN"
      },
      {
        "key": "bitcoin.com",
        "name": "Bitcoin.com",
        "img": "https://images.cryptocompare.com/news/default/bitcoincom.png",
        "lang": "EN"
      },
      {
        "key": "newsbtc",
        "name": "NewsBTC",
        "img": "https://images.cryptocompare.com/news/default/newsbtc.png",
        "lang": "EN"
      },
      {
        "key": "utoday",
        "name": "U.Today",
        "img": "https://images.cryptocompare.com/news/default/utoday.png",
        "lang": "EN"
      },
      {
        "key": "bitcoinist",
        "name": "Bitcoinist",
        "img": "https://images.cryptocompare.com/news/default/bitcoinist.png",
        "lang": "EN"
      },
      {
        "key": "coinpedia",
        "name": "coinpedia",
        "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
        "lang": "EN"
      },
      {
        "key": "coinrepublic",
        "name": "The Coin Republic",
        "img": "https://images.cryptocompare.com/news/default/coinrepublic.png",
        "lang": "EN"
      },
      {
        "key": "chaintimes",
        "name": "Chaintimes",
        "img": "https://images.cryptocompare.com/news/default/chaintimes.png",
        "lang": "EN"
      },
      {
        "key": "ccn",
        "name": "CCN",
        "img": "https://images.cryptocompare.com/news/default/ccn.png",
        "lang": "EN"
      },
      {
        "key": "criptonoticias",
        "name": "CriptoNoticias",
        "img": "https://images.cryptocompare.com/news/default/cryptonoticias.png",
        "lang": "ES"
      },
      {
        "key": "financemagnates",
        "name": "Finance Magnates",
        "img": "https://images.cryptocompare.com/news/default/financemagnates.png",
        "lang": "EN"
      },
      {
        "key": "espaciobit",
        "name": "EspacioBit",
        "img": "https://images.cryptocompare.com/news/default/espaciobit.png",
        "lang": "ES"
      },
      {
        "key": "cryptonewsreview",
        "name": "CryptoNewsReview",
        "img": "https://images.cryptocompare.com/news/default/cryptonewsreview.png",
        "lang": "EN"
      },
      {
        "key": "cointelegraph_fr",
        "name": "CoinTelegraph",
        "img": "https://resources.cryptocompare.com/news/92/default.png",
        "lang": "FR"
      },
      {
        "key": "ethnews.com",
        "name": "ETHNews.com",
        "img": "https://images.cryptocompare.com/news/default/ethnews.png",
        "lang": "EN"
      },
      {
        "key": "cryptovest",
        "name": "CryptoVest",
        "img": "https://images.cryptocompare.com/news/default/cryptovest.png",
        "lang": "EN"
      },
      {
        "key": "cryptoinsider",
        "name": "CryptoInsider",
        "img": "https://images.cryptocompare.com/news/default/cryptoinsider.png",
        "lang": "EN"
      },
      {
        "key": "coinspeaker",
        "name": "CoinSpeaker",
        "img": "https://images.cryptocompare.com/news/default/coinspeaker.png",
        "lang": "EN"
      },
      {
        "key": "coinjoker",
        "name": "CoinJoker",
        "img": "https://images.cryptocompare.com/news/default/coinjoker.png",
        "lang": "EN"
      },
      {
        "key": "cointelligence",
        "name": "Cointelligence",
        "img": "https://images.cryptocompare.com/news/default/cointelligence.png",
        "lang": "EN"
      },
      {
        "key": "okexinsights",
        "name": "OKX Insights",
        "img": "https://images.cryptocompare.com/news/default/okexinsights.png",
        "lang": "EN"
      },
      {
        "key": "ambcrypto_es",
        "name": "AMB Crypto",
        "img": "https://images.cryptocompare.com/news/default/ambcrypto.png",
        "lang": "ES"
      },
      {
        "key": "cryptocoremedia",
        "name": "Crypto CoreMedia",
        "img": "https://images.cryptocompare.com/news/default/coremedia.png",
        "lang": "EN"
      },
      {
        "key": "bitcoinerx",
        "name": "Bitcoinerx",
        "img": "https://images.cryptocompare.com/news/default/bitcoinerx.png",
        "lang": "EN"
      },
      {
        "key": "crypto_watch_com_br",
        "name": "Crypto Watch",
        "img": "https://images.cryptocompare.com/news/default/crypto_watch_com_br.png",
        "lang": "PT"
      },
      {
        "key": "weisscrypto",
        "name": "Weiss Crypto Ratings",
        "img": "https://images.cryptocompare.com/news/default/weisscrypto.png",
        "lang": "EN"
      },
      {
        "key": "cryptonaute",
        "name": "Cryptonaute",
        "img": "https://resources.cryptocompare.com/news/89/default.png",
        "lang": "FR"
      },
      {
        "key": "forbes",
        "name": "Forbes Digital Assets",
        "img": "https://resources.cryptocompare.com/news/94/default.png",
        "lang": "EN"
      },
      {
        "key": "coinpaprika",
        "name": "Coinpaprika",
        "img": "https://resources.cryptocompare.com/news/80/default.png",
        "lang": "EN"
      },
      {
        "key": "cryptodaily",
        "name": "Crypto Daily",
        "img": "https://resources.cryptocompare.com/news/75/default.png",
        "lang": "EN"
      },
      {
        "key": "journalducoin",
        "name": "Journal Du Coin",
        "img": "https://resources.cryptocompare.com/news/86/default.png",
        "lang": "FR"
      },
      {
        "key": "coinotag",
        "name": "CoinOtag",
        "img": "https://resources.cryptocompare.com/news/77/default.png",
        "lang": "EN"
      },
      {
        "key": "cryptopolitan",
        "name": "Cryptopolitan",
        "img": "https://images.cryptocompare.com/news/default/cryptopolitan.png",
        "lang": "EN"
      },
      {
        "key": "seekingalpha",
        "name": "Seeking Alpha",
        "img": "https://images.cryptocompare.com/news/default/seekingalpha.png",
        "lang": "EN"
      },
      {
        "key": "bitzo",
        "name": "Bitzo",
        "img": "https://resources.cryptocompare.com/news/104/default.png",
        "lang": "EN"
      },
      {
        "key": "investing_comcryptonews",
        "name": "Investing.com Crypto News",
        "img": "https://resources.cryptocompare.com/news/106/default.png",
        "lang": "EN"
      },
      {
        "key": "chainwire",
        "name": "Chainwire",
        "img": "https://resources.cryptocompare.com/news/68/default.png",
        "lang": "EN"
      },
      {
        "key": "thecryptobasic",
        "name": "The Crypto Basic",
        "img": "https://images.cryptocompare.com/news/default/thecryptobasic.png",
        "lang": "EN"
      },
      {
        "key": "bitcoinworld",
        "name": "Bitcoin World",
        "img": "https://resources.cryptocompare.com/news/82/default.png",
        "lang": "EN"
      },
      {
        "key": "cryptonews",
        "name": "cryptonews",
        "img": "https://images.cryptocompare.com/news/default/cryptonews.png",
        "lang": "EN"
      },
      {
        "key": "themerkle",
        "name": "NullTx",
        "img": "https://images.cryptocompare.com/news/default/nulltx.png",
        "lang": "EN"
      },
      {
        "key": "investing_comcryptoopinionandanalysis",
        "name": "Investing.Com Crypto Opinion and Analysis",
        "img": "https://resources.cryptocompare.com/news/107/default.png",
        "lang": "EN"
      },
      {
        "key": "diariobitcoin",
        "name": "DiarioBitcoin",
        "img": "https://images.cryptocompare.com/news/default/diariobitcoin.png",
        "lang": "ES"
      },
      {
        "key": "cryptocoinnews",
        "name": "CryptoCoin.News",
        "img": "https://images.cryptocompare.com/news/default/cryptocoinnews.png",
        "lang": "EN"
      },
      {
        "key": "coinpaper",
        "name": "Coinpaper",
        "img": "https://resources.cryptocompare.com/news/93/default.png",
        "lang": "EN"
      },
      {
        "key": "cryptoast",
        "name": "Cryptoast",
        "img": "https://resources.cryptocompare.com/news/87/default.png",
        "lang": "FR"
      },
      {
        "key": "cryptonewsz",
        "name": "CryptoNewsZ",
        "img": "https://images.cryptocompare.com/news/default/cryptonewsz.png",
        "lang": "EN"
      },
      {
        "key": "huobi",
        "name": "Huobi blog",
        "img": "https://resources.cryptocompare.com/news/100/default.png",
        "lang": "EN"
      },
      {
        "key": "coinacademy",
        "name": "Coin Academy",
        "img": "https://resources.cryptocompare.com/news/90/default.png",
        "lang": "FR"
      },
      {
        "key": "bitcoincore",
        "name": "Bitcoin Core",
        "img": "https://resources.cryptocompare.com/news/109/default.png",
        "lang": "EN"
      },
      {
        "key": "zycrypto",
        "name": "ZyCrypto",
        "img": "https://images.cryptocompare.com/news/default/zycrypto.png",
        "lang": "EN"
      },
      {
        "key": "financialtimes_crypto_",
        "name": "Financial Times (Crypto)",
        "img": "https://resources.cryptocompare.com/news/102/default.png",
        "lang": "EN"
      },
      {
        "key": "trustnodes",
        "name": "TrustNodes",
        "img": "https://images.cryptocompare.com/news/default/trustnodes.png",
        "lang": "EN"
      },
      {
        "key": "finbold",
        "name": "Finbold",
        "img": "https://images.cryptocompare.com/news/default/finbold.png",
        "lang": "EN"
      },
      {
        "key": "ambcrypto",
        "name": "AMB Crypto",
        "img": "https://images.cryptocompare.com/news/default/ambcrypto.png",
        "lang": "EN"
      },
      {
        "key": "cointelegraph_es",
        "name": "Cointelegraph",
        "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
        "lang": "ES"
      },
      {
        "key": "cointelegraph",
        "name": "Cointelegraph",
        "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
        "lang": "EN"
      },
      {
        "key": "cointurk",
        "name": "CoinTurk",
        "img": "https://resources.cryptocompare.com/news/78/default.png",
        "lang": "TR"
      },
      {
        "key": "ethereumfoundation",
        "name": "Ethereum Foundation",
        "img": null,
        "lang": "EN"
      },
      {
        "key": "coinquora",
        "name": "Coin Edition",
        "img": "https://resources.cryptocompare.com/news/7/default.png",
        "lang": "EN"
      },
      {
        "key": "bitdegree",
        "name": "BitDegree",
        "img": "https://images.cryptocompare.com/news/default/bitdegree.png",
        "lang": "EN"
      },
      {
        "key": "timestabloid",
        "name": "TimesTabloid",
        "img": "https://resources.cryptocompare.com/news/67/default.png",
        "lang": "EN"
      },
      {
        "key": "invezz",
        "name": "Invezz",
        "img": "https://resources.cryptocompare.com/news/69/default.png",
        "lang": "EN"
      },
      {
        "key": "krakenblog",
        "name": "Kraken Blog",
        "img": "https://resources.cryptocompare.com/news/98/default.png",
        "lang": "EN"
      },
      {
        "key": "bitfinexblog",
        "name": "Bitfinex blog",
        "img": "https://resources.cryptocompare.com/news/99/default.png",
        "lang": "EN"
      },
      {
        "key": "coinotag",
        "name": "CoinOtag",
        "img": "https://resources.cryptocompare.com/news/97/default.png",
        "lang": "TR"
      },
      {
        "key": "cryptocompare",
        "name": "CryptoCompare",
        "img": "https://images.cryptocompare.com/news/default/cryptocompare.png",
        "lang": "EN"
      },
      {
        "key": "cointurken",
        "name": "CoinTurk News",
        "img": "https://resources.cryptocompare.com/news/79/default.png",
        "lang": "EN"
      },
      {
        "key": "bloomberg_crypto_",
        "name": "Bloomberg (Crypto)",
        "img": "https://resources.cryptocompare.com/news/103/default.png",
        "lang": "EN"
      },
      {
        "key": "blokt",
        "name": "Blokt",
        "img": "https://images.cryptocompare.com/news/default/blokt.png",
        "lang": "EN"
      },
      {
        "key": "cryptointelligence",
        "name": "CryptoIntelligence",
        "img": "https://resources.cryptocompare.com/news/95/default.png",
        "lang": "EN"
      },
      {
        "key": "bitcoinsistemi",
        "name": "BitcoinSistemi",
        "img": "https://resources.cryptocompare.com/news/81/default.png",
        "lang": "EN"
      },
      {
        "key": "cardanoofficialblog",
        "name": "Cardano Official Blog",
        "img": "https://resources.cryptocompare.com/news/108/default.png",
        "lang": "EN"
      },
      {
        "key": "btcpulse",
        "name": "BTC Pulse",
        "img": "https://resources.cryptocompare.com/news/85/default.png",
        "lang": "EN"
      },
      {
        "key": "thecoinrise",
        "name": "The Coin Rise",
        "img": "https://images.cryptocompare.com/news/default/thecoinrise.png",
        "lang": "EN"
      },
      {
        "key": "cryptoknowmics",
        "name": "Cryptoknowmics",
        "img": "https://images.cryptocompare.com/news/default/cryptoknowmics.png",
        "lang": "EN"
      },
      {
        "key": "crypto_news",
        "name": "crypto.news",
        "img": "https://resources.cryptocompare.com/news/73/default.png",
        "lang": "EN"
      },
      {
        "key": "tipranks",
        "name": "TipRanks",
        "img": "https://images.cryptocompare.com/news/default/tipranks.png",
        "lang": "EN"
      },
      {
        "key": "beincrypto",
        "name": "BeInCrypto",
        "img": "https://resources.cryptocompare.com/news/88/default.png",
        "lang": "FR"
      },
      {
        "key": "thedefiant",
        "name": "The Defiant",
        "img": "https://resources.cryptocompare.com/news/101/default.png",
        "lang": "EN"
      },
      {
        "key": "thenewscrypto",
        "name": "The News Crypto",
        "img": "https://images.cryptocompare.com/news/default/thenewscrypto.png",
        "lang": "EN"
      },
      {
        "key": "ccdata",
        "name": "CCData",
        "img": "https://resources.cryptocompare.com/news/76/default.png",
        "lang": "EN"
      },
      {
        "key": "cryptoglobe",
        "name": "CryptoGlobe",
        "img": "https://images.cryptocompare.com/news/default/cryptoglobe.png",
        "lang": "EN"
      },
      {
        "key": "nft_news",
        "name": "nft.news",
        "img": "https://resources.cryptocompare.com/news/74/default.png",
        "lang": "EN"
      },
      {
        "key": "coincu",
        "name": "Coincu",
        "img": "https://resources.cryptocompare.com/news/96/default.png",
        "lang": "EN"
      },
      {
        "key": "cryptonewsfr",
        "name": "Cryptonewsfr",
        "img": "https://resources.cryptocompare.com/news/91/default.png",
        "lang": "FR"
      },
      {
        "key": "coinnounce",
        "name": "Coinnounce",
        "img": "https://images.cryptocompare.com/news/default/coinnounce.png",
        "lang": "EN"
      },
      {
        "key": "livebitcoinnews",
        "name": "Live Bitcoin News",
        "img": "https://images.cryptocompare.com/news/default/livebitcoinnews.png",
        "lang": "EN"
      },
      {
        "key": "timesnext",
        "name": "TimesNext",
        "img": "https://images.cryptocompare.com/news/default/timesnext.png",
        "lang": "EN"
      },
      {
        "key": "ethereumworldnews",
        "name": "Ethereum World News",
        "img": "https://images.cryptocompare.com/news/default/ethereumworldnews.png",
        "lang": "EN"
      },
      {
        "key": "vauld_insights",
        "name": "Vauld Insights",
        "img": "https://images.cryptocompare.com/news/default/vauld_insights.png",
        "lang": "EN"
      },
      {
        "key": "cryptonomist",
        "name": "Cryptonomist",
        "img": "https://resources.cryptocompare.com/news/84/default.png",
        "lang": "EN"
      },
      {
        "key": "chaindd",
        "name": "Chaindd",
        "img": "https://images.cryptocompare.com/news/default/chaindd.png",
        "lang": "EN"
      },
      {
        "key": "dailycoin",
        "name": "Daily Coin",
        "img": "https://images.cryptocompare.com/news/default/dailycoin.png",
        "lang": "EN"
      },
      {
        "key": "99bitcoins",
        "name": "99bitcoins",
        "img": "https://images.cryptocompare.com/news/default/99bitcoins.png",
        "lang": "EN"
      },
      {
        "key": "yahoofinance",
        "name": "Yahoo Finance Bitcoin",
        "img": "https://images.cryptocompare.com/news/default/yahoofinance.png",
        "lang": "EN"
      }
    ]
  }
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

**Data object keys**: `Categories`, `Feeds`

## Performance

**Average Response Time**: 699.14ms  
**Min Response Time**: 699.14ms  
**Max Response Time**: 699.14ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 699.14ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
