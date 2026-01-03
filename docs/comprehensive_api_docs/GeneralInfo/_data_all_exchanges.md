# All Exchanges

**Endpoint**: `/data/all/exchanges`  
**Category**: GeneralInfo  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Other/allExchangesV4Endpoint](https://developers.coindesk.com/documentation/legacy/Other/allExchangesV4Endpoint)

## Description

List all available exchanges

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
curl -X GET "https://min-api.cryptocompare.com/data/all/exchanges"
```

### Python

```python
import requests

# Endpoint: /data/all/exchanges
url = "https://min-api.cryptocompare.com/data/all/exchanges"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/all/exchanges
const url = "https://min-api.cryptocompare.com/data/all/exchanges";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "aax": {},
  "ABCC": {},
  "ACX": {},
  "AidosMarket": {},
  "alphaex": {},
  "archax": {},
  "ascendex": {
    "1": [
      "USDT"
    ],
    "4": [
      "USDT"
    ],
    "DESCI": [
      "USDT"
    ],
    "GOAT": [
      "USDT"
    ],
    "DOGEGOV": [
      "USDT"
    ],
    "MAHA": [
      "USDT"
    ],
    "BNB": [
      "USD",
      "USDT"
    ],
    "HTR": [
      "USDT"
    ],
    "IMGN": [
      "USDT"
    ],
    "NIM": [
      "USDT"
    ],
    "ZEC": [
      "USDT"
    ],
    "MIM": [
      "USDT"
    ],
    "SUSHI": [
      "USDT"
    ],
    "ZEE": [
      "USDT"
    ],
    "ROSS": [
      "USDT"
    ],
    "PIXEL": [
      "USDT"
    ],
    "PEPE": [
      "USDT"
    ],
    "DOT": [
      "USD",
      "USDT"
    ],
    "POOLX": [
      "USDT"
    ],
    "BTC": [
      "USD",
      "USDT"
    ],
    "SWP": [
      "USDT"
    ],
    "LETSBONK": [
      "USDT"
    ],
    "COOKIE": [
      "USDT"
    ],
    "PING": [
      "USDT"
    ],
    "AVAIL": [
      "USDT"
    ],
    "SUNDOG": [
      "USDT"
    ],
    "WBTC": [
      "USDT"
    ],
    "AJNA": [
      "USDT"
    ],
    "FWC": [
      "USDT"
    ],
    "KASPER": [
      "USDT"
    ],
    "SIGN": [
      "USDT"
    ],
    "METIS": [
      "USDT"
    ],
    "ZIL": [
      "USD",
      "USDT"
    ],
    "MOVE": [
      "USDT"
    ],
    "OSCAR": [
      "USDT"
    ],
    "BTT": [
      "USDT"
    ],
    "MATIC": [
      "USD"
    ],
    "AKUMA": [
      "USDT"
    ],
    "LIKE": [
      "USDT"
    ],
    "TROLL": [
      "USDT"
    ],
    "AIXBT": [
      "USDT"
    ],
    "VIRTUAL": [
      "USDT"
    ],
    "AVA": [
      "USDT"
    ],
    "CUDIS": [
      "USDT"
    ],
    "MRLIGHTSPEED": [
      "USDT"
    ],
    "SCROLL": [
      "USDT"
    ],
    "GNS": [
      "USDT"
    ],
    "PI": [
      "USDT"
    ],
    "ASTER": [
      "USDT"
    ],
    "FET": [
      "USDT"
    ],
    "VIC": [
      "USDT"
    ],
    "BOLT": [
      "USDT"
    ],
    "HEGE": [
      "USDT"
    ],
    "TRUMPJR": [
      "USDT"
    ],
    "NEWT": [
      "USDT"
    ],
    "STORJ": [
      "USDT"
    ],
    "MWC": [
      "USDT"
    ],
    "CVX": [
      "USDT"
    ],
    "PURPLEBTC": [
      "USDT"
    ],
    "CHZ": [
      "USDT"
    ],
    "DASH": [
      "USDT"
    ],
    "BEFE": [
      "USDT"
    ],
    "MEW": [
      "USDT"
    ],
    "PORTAL": [
      "USDT"
    ],
    "HTX": [
      "USDT"
    ],
    "BRUH": [
      "USDT"
    ],
    "VET": [
      "USDT",
      "USD"
    ],
    "MET": [
      "USDT"
    ],
    "USDX": [
      "USDT"
    ],
    "MIGGLES": [
      "USDT"
    ],
    "BIZA": [
      "USDT"
    ],
    "PAXG": [
      "USDT"
    ],
    "COK": [
      "USDT"
    ],
    "OXY": [
      "USDT"
    ],
    "TRX": [
      "USDT",
      "USD"
    ],
    "POLIS": [
      "USDT"
    ],
    "RVN": [
      "USDT"
    ],
    "ALICE": [
      "USDT"
    ],
    "H": [
      "USDT"
    ],
    "TETSUO": [
      "USDT"
    ],
    "OPEN": [
      "USDT"
    ],
    "ZIG": [
      "USDT"
    ],
    "FOUR": [
      "USDT"
    ],
    "AVC": [
      "USDT"
    ],
    "LUCE": [
      "USDT"
    ],
    "LOKR": [
      "USDT"
    ],
    "ARIX": [
      "USDT"
    ],
    "BABYCATE": [
      "USDT"
    ],
    "STRK": [
      "USDT"
    ],
    "REVV": [
      "USDT"
    ],
    "DAO": [
      "USDT"
    ],
    "BRETT": [
      "USDT"
    ],
    "ZKJ": [
      "USDT"
    ],
    "LYA": [
      "USDT"
    ],
    "CROWWITH": [
      "USDT"
    ],
    "AI16Z": [
      "USDT"
    ],
    "SAND": [
      "USDT"
    ],
    "BAN": [
      "USDT"
    ],
    "FRIN": [
      "USDT"
    ],
    "ETH": [
      "USD",
      "BTC",
      "USDT"
    ],
    "LKY": [
      "USDT"
    ],
    "USUAL": [
      "USDT"
    ],
    "AP": [
      "USDT"
    ],
    "GNO": [
      "USDT"
    ],
    "USELESS": [
      "USDT"
    ],
    "MNEE": [
      "USDT"
    ],
    "IO": [
      "USDT"
    ],
    "ENA": [
      "USDT"
    ],
    "MANA": [
      "USDT"
    ],
    "NPC": [
      "USDT"
    ],
    "MYRO": [
      "USDT"
    ],
    "CAT": [
      "USDT"
    ],
    "LISTA": [
      "USDT"
    ],
    "JULD": [
      "USDT"
    ],
    "MOG": [
      "USDT"
    ],
    "ELIZAOS": [
      "USDT"
    ],
    "FTRB": [
      "USDT"
    ],
    "ONDO": [
      "USDT"
    ],
    "CULT": [
      "USDT"
    ],
    "XPRT": [
      "USDT"
    ],
    "ACX": [
      "USDT"
    ],
    "SHAR": [
      "USDT"
    ],
    "HOSKY": [
      "USDT"
    ],
    "HARD": [
      "USDT"
    ],
    "MONI": [
      "USDT"
    ],
    "ALGO": [
      "USD",
      "USDT"
    ],
    "ZKC": [
      "USDT"
    ],
    "IOST": [
      "USDT"
    ],
    "ANVL": [
      "USDT"
    ],
    "JAILSTOOL": [
      "USDT"
    ],
    "POLC": [
      "USDT"
    ],
    "WEN": [
      "USDT"
    ],
    "XEM": [
      "USDT"
    ],
    "NOICE": [
      "USDT"
    ],
    "SYRUP": [
      "USDT"
    ],
    "BR": [
      "USDT"
    ],
    "SWAP": [
      "USDT"
    ],
    "BROAK": [
      "USDT"
    ],
    "CNS": [
      "USDT"
    ],
    "NIOX": [
      "USDT"
    ],
    "NEIROINU": [
      "USDT"
    ],
    "LOBO": [
      "USDT"
    ],
    "ZANO": [
      "USDT"
    ],
    "QNT": [
      "USDT"
    ],
    "HOPR": [
      "USDT"
    ],
    "BYTE": [
      "USDT"
    ],
    "LTC": [
      "USDT"
    ],
    "W": [
      "USDT"
    ],
    "DIVER": [
      "USDT"
    ],
    "BUZZ": [
      "USDT"
    ],
    "AKRO": [
      "USDT"
    ],
    "EDU": [
      "USDT"
    ],
    "XAUT": [
      "USD",
      "BTC",
      "USDT"
    ],
    "AIDOGE": [
      "USDT"
    ],
    "YURU": [
      "USDT"
    ],
    "PUSS": [
      "USDT"
    ],
    "FIDA": [
      "USDT"
    ],
    "ATH": [
      "USDT"
    ],
    "INJ": [
      "USDT"
    ],
    "ADASOL": [
      "USDT"
    ],
    "GRT": [
      "USDT"
    ],
    "PTF": [
      "USDT"
    ],
    "CCD": [
      "USDT"
    ],
    "A": [
      "USD",
      "USDT"
    ],
    "SQGROW": [
      "USDT"
    ],
    "NOM": [
      "USDT"
    ],
    "JST": [
      "USDT"
    ],
    "DIA": [
      "USDT"
    ],
    "GUAN": [
      "USDT"
    ],
    "SFP": [
      "USDT"
    ],
    "SONIC": [
      "USDT"
    ],
    "SIDUS": [
      "USDT"
    ],
    "1INCH": [
      "USDT"
    ],
    "CXT": [
      "USDT"
    ],
    "EIGEN": [
      "USDT"
    ],
    "MINDFAK": [
      "USDT",
      "USD"
    ],
    "SATS": [
      "USDT"
    ],
    "POL": [
      "USDT",
      "USD"
    ],
    "ARB": [
      "USDT"
    ],
    "DOGK": [
      "USDT"
    ],
    "DOGY": [
      "USDT"
    ],
    "RADX": [
      "USDT"
    ],
    "CCDOG": [
      "USDT"
    ],
    "PEIPEI": [
      "USDT"
    ],
    "BOBLS": [
      "USDT"
    ],
    "BLAST": [
      "USDT"
    ],
    "ZKF": [
      "USDT"
    ],
    "BOBT": [
      "USDT"
    ],
    "FRM": [
      "USDT"
    ],
    "ARKM": [
      "USDT"
    ],
    "ESX": [
      "USDT"
    ],
    "FLAME": [
      "USDT"
    ],
    "B": [
      "USDT"
    ],
    "USDR": [
      "USDT",
      "USD"
    ],
    "PUMP": [
      "USDT"
    ],
    "XFI": [
      "BTC",
      "USDT"
    ],
    "NOVA": [
      "USDT"
    ],
    "CPOOL": [
      "USDT"
    ],
    "ODDZ": [
      "USDT"
    ],
    "OMI": [
      "USDT"
    ],
    "PYTH": [
      "USDT"
    ],
    "HMSTR": [
      "USDT"
    ],
    "HOUSE": [
      "USDT"
    ],
    "LUMIA": [
      "USDT"
    ],
    "HIPPO": [
      "USDT"
    ],
    "SAROS": [
      "USDT"
    ],
    "LADYS": [
      "USDT"
    ],
    "ARC": [
      "USDT"
    ],
    "SKYAI": [
      "USDT"
    ],
    "COTI": [
      "USDT"
    ],
    "KHAI": [
      "USDT"
    ],
    "URANUS": [
      "USDT"
    ],
    "WIF": [
      "USDT"
    ],
    "KERNEL": [
      "USDT"
    ],
    "TROPPY": [
      "USDT"
    ],
    "AAST": [
      "USDT"
    ],
    "DINGO": [
      "USDT"
    ],
    "WSBABY": [
      "USDT"
    ],
    "WIN": [
      "USDT"
    ],
    "GMX": [
      "USDT"
    ],
    "ETHFI": [
      "USDT"
    ],
    "MARSH": [
      "USDT"
    ],
    "FWOG": [
      "USDT"
    ],
    "ADA": [
      "USD",
      "USDT"
    ],
    "SPX": [
      "USDT"
    ],
    "STX": [
      "USDT"
    ],
    "TRUMP": [
      "USDT"
    ],
    "MCTP": [
      "USDT"
    ],
    "TRENCHER": [
      "USDT"
    ],
    "LINK": [
      "USD",
      "USDT"
    ],
    "XAI": [
      "USDT"
    ],
    "CUUT": [
      "USDT"
    ],
    "CETUS": [
      "USDT"
    ],
    "P2P": [
      "USDT"
    ],
    "USDD": [
      "USDT"
    ],
    "JKC": [
      "USDT"
    ],
    "BDX": [
      "USDT"
    ],
    "CSPR": [
      "USDT"
    ],
    "SWEAT": [
      "USDT"
    ],
    "CELR": [
      "USDT"
    ],
    "AUCTION": [
      "USDT"
    ],
    "SHELL": [
      "USDT"
    ],
    "RED": [
      "USDT"
    ],
    "NEIRO": [
      "USDT"
    ],
    "BABYBONK": [
      "USDT"
    ],
    "ACT": [
      "USDT"
    ],
    "SUEDE": [
      "USDT"
    ],
    "GIGGLE": [
      "USDT"
    ],
    "DESO": [
      "USDT"
    ],
    "MNRY": [
      "USDT"
    ],
    "BILLY": [
      "USDT"
    ],
    "APE": [
      "USDT"
    ],
    "BCH": [
      "USDT"
    ],
    "TLOS": [
      "USDT"
    ],
    "TEMA": [
      "USDT"
    ],
    "TON": [
      "USDT"
    ],
    "FIN": [
      "USDT"
    ],
    "VELOD": [
      "USDT"
    ],
    "BNBXBT": [
      "USDT"
    ],
    "GOHOME": [
      "USDT"
    ],
    "VRTX": [
      "USDT"
    ],
    "ETC": [
      "USDT"
    ],
    "MOODENG": [
      "USDT"
    ],
    "DRIFT": [
      "USDT"
    ],
    "KAS": [
      "USDT"
    ],
    "LAUNCHCOIN": [
      "USDT"
    ],
    "XRP": [
      "USDT",
      "USD"
    ],
    "SCF": [
      "USDT"
    ],
    "KIN": [
      "USDT"
    ],
    "SOL": [
      "BTC",
      "USDT",
      "USD"
    ],
    "NUTS": [
      "USDT"
    ],
    "LF": [
      "USDT"
    ],
    "UFT": [
      "USDT"
    ],
    "DF": [
      "USDT"
    ],
    "CARDS": [
      "USDT"
    ],
    "PENG": [
      "USDT"
    ],
    "SSSSS": [
      "USDT"
    ],
    "DUEL": [
      "USDT"
    ],
    "UNI": [
      "USDT"
    ],
    "WLD": [
      "USDT"
    ],
    "RAY": [
      "USDT"
    ],
    "NOCHILL": [
      "USDT"
    ],
    "PROMPT": [
      "USDT"
    ],
    "XEC": [
      "USDT"
    ],
    "PALU": [
      "USDT"
    ],
    "XEP": [
      "USDT"
    ],
    "RARE": [
      "USDT"
    ],
    "BAND": [
      "USDT"
    ],
    "LEMX": [
      "USDT"
    ],
    "LDXG": [
      "USDT"
    ],
    "AEVO": [
      "USDT"
    ],
    "AVAXAI": [
      "USDT"
    ],
    "PIZA": [
      "USDT"
    ],
    "BOOCHIE": [
      "USDT"
    ],
    "SAHARA": [
      "USDT"
    ],
    "OG": [
      "USDT"
    ],
    "IMX": [
      "USDT"
    ],
    "KANGO": [
      "USDT"
    ],
    "JELLYJELLY": [
      "USDT"
    ],
    "KAITO": [
      "USDT"
    ],
    "FREL": [
      "USDT"
    ],
    "ME": [
      "USDT"
    ],
    "BAGWORK": [
      "USDT"
    ],
    "GAU": [
      "USDT"
    ],
    "RENDER": [
      "USDT"
    ],
    "CWS": [
      "USDT"
    ],
    "NSURE": [
      "USDT"
    ],
    "ORDER": [
      "USDT"
    ],
    "FIGHT": [
      "USDT"
    ],
    "BEAM": [
      "USDT"
    ],
    "BANK": [
      "USDT"
    ],
    "NIL": [
      "USDT"
    ],
    "ALEX": [
      "USDT"
    ],
    "TAIKO": [
      "USDT"
    ],
    "AKIO": [
      "USDT"
    ],
    "MIX": [
      "USDT"
    ],
    "HONEY": [
      "USDT"
    ],
    "MANTA": [
      "USDT"
    ],
    "PROVE": [
      "USDT"
    ],
    "WLFI": [
      "USDT"
    ],
    "VERA": [
      "USDT"
    ],
    "QUBIC": [
      "USDT"
    ],
    "SYPOOL": [
      "USDT"
    ],
    "GPS": [
      "USDT"
    ],
    "BDTC": [
      "USDT"
    ],
    "IKIGAI": [
      "USDT"
    ],
    "THE": [
      "USDT"
    ],
    "DEEPSEEK": [
      "USDT"
    ],
    "LUX": [
      "USDT"
    ],
    "QTUM": [
      "USDT"
    ],
    "ZRX": [
      "USDT"
    ],
    "YZY": [
      "USDT"
    ],
    "JESSE": [
      "USDT"
    ],
    "BUILDON": [
      "USDT"
    ],
    "MANEKI": [
      "USDT"
    ],
    "UOS": [
      "USDT"
    ],
    "WAS": [
      "USDT"
    ],
    "SPK": [
      "USDT"
    ],
    "MOBY": [
      "USDT"
    ],
    "USDQ": [
      "USD",
      "USDT"
    ],
    "HGET": [
      "USDT"
    ],
    "SINK": [
      "USDT"
    ],
    "POWSCHE": [
      "USDT"
    ],
    "DOG": [
      "USDT"
    ],
    "RATS": [
      "USDT"
    ],
    "GOKU": [
      "USDT"
    ],
    "HFT": [
      "USDT"
    ],
    "ATR": [
      "USDT"
    ],
    "YGG": [
      "USDT"
    ],
    "ATOM": [
      "USDT",
      "USD"
    ],
    "MAXETH": [
      "USDT"
    ],
    "BERT": [
      "USDT"
    ],
    "M87": [
      "USDT"
    ],
    "TIA": [
      "USDT"
    ],
    "CGPT": [
      "USDT"
    ],
    "FTT": [
      "USDT",
      "USD"
    ],
    "LAYER": [
      "USDT"
    ],
    "S": [
      "USDT"
    ],
    "NEET": [
      "USDT"
    ],
    "HAEDAL": [
      "USDT"
    ],
    "BNC": [
      "USDT"
    ],
    "DOGE": [
      "USDT"
    ],
    "FIO": [
      "USDT"
    ],
    "DIVI": [
      "USDT"
    ],
    "SUN": [
      "USDT"
    ],
    "MICE": [
      "USDT"
    ],
    "TST": [
      "USDT"
    ],
    "VRA": [
      "USDT"
    ],
    "X": [
      "USDT"
    ],
    "OP": [
      "USDT"
    ],
    "SHIB": [
      "USDT"
    ],
    "SOLV": [
      "USDT"
    ],
    "DARK": [
      "USDT"
    ],
    "USDT": [
      "USD"
    ],
    "BAT": [
      "USDT"
    ],
    "KIMBO": [
      "USDT"
    ],
    "PECH": [
      "USDT"
    ],
    "NEIROLIVE": [
      "USDT"
    ],
    "HUAHUA": [
      "USDT"
    ],
    "HIGH": [
      "USDT"
    ],
    "BANANA": [
      "USDT"
    ],
    "FRAX": [
      "USDT"
    ],
    "ZORA": [
      "USDT"
    ],
    "A2Z": [
      "USDT"
    ],
    "SNX": [
      "USDT"
    ],
    "ONE": [
      "USDT"
    ],
    "CKB": [
      "USDT"
    ],
    "NFT": [
      "USDT"
    ],
    "XLM": [
      "USDT"
    ],
    "BOME": [
      "USDT"
    ],
    "PNUT": [
      "USDT"
    ],
    "PORK": [
      "USDT"
    ],
    "G": [
      "USDT"
    ],
    "AVNT": [
      "USDT"
    ],
    "OPUL": [
      "USDT"
    ],
    "REZ": [
      "USDT"
    ],
    "EDAT": [
      "USDT"
    ],
    "BLUR": [
      "USDT"
    ],
    "EURR": [
      "USDT"
    ],
    "GME": [
      "USDT"
    ],
    "GRASS": [
      "USDT"
    ],
    "CHR": [
      "USDT"
    ],
    "MCOIN": [
      "USDT"
    ],
    "PENGU": [
      "USDT"
    ],
    "SENDOR": [
      "USDT"
    ],
    "CAKE": [
      "USDT"
    ],
    "MEME": [
      "USDT"
    ],
    "BNBHOLDER": [
      "USDT"
    ],
    "TOON": [
      "USDT"
    ],
    "XCAD": [
      "USDT"
    ],
    "BARIO": [
      "USDT"
    ],
    "XYO": [
      "USDT"
    ],
    "C98": [
      "USDT"
    ],
    "TITCOIN": [
      "USDT"
    ],
    "PUPS": [
      "USDT"
    ],
    "STOS": [
      "USDT"
    ],
    "XDC": [
      "USDT"
    ],
    "FLOKI": [
      "USDT"
    ],
    "NATO": [
      "USDT"
    ],
    "FIRO": [
      "USDT"
    ],
    "BEEG": [
      "USDT"
    ],
    "APFC": [
      "USDT"
    ],
    "AXOL": [
      "USDT"
    ],
    "FHE": [
      "USDT"
    ],
    "WHY": [
      "USDT"
    ],
    "ETHW": [
      "USDT"
    ],
    "ONGAS": [
      "USDT"
    ],
    "RDNT": [
      "USDT"
    ],
    "BMT": [
      "USDT"
    ],
    "ROUTE": [
      "USDT"
    ],
    "LIME": [
      "USDT"
    ],
    "NEIROCOIN": [
      "USDT"
    ],
    "LFGO": [
      "USDT"
    ],
    "XPL": [
      "USDT"
    ],
    "LBAI": [
      "USDT"
    ],
    "OLT": [
      "USDT"
    ],
    "FUSE": [
      "USDT"
    ],
    "UNDEAD": [
      "USDT"
    ],
    "JTO": [
      "USDT"
    ],
    "AAVE": [
      "USDT"
    ],
    "CRV": [
      "USDT"
    ],
    "AXS": [
      "USDT"
    ],
    "MUBARAK": [
      "USDT"
    ],
    "ZETA": [
      "USDT"
    ],
    "ZK": [
      "USDT"
    ],
    "SNY": [
      "USDT"
    ],
    "BIGTIME": [
      "USDT"
    ],
    "ILV": [
      "USDT"
    ],
    "ANIME": [
      "USDT"
    ],
    "FARTCOIN": [
      "USDT"
    ],
    "DUSK": [
      "USDT"
    ],
    "XTZ": [
      "USDT"
    ],
    "LRC": [
      "USDT"
    ],
    "VINE": [
      "USDT"
    ],
    "KIBSHI": [
      "USDT"
    ],
    "RSR": [
      "USDT"
    ],
    "GALEON": [
      "USDT"
    ],
    "VSG": [
      "USDT"
    ],
    "KEX": [
      "USDT"
    ],
    "QUICK": [
      "USDT"
    ],
    "HOPPY": [
      "USDT"
    ],
    "MERL": [
      "USDT"
    ],
    "YNE": [
      "USDT"
    ],
    "OMNI": [
      "USDT"
    ],
    "ID": [
      "USDT"
    ],
    "VANRY": [
      "USDT"
    ],
    "PHIL": [
      "USDT"
    ],
    "ORCA": [
      "USDT"
    ],
    "BEY": [
      "USDT"
    ],
    "ZYNC": [
      "USDT"
    ],
    "NXPC": [
      "USDT"
    ],
    "ONT": [
      "USDT"
    ],
    "HIGHER": [
      "USDT"
    ],
    "RETAR": [
      "USDT"
    ],
    "ACH": [
      "USDT"
    ],
    "MAGAHAT": [
      "USDT"
    ],
    "SCUBA": [
      "USDT"
    ],
    "KONAN": [
      "USDT"
    ],
    "SLIM": [
      "USDT"
    ],
    "ASD": [
      "USDT"
    ],
    "LTO": [
      "USDT"
    ],
    "DC": [
      "USDT"
    ],
    "URMOM": [
      "USDT"
    ],
    "CRO": [
      "USDT"
    ],
    "COMP": [
      "USDT"
    ],
    "GEEQ": [
      "USDT"
    ],
    "FIL": [
      "USDT"
    ],
    "JCO": [
      "USDT"
    ],
    "SWARMS": [
      "USDT"
    ],
    "DAKU": [
      "USDT"
    ],
    "MASK": [
      "USDT"
    ],
    "VVV": [
      "USDT"
    ],
    "VOXEL": [
      "USDT"
    ],
    "DOOD": [
      "USDT"
    ],
    "FORWARD": [
      "USDT"
    ],
    "SIREN": [
      "USDT"
    ],
    "BIO": [
      "USDT"
    ],
    "ALT": [
      "USDT"
    ],
    "SUI": [
      "USDT"
    ],
    "BIAO": [
      "USDT"
    ],
    "SKYA": [
      "USDT"
    ],
    "NEO": [
      "USDT"
    ],
    "JUP": [
      "USDT"
    ],
    "SMTY": [
      "USDT"
    ],
    "PENDLE": [
      "USDT"
    ],
    "RUNE": [
      "USDT"
    ],
    "RUNESX": [
      "USDT"
    ],
    "HOOK": [
      "USDT"
    ],
    "DEGO": [
      "USDT"
    ],
    "SSV": [
      "USDT"
    ],
    "PONKE": [
      "USDT"
    ],
    "COW": [
      "USDT"
    ],
    "POPDOG": [
      "USDT"
    ],
    "RPL": [
      "USDT"
    ],
    "ENS": [
      "USDT"
    ],
    "RIZZMAS": [
      "USDT"
    ],
    "AVL": [
      "USDT"
    ],
    "ATLAS": [
      "USDT"
    ],
    "KAVA": [
      "USDT"
    ],
    "LINEA": [
      "USDT"
    ],
    "DYDX": [
      "USDT"
    ],
    "OM": [
      "USDT"
    ],
    "EPIC": [
      "USDT"
    ],
    "BABY": [
      "USDT"
    ],
    "CAPS": [
      "USDT"
    ],
    "BRISE": [
      "USDT"
    ],
    "LEO": [
      "USDT"
    ],
    "ALKI": [
      "USDT"
    ],
    "BROCCO": [
      "USDT"
    ],
    "XDAI": [
      "USDT"
    ],
    "HOT": [
      "USDT"
    ],
    "TNSR": [
      "USDT"
    ],
    "ORDI": [
      "USDT"
    ],
    "GTAI": [
      "USDT"
    ],
    "ENJ": [
      "USDT"
    ],
    "BROCCOLI": [
      "USDT"
    ],
    "TRAXX": [
      "USDT"
    ],
    "SHOGGOTH": [
      "USDT"
    ],
    "KIKI": [
      "USDT"
    ],
    "DEGEN": [
      "USDT"
    ],
    "AVAX": [
      "USDT"
    ],
    "STARTUP": [
      "USDT"
    ],
    "WOLF": [
      "USDT"
    ],
    "ZRO": [
      "USDT"
    ],
    "LOOKS": [
      "USDT"
    ],
    "ELON": [
      "USDT"
    ],
    "ICE": [
      "USDT"
    ],
    "WCT": [
      "USDT"
    ],
    "AITECH": [
      "USDT"
    ],
    "LDO": [
      "USDT"
    ],
    "STASH": [
      "USDT"
    ],
    "PINU100X": [
      "USDT"
    ],
    "WOO": [
      "USDT"
    ],
    "UBX": [
      "USDT"
    ],
    "SHRUB": [
      "USDT"
    ],
    "BB": [
      "USDT"
    ],
    "WALTER": [
      "USDT"
    ],
    "K": [
      "USDT"
    ],
    "APT": [
      "USDT"
    ],
    "CHILLGUY": [
      "USDT"
    ],
    "DONKEY": [
      "USDT"
    ],
    "WOJAK": [
      "USDT"
    ],
    "TOWER": [
      "USDT"
    ],
    "NOT": [
      "USDT"
    ],
    "EGLD": [
      "USDT"
    ],
    "B2": [
      "USDT"
    ],
    "ZRC": [
      "USDT"
    ],
    "ICP": [
      "USDT"
    ],
    "TORAN": [
      "USDT"
    ],
    "LAND": [
      "USDT"
    ],
    "EURQ": [
      "USDT"
    ],
    "EPT": [
      "USDT"
    ],
    "JYAI": [
      "USDT"
    ],
    "DOGS": [
      "USDT"
    ],
    "RESOLV": [
      "USDT"
    ],
    "WTF": [
      "USDT"
    ],
    "NACHO": [
      "USDT"
    ],
    "AKT": [
      "USDT"
    ],
    "SOPHON": [
      "USDT"
    ],
    "L3": [
      "USDT"
    ],
    "NGTG": [
      "USDT"
    ],
    "AB": [
      "USDT"
    ],
    "TREE": [
      "USDT"
    ],
    "TURBO": [
      "USDT"
    ],
    "ZBCN": [
      "USDT"
    ],
    "NEAR": [
      "USDT"
    ],
    "PDEX": [
      "USDT"
    ]
  },
  "ataix": {},
  "backpack": {
    "XPL": [
      "USDC"
    ],
    "PIPE": [
      "USDC"
    ],
    "HYPE": [
      "USDC"
    ],
    "SEI": [
      "USDC"
    ],
    "PUMP": [
      "USDC"
    ],
    "RENDER": [
      "USDC"
    ],
    "APT": [
      "USDC"
    ],
    "POL": [
      "USDC"
    ],
    "ZRO": [
      "USDC"
    ],
    "ME": [
      "USDC"
    ],
    "WIF": [
      "USDC"
    ],
    "HNT": [
      "USDC"
    ],
    "SUI": [
      "USDC"
    ],
    "WEN": [
      "USDC"
    ],
    "MOODENG": [
      "USDC"
    ],
    "BLUE": [
      "USDC"
    ],
    "BTC": [
      "USDC"
    ],
    "XRP": [
      "USDC"
    ],
    "BOME": [
      "USDC"
    ],
    "TRUMP": [
      "USDC"
    ],
    "DRIFT": [
      "USDC"
    ],
    "WCT": [
      "USDC"
    ],
    "APE": [
      "USDC"
    ],
    "WLFI": [
      "USDC"
    ],
    "RAY": [
      "USDC"
    ],
    "HAEDAL": [
      "USDC"
    ],
    "JUP": [
      "USDC"
    ],
    "CLOUD": [
      "USDC"
    ],
    "2Z": [
      "USDC"
    ],
    "WAL": [
      "USDC"
    ],
    "LDO": [
      "USDC"
    ],
    "0G": [
      "USDC"
    ],
    "STRK": [
      "USDC"
    ],
    "FLOCK": [
      "USDC"
    ],
    "ENA": [
      "USDC"
    ],
    "IO": [
      "USDC"
    ],
    "WLD": [
      "USDC"
    ],
    "SEND": [
      "USDC"
    ],
    "SONIC": [
      "USDC"
    ],
    "LINK": [
      "USDC"
    ],
    "DOGE": [
      "USDC"
    ],
    "PRCL": [
      "USDC"
    ],
    "MET": [
      "USDC"
    ],
    "DBR": [
      "USDC"
    ],
    "PYTH": [
      "USDC"
    ],
    "USDC": [
      "USDT"
    ],
    "AAVE": [
      "USDC"
    ],
    "ETH": [
      "USDC"
    ],
    "ONDO": [
      "USDC"
    ],
    "TNSR": [
      "USDC"
    ],
    "STABLE": [
      "USDC"
    ],
    "SOL": [
      "USDC"
    ],
    "KMNO": [
      "USDC"
    ],
    "PEPE": [
      "USDC"
    ],
    "W": [
      "USDC"
    ],
    "JTO": [
      "USDC"
    ],
    "BNB": [
      "USDC"
    ],
    "FRAG": [
      "USDC"
    ],
    "SWTCH": [
      "USDC"
    ],
    "APR": [
      "USDC"
    ],
    "UNI": [
      "USDC"
    ],
    "SHIB": [
      "USDC"
    ],
    "NS": [
      "USDC"
    ],
    "BONK": [
      "USDC"
    ],
    "PENGU": [
      "USDC"
    ],
    "DEEP": [
      "USDC"
    ],
    "ES": [
      "USDC"
    ]
  },
  "bequant": {
    "ALGO": [
      "USDT",
      "BTC"
    ],
    "SNX": [
      "BTC",
      "USDT"
    ],
    "BTG": [
      "ETH",
      "USDT",
      "BTC"
    ],
    "AAVE": [
      "USDT",
      "BTC"
    ],
    "CHZ": [
      "BTC",
      "USDT"
    ],
    "CRV": [
      "USDT",
      "BTC"
    ],
    "ETH": [
      "GBP",
      "USDT",
      "USDC",
      "BTC"
    ],
    "A": [
      "USDT",
      "BTC"
    ],
    "BSV": [
      "BTC",
      "USDT"
    ],
    "XRP": [
      "USD",
      "GBP",
      "EUR",
      "USDT",
      "BTC"
    ],
    "OP": [
      "USDT"
    ],
    "SHIB": [
      "USDT",
      "BTC"
    ],
    "TON": [
      "USDT",
      "BTC",
      "USDC"
    ],
    "DYDX": [
      "USDT",
      "BTC"
    ],
    "USDT": [
      "GBP",
      "USD",
      "EUR"
    ],
    "BAT": [
      "USDT",
      "BTC"
    ],
    "XTZ": [
      "BTC",
      "USDT"
    ],
    "TRX": [
      "BTC",
      "ETH",
      "USDT"
    ],
    "NEAR": [
      "BTC",
      "USDT"
    ],
    "WBTC": [
      "BTC",
      "USDT"
    ],
    "S": [
      "USDT"
    ],
    "DOGE": [
      "BTC",
      "USDT"
    ],
    "XLM": [
      "BTC",
      "USDT"
    ],
    "TUSD": [
      "USDT"
    ],
    "BCH": [
      "BTC",
      "USDT"
    ],
    "HBAR": [
      "USDT",
      "BTC"
    ],
    "ZEC": [
      "USDT",
      "BTC"
    ],
    "NEO": [
      "BTC",
      "USDT"
    ],
    "SKY": [
      "USDT"
    ],
    "DOT": [
      "BTC",
      "USDT"
    ],
    "FRAX": [
      "USDT"
    ],
    "1INCH": [
      "USDT"
    ],
    "NEXO": [
      "USDT",
      "BTC"
    ],
    "BTC": [
      "GBP",
      "USD",
      "EUR",
      "USDT",
      "USDC"
    ],
    "YFI": [
      "BTC",
      "USDT"
    ],
    "POL": [
      "USDT",
      "BTC"
    ],
    "ARB": [
      "USDT"
    ],
    "ALPACA": [
      "USDT",
      "BTC"
    ],
    "USDC": [
      "USDT"
    ],
    "ONE": [
      "USDT"
    ],
    "SAND": [
      "USDT",
      "BTC"
    ],
    "ATOM": [
      "BTC",
      "USDT"
    ],
    "ENJ": [
      "USDT",
      "BTC"
    ],
    "WAVES": [
      "USDT",
      "BTC"
    ],
    "UNI": [
      "BTC",
      "USDT"
    ],
    "OMG": [
      "BTC",
      "USDT"
    ],
    "LINK": [
      "BTC",
      "USDT"
    ],
    "GALA": [
      "BTC",
      "USDT"
    ],
    "YGG": [
      "BTC"
    ],
    "HIFI": [
      "USDT"
    ],
    "SOL": [
      "ETH",
      "BTC",
      "USDT"
    ],
    "ZRX": [
      "USDT",
      "BTC"
    ],
    "MANA": [
      "USDT",
      "BTC"
    ],
    "KNC": [
      "BTC"
    ],
    "AVAX": [
      "USDT",
      "BTC"
    ],
    "ADA": [
      "USDT",
      "BTC",
      "ETH"
    ],
    "PYTH": [
      "USDT"
    ],
    "ETC": [
      "USDT"
    ],
    "LUNA": [
      "USDT"
    ],
    "LTC": [
      "BTC",
      "USDT"
    ],
    "COMP": [
      "USDT",
      "BTC"
    ],
    "BNB": [
      "USDT",
      "BTC"
    ],
    "FIL": [
      "USDT",
      "BTC"
    ],
    "LUNC": [
      "USDT",
      "BTC"
    ],
    "APT": [
      "USDT"
    ],
    "ETHW": [
      "USDT"
    ],
    "ICP": [
      "USDT"
    ],
    "XEM": [
      "USDT",
      "BTC"
    ],
    "BCUG": [
      "USDT"
    ],
    "XEC": [
      "USDT"
    ],
    "FTT": [
      "BTC",
      "USDT"
    ],
    "VET": [
      "USDT",
      "BTC"
    ],
    "QNT": [
      "USDT"
    ],
    "GMX": [
      "USDT"
    ],
    "STX": [
      "USDT"
    ]
  },
  "...": "(171 more fields)"
}
```

## Response Schema

**Top-level keys**: `aax`, `ABCC`, `ACX`, `AidosMarket`, `alphaex`, `archax`, `ascendex`, `ataix`, `backpack`, `bequant`, `Bgogo`, `Bibox`, `BigONE`, `bilaxy`, `Binance`, `binanceusa`, `bingx`, `BitSquare`, `bit`, `Bit2C`, `bit2me`, `BitBank`, `BitBay`, `bitbns`, `bitbuy`, `bitci`, `BitexBook`, `bitfex`, `Bitfinex`, `bitFlyer`, `bitflyereu`, `bitFlyerFX`, `bitflyerus`, `Bitforex`, `bitget`, `bithumbglobal`, `Bithumb`, `bitinka`, `Bitkub`, `BitMart`, `Bitmex`, `bitopro`, `bitpanda`, `bitrue`, `Bitso`, `Bitstamp`, `BitTrex`, `bitunix`, `bitvavo`, `bkex`, `Blackturtle`, `Bleutrade`, `blockchaincom`, `BTCAlpha`, `BTCBOX`, `btcex`, `BTCMarkets`, `BTCTurk`, `btse`, `Buda`, `bullish`, `buyucoin`, `bwexchange`, `bybit`, `bydfi`, `Catex`, `Cexio`, `Coinbase`, `coinbaseinternational`, `Coincheck`, `CoinCorner`, `coindcx`, `CoinDeal`, `CoinEx`, `CoinFalcon`, `coinfield`, `CoinJar`, `Coinmate`, `Coinone`, `Coinsbit`, `coinspro`, `CoinTiger`, `coinw`, `coss`, `crex24`, `crosstower`, `CryptoCarbon`, `cryptodotcom`, `cryptology`, `Cryptopia`, `Cryptsy`, `cube`, `currency`, `dcoin`, `DDEX`, `decoin`, `deribit`, `DigiFinex`, `edxmarkets`, `erisx`, `etoro`, `Exmo`, `fastex`, `FCoin`, `figuremarkets`, `flipster`, `Foxbit`, `ftx`, `ftxus`, `garantex`, `Gateio`, `Gemini`, `Globitex`, `gopax`, `Graviex`, `hashkey`, `HitBTC`, `huobijapan`, `HuobiPro`, `hyperliquid`, `IndependentReserve`, `indodax`, `indoex`, `inx`, `itBit`, `Korbit`, `Kraken`, `Kucoin`, `Kuna`, `LAToken`, `LBank`, `Liqnet`, `Liquid`, `litebit`, `lmax`, `Luno`, `Lykke`, `MercadoBitcoin`, `mercatox`, `mexc`, `mock`, `MtGox`, `NDAX`, `nominex`, `OKCoin`, `OKEX`, `onetrading`, `osl`, `oslhongkong`, `P2PB2B`, `pancakeswap`, `paramountdax`, `paribu`, `phemex`, `Poloniex`, `probit`, `safetrade`, `sigenpro`, `TheRockTrading`, `tidefi`, `timex`, `Tokenomy`, `toobit`, `tradeogre`, `uniswap`, `Unocoin`, `Upbit`, `valr`, `vitex`, `wazirx`, `whitebit`, `woo`, `xcoex`, `xtpub`, `yellow`, `Yobit`, `Zaif`, `zbdotcom`, `ZBG`, `zebitex`, `zonda`

## Performance

**Average Response Time**: 1164.05ms  
**Min Response Time**: 1164.05ms  
**Max Response Time**: 1164.05ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 1164.05ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
