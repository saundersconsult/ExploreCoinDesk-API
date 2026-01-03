# Multiple Symbols Full Price

**Endpoint**: `/data/pricemultifull`  
**Category**: Price  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsFullPriceEndpoint](https://developers.coindesk.com/documentation/legacy/Price/multipleSymbolsFullPriceEndpoint)

## Description

Detailed price info including market data (high, low, volume, etc.)

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsyms` | string | TBD | TBD |
| `tsyms` | string | TBD | TBD |
| `e` | string | TBD | TBD |
| `tryConversion` | string | TBD | TBD |

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD"
```

### Python

```python
import requests

# Endpoint: /data/pricemultifull
url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - fsyms: BTC,ETH
# - tsyms: USD
```

### JavaScript

```javascript
// Endpoint: /data/pricemultifull
const url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "RAW": {
    "BTC": {
      "USD": {
        "TYPE": "5",
        "MARKET": "CCCAGG",
        "FROMSYMBOL": "BTC",
        "TOSYMBOL": "USD",
        "FLAGS": "2",
        "LASTMARKET": "CCCAGG",
        "MEDIAN": 90176.2230825884,
        "TOPTIERVOLUME24HOUR": 30885.72287551,
        "TOPTIERVOLUME24HOURTO": 2771230723.09418,
        "LASTTRADEID": "981225884",
        "PRICE": 90176.2230825884,
        "LASTUPDATE": 1767411267,
        "LASTVOLUME": 0.0006106,
        "LASTVOLUMETO": 55.0687928,
        "VOLUMEHOUR": 117.58253959,
        "VOLUMEHOURTO": 10608021.3763152,
        "OPENHOUR": 90301.8974596708,
        "HIGHHOUR": 90328.3925335518,
        "LOWHOUR": 90166.6215801568,
        "VOLUMEDAY": 1199.40616347,
        "VOLUMEDAYTO": 108121492.674488,
        "OPENDAY": 89959.2467726096,
        "HIGHDAY": 90375.0504471023,
        "LOWDAY": 89930.3433564066,
        "VOLUME24HOUR": 30885.72287551,
        "VOLUME24HOURTO": 2771230723.09418,
        "OPEN24HOUR": 88846.1136412025,
        "HIGH24HOUR": 90940.5362669072,
        "LOW24HOUR": 88400.8971197111,
        "CHANGE24HOUR": 1330.10944138591,
        "CHANGEPCT24HOUR": 1.497093555220034,
        "CHANGEDAY": 216.9763099788106,
        "CHANGEPCTDAY": 0.24119400480004308,
        "CHANGEHOUR": -125.67437708239595,
        "CHANGEPCTHOUR": -0.13917135809745598,
        "CONVERSIONTYPE": "direct",
        "CONVERSIONSYMBOL": "",
        "CONVERSIONLASTUPDATE": 1767411267,
        "SUPPLY": 19970762,
        "MKTCAP": 1800887889241.2793,
        "MKTCAPPENALTY": 0,
        "CIRCULATINGSUPPLY": 19970762,
        "CIRCULATINGSUPPLYMKTCAP": 1800887889241.2793,
        "TOTALVOLUME24H": 255998.309703243,
        "TOTALVOLUME24HTO": 23071033571.570385,
        "TOTALTOPTIERVOLUME24H": 138218.597091567,
        "TOTALTOPTIERVOLUME24HTO": 12450103932.496738,
        "IMAGEURL": "/media/37746251/btc.png"
      }
    },
    "ETH": {
      "USD": {
        "TYPE": "5",
        "MARKET": "CCCAGG",
        "FROMSYMBOL": "ETH",
        "TOSYMBOL": "USD",
        "FLAGS": "2",
        "LASTMARKET": "CCCAGG",
        "MEDIAN": 3120.02994706168,
        "TOPTIERVOLUME24HOUR": 391174.04956232,
        "TOPTIERVOLUME24HOURTO": 1207826213.57055,
        "LASTTRADEID": "899812902",
        "PRICE": 3120.02994706168,
        "LASTUPDATE": 1767411267,
        "LASTVOLUME": 0.007661,
        "LASTVOLUMETO": 23.90063458,
        "VOLUMEHOUR": 2476.23344362,
        "VOLUMEHOURTO": 7731283.95243642,
        "OPENHOUR": 3125.17176756761,
        "HIGHHOUR": 3126.10926638166,
        "LOWHOUR": 3117.69725256488,
        "VOLUMEDAY": 20476.69015671,
        "VOLUMEDAYTO": 64014871.1515896,
        "OPENDAY": 3124.70953403863,
        "HIGHDAY": 3135.40521071927,
        "LOWDAY": 3117.69725256488,
        "VOLUME24HOUR": 391174.04956232,
        "VOLUME24HOURTO": 1207826213.57055,
        "OPEN24HOUR": 3019.37115688818,
        "HIGH24HOUR": 3148.96201674119,
        "LOW24HOUR": 3005.74633061256,
        "CHANGE24HOUR": 100.65879017350017,
        "CHANGEPCT24HOUR": 3.3337666998594826,
        "CHANGEDAY": -4.6795869769498495,
        "CHANGEPCTDAY": -0.14976070338613423,
        "CHANGEHOUR": -5.1418205059299,
        "CHANGEPCTHOUR": -0.16452921273930143,
        "CONVERSIONTYPE": "direct",
        "CONVERSIONSYMBOL": "",
        "CONVERSIONLASTUPDATE": 1767411267,
        "SUPPLY": 120694878.114886,
        "MKTCAP": 376571634175.4037,
        "MKTCAPPENALTY": 0,
        "CIRCULATINGSUPPLY": 120694878.114886,
        "CIRCULATINGSUPPLYMKTCAP": 376571634175.4037,
        "TOTALVOLUME24H": 3722946.78746227,
        "TOTALVOLUME24HTO": 11603056932.622078,
        "TOTALTOPTIERVOLUME24H": 2128522.11858004,
        "TOTALTOPTIERVOLUME24HTO": 6628404217.375619,
        "IMAGEURL": "/media/37746238/eth.png"
      }
    }
  },
  "DISPLAY": {
    "BTC": {
      "USD": {
        "FROMSYMBOL": "\u0243",
        "TOSYMBOL": "$",
        "MARKET": "CryptoCompare Index",
        "LASTMARKET": "CCCAGG",
        "TOPTIERVOLUME24HOUR": "\u0243 30,885.7",
        "TOPTIERVOLUME24HOURTO": "$ 2,771,230,723.1",
        "LASTTRADEID": "981225884",
        "PRICE": "$ 90,176.2",
        "LASTUPDATE": "Just now",
        "LASTVOLUME": "\u0243 0.0006106",
        "LASTVOLUMETO": "$ 55.07",
        "VOLUMEHOUR": "\u0243 117.58",
        "VOLUMEHOURTO": "$ 10,608,021.4",
        "OPENHOUR": "$ 90,301.9",
        "HIGHHOUR": "$ 90,328.4",
        "LOWHOUR": "$ 90,166.6",
        "VOLUMEDAY": "\u0243 1,199.41",
        "VOLUMEDAYTO": "$ 108,121,492.7",
        "OPENDAY": "$ 89,959.2",
        "HIGHDAY": "$ 90,375.1",
        "LOWDAY": "$ 89,930.3",
        "VOLUME24HOUR": "\u0243 30,885.7",
        "VOLUME24HOURTO": "$ 2,771,230,723.1",
        "OPEN24HOUR": "$ 88,846.1",
        "HIGH24HOUR": "$ 90,940.5",
        "LOW24HOUR": "$ 88,400.9",
        "CHANGE24HOUR": "$ 1,330.11",
        "CHANGEPCT24HOUR": "1.50",
        "CHANGEDAY": "$ 216.98",
        "CHANGEPCTDAY": "0.24",
        "CHANGEHOUR": "$ -125.67",
        "CHANGEPCTHOUR": "-0.14",
        "CONVERSIONTYPE": "direct",
        "CONVERSIONSYMBOL": "",
        "CONVERSIONLASTUPDATE": "Just now",
        "SUPPLY": "\u0243 19,970,762.0",
        "MKTCAP": "$ 1,800.89 B",
        "MKTCAPPENALTY": "0 %",
        "CIRCULATINGSUPPLY": "\u0243 19,970,762.0",
        "CIRCULATINGSUPPLYMKTCAP": "$ 1,800.89 B",
        "TOTALVOLUME24H": "\u0243 256.00 K",
        "TOTALVOLUME24HTO": "$ 23.07 B",
        "TOTALTOPTIERVOLUME24H": "\u0243 138.22 K",
        "TOTALTOPTIERVOLUME24HTO": "$ 12.45 B",
        "IMAGEURL": "/media/37746251/btc.png"
      }
    },
    "ETH": {
      "USD": {
        "FROMSYMBOL": "\u039e",
        "TOSYMBOL": "$",
        "MARKET": "CryptoCompare Index",
        "LASTMARKET": "CCCAGG",
        "TOPTIERVOLUME24HOUR": "\u039e 391,174.0",
        "TOPTIERVOLUME24HOURTO": "$ 1,207,826,213.6",
        "LASTTRADEID": "899812902",
        "PRICE": "$ 3,120.03",
        "LASTUPDATE": "Just now",
        "LASTVOLUME": "\u039e 0.007661",
        "LASTVOLUMETO": "$ 23.90",
        "VOLUMEHOUR": "\u039e 2,476.23",
        "VOLUMEHOURTO": "$ 7,731,284.0",
        "OPENHOUR": "$ 3,125.17",
        "HIGHHOUR": "$ 3,126.11",
        "LOWHOUR": "$ 3,117.70",
        "VOLUMEDAY": "\u039e 20,476.7",
        "VOLUMEDAYTO": "$ 64,014,871.2",
        "OPENDAY": "$ 3,124.71",
        "HIGHDAY": "$ 3,135.41",
        "LOWDAY": "$ 3,117.70",
        "VOLUME24HOUR": "\u039e 391,174.0",
        "VOLUME24HOURTO": "$ 1,207,826,213.6",
        "OPEN24HOUR": "$ 3,019.37",
        "HIGH24HOUR": "$ 3,148.96",
        "LOW24HOUR": "$ 3,005.75",
        "CHANGE24HOUR": "$ 100.66",
        "CHANGEPCT24HOUR": "3.33",
        "CHANGEDAY": "$ -4.68",
        "CHANGEPCTDAY": "-0.15",
        "CHANGEHOUR": "$ -5.14",
        "CHANGEPCTHOUR": "-0.16",
        "CONVERSIONTYPE": "direct",
        "CONVERSIONSYMBOL": "",
        "CONVERSIONLASTUPDATE": "Just now",
        "SUPPLY": "\u039e 120,694,878.1",
        "MKTCAP": "$ 376.57 B",
        "MKTCAPPENALTY": "0 %",
        "CIRCULATINGSUPPLY": "\u039e 120,694,878.1",
        "CIRCULATINGSUPPLYMKTCAP": "$ 376.57 B",
        "TOTALVOLUME24H": "\u039e 3.72 M",
        "TOTALVOLUME24HTO": "$ 11.60 B",
        "TOTALTOPTIERVOLUME24H": "\u039e 2.13 M",
        "TOTALTOPTIERVOLUME24HTO": "$ 6.63 B",
        "IMAGEURL": "/media/37746238/eth.png"
      }
    }
  }
}
```

## Response Schema

**Top-level keys**: `RAW`, `DISPLAY`

## Performance

**Average Response Time**: 679.00ms  
**Min Response Time**: 672.03ms  
**Max Response Time**: 684.79ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsyms=BTC,ETH, tsyms=USD | ✅ Success | 672.03ms |
| 2 | fsyms=BTC,ETH,XRP, tsyms=USD,EUR | ✅ Success | 680.17ms |
| 3 | fsyms=BTC, tsyms=USD, e=CCCAGG | ✅ Success | 684.79ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
