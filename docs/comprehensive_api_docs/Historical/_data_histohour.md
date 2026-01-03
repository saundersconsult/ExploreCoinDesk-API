# Hourly Historical OHLCV

**Endpoint**: `/data/histohour`  
**Category**: Historical  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Historical/dataHistohour](https://developers.coindesk.com/documentation/legacy/Historical/dataHistohour)

## Description

Get hourly historical OHLCV data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `tsym` | string | TBD | TBD |
| `limit` | string | TBD | TBD |
| `aggregate` | string | TBD | TBD |
| `toTs` | string | TBD | TBD |
| `e` | string | TBD | TBD |

## Test Results

**Total Tests**: 6  
**Successful**: 6  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=10"
```

### Python

```python
import requests

# Endpoint: /data/histohour
url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=10"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - fsym: BTC
# - tsym: USD
# - limit: 10
```

### JavaScript

```javascript
// Endpoint: /data/histohour
const url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=10";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Success",
  "Type": 100,
  "Aggregated": false,
  "TimeTo": 1767409200,
  "TimeFrom": 1767373200,
  "FirstValueInArray": true,
  "ConversionType": {
    "type": "direct",
    "conversionSymbol": ""
  },
  "Data": [
    {
      "time": 1767373200,
      "high": 90940.54,
      "low": 90153.46,
      "open": 90340.08,
      "volumefrom": 3748.45,
      "volumeto": 339568834.51,
      "close": 90341.35,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767376800,
      "high": 90530.81,
      "low": 89510.4,
      "open": 90341.35,
      "volumefrom": 2325.23,
      "volumeto": 209404991.87,
      "close": 89730.38,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767380400,
      "high": 90121.63,
      "low": 89614.03,
      "open": 89730.38,
      "volumefrom": 1762.44,
      "volumeto": 158424936.28,
      "close": 89857.78,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767384000,
      "high": 90046.55,
      "low": 89584.74,
      "open": 89857.78,
      "volumefrom": 1648.08,
      "volumeto": 148052048.2,
      "close": 89705.49,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767387600,
      "high": 90130.35,
      "low": 89703.17,
      "open": 89705.49,
      "volumefrom": 686.41,
      "volumeto": 61699985.72,
      "close": 90027.76,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767391200,
      "high": 90376.37,
      "low": 89986.1,
      "open": 90027.76,
      "volumefrom": 550.45,
      "volumeto": 49626179.1,
      "close": 90165.77,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767394800,
      "high": 90168.68,
      "low": 89866.13,
      "open": 90165.77,
      "volumefrom": 403.79,
      "volumeto": 36332231.75,
      "close": 89959.25,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767398400,
      "high": 90160.18,
      "low": 89930.34,
      "open": 89959.25,
      "volumefrom": 340.73,
      "volumeto": 30680039.95,
      "close": 90126.3,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767402000,
      "high": 90265.79,
      "low": 90044.1,
      "open": 90126.3,
      "volumefrom": 354.66,
      "volumeto": 31973974.75,
      "close": 90247.55,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767405600,
      "high": 90375.05,
      "low": 90102.61,
      "open": 90247.55,
      "volumefrom": 386.43,
      "volumeto": 34859456.6,
      "close": 90301.9,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767409200,
      "high": 90328.39,
      "low": 90166.62,
      "open": 90301.9,
      "volumefrom": 121.89,
      "volumeto": 10996480.29,
      "close": 90175.54,
      "conversionType": "direct",
      "conversionSymbol": ""
    }
  ],
  "RateLimit": {},
  "HasWarning": false
}
```

## Response Schema

**Top-level keys**: `Response`, `Type`, `Aggregated`, `TimeTo`, `TimeFrom`, `FirstValueInArray`, `ConversionType`, `Data`, `RateLimit`, `HasWarning`

**Data items**: 11

## Performance

**Average Response Time**: 670.49ms  
**Min Response Time**: 661.65ms  
**Max Response Time**: 682.68ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC, tsym=USD, limit=10 | ✅ Success | 682.68ms |
| 2 | fsym=BTC, tsym=USD, limit=100 | ✅ Success | 661.65ms |
| 3 | fsym=ETH, tsym=USD, limit=30 | ✅ Success | 662.3ms |
| 4 | fsym=BTC, tsym=USD, limit=7, aggregate=1 | ✅ Success | 670.53ms |
| 5 | fsym=BTC, tsym=USD, toTs=1767324890 | ✅ Success | 670.32ms |
| 6 | fsym=BTC, tsym=USD, toTs=1766806490, limit=7 | ✅ Success | 675.48ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
