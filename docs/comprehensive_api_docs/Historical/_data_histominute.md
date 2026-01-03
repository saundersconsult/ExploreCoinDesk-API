# Minute Historical OHLCV

**Endpoint**: `/data/histominute`  
**Category**: Historical  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Historical/dataHistominute](https://developers.coindesk.com/documentation/legacy/Historical/dataHistominute)

## Description

Get minute-level historical OHLCV data

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
curl -X GET "https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=10"
```

### Python

```python
import requests

# Endpoint: /data/histominute
url = "https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=10"

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
// Endpoint: /data/histominute
const url = "https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=10";

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
  "TimeTo": 1767411240,
  "TimeFrom": 1767410640,
  "FirstValueInArray": true,
  "ConversionType": {
    "type": "direct",
    "conversionSymbol": ""
  },
  "Data": [
    {
      "time": 1767410640,
      "high": 90202.93,
      "low": 90193.48,
      "open": 90201.83,
      "volumefrom": 1.545,
      "volumeto": 139243.77,
      "close": 90193.8,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767410700,
      "high": 90195.44,
      "low": 90184.54,
      "open": 90193.8,
      "volumefrom": 2.006,
      "volumeto": 180852.33,
      "close": 90184.54,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767410760,
      "high": 90184.54,
      "low": 90173.44,
      "open": 90184.54,
      "volumefrom": 0.8373,
      "volumeto": 75512.84,
      "close": 90173.46,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767410820,
      "high": 90173.85,
      "low": 90171.78,
      "open": 90173.46,
      "volumefrom": 0.5864,
      "volumeto": 52849.55,
      "close": 90173.68,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767410880,
      "high": 90173.68,
      "low": 90167.35,
      "open": 90173.68,
      "volumefrom": 1.946,
      "volumeto": 175413.28,
      "close": 90167.35,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767410940,
      "high": 90186.11,
      "low": 90166.62,
      "open": 90167.35,
      "volumefrom": 2.028,
      "volumeto": 182895.34,
      "close": 90185.81,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767411000,
      "high": 90203.85,
      "low": 90185.81,
      "open": 90185.81,
      "volumefrom": 7.366,
      "volumeto": 664351.83,
      "close": 90203.53,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767411060,
      "high": 90221.18,
      "low": 90203.43,
      "open": 90203.53,
      "volumefrom": 2.273,
      "volumeto": 205043.14,
      "close": 90205.15,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767411120,
      "high": 90205.15,
      "low": 90194.35,
      "open": 90205.15,
      "volumefrom": 1.451,
      "volumeto": 130894.91,
      "close": 90194.35,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767411180,
      "high": 90194.35,
      "low": 90176.11,
      "open": 90194.35,
      "volumefrom": 2.595,
      "volumeto": 234041.81,
      "close": 90177.26,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767411240,
      "high": 90177.26,
      "low": 90175.41,
      "open": 90177.26,
      "volumefrom": 0,
      "volumeto": 0,
      "close": 90175.41,
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

**Average Response Time**: 908.92ms  
**Min Response Time**: 661.51ms  
**Max Response Time**: 1294.86ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC, tsym=USD, limit=10 | ✅ Success | 1294.86ms |
| 2 | fsym=BTC, tsym=USD, limit=100 | ✅ Success | 1013.65ms |
| 3 | fsym=ETH, tsym=USD, limit=30 | ✅ Success | 687.76ms |
| 4 | fsym=BTC, tsym=USD, limit=7, aggregate=1 | ✅ Success | 674.54ms |
| 5 | fsym=BTC, tsym=USD, toTs=1767324897 | ✅ Success | 1121.18ms |
| 6 | fsym=BTC, tsym=USD, toTs=1766806497, limit=7 | ✅ Success | 661.51ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
