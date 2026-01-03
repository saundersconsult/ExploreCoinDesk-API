# Daily Historical OHLCV

**Endpoint**: `/data/histoday`  
**Category**: Historical  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Historical/dataHistoday](https://developers.coindesk.com/documentation/legacy/Historical/dataHistoday)

## Description

Get daily historical OHLCV data

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
curl -X GET "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10"
```

### Python

```python
import requests

# Endpoint: /data/histoday
url = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10"

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
// Endpoint: /data/histoday
const url = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10";

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
  "TimeTo": 1767398400,
  "TimeFrom": 1766534400,
  "FirstValueInArray": true,
  "ConversionType": {
    "type": "direct",
    "conversionSymbol": ""
  },
  "Data": [
    {
      "time": 1766534400,
      "high": 88003.03,
      "low": 86365.36,
      "open": 87440.81,
      "volumefrom": 16558.92,
      "volumeto": 1443982911.33,
      "close": 87620.12,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1766620800,
      "high": 88545.97,
      "low": 86913.66,
      "open": 87620.12,
      "volumefrom": 8950.93,
      "volumeto": 785512556.31,
      "close": 87183.32,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1766707200,
      "high": 89503.42,
      "low": 86589.77,
      "open": 87183.32,
      "volumefrom": 24423.76,
      "volumeto": 2146285656.23,
      "close": 87315.1,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1766793600,
      "high": 87925.14,
      "low": 87154.06,
      "open": 87315.1,
      "volumefrom": 4960.63,
      "volumeto": 433943569.04,
      "close": 87823.31,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1766880000,
      "high": 88018.43,
      "low": 87381.32,
      "open": 87823.31,
      "volumefrom": 5733.05,
      "volumeto": 502876455.57,
      "close": 87886.81,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1766966400,
      "high": 90327.16,
      "low": 86704.68,
      "open": 87886.81,
      "volumefrom": 30609.16,
      "volumeto": 2698231723.66,
      "close": 87133.26,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767052800,
      "high": 89341.34,
      "low": 86732.68,
      "open": 87133.26,
      "volumefrom": 22736.07,
      "volumeto": 2002631036.31,
      "close": 88410.54,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767139200,
      "high": 89105.68,
      "low": 87109.45,
      "open": 88410.54,
      "volumefrom": 18255.84,
      "volumeto": 1607399099.44,
      "close": 87519.13,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767225600,
      "high": 88806.59,
      "low": 87400.21,
      "open": 87519.13,
      "volumefrom": 9510.96,
      "volumeto": 835819448.91,
      "close": 88742.68,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767312000,
      "high": 90940.54,
      "low": 88289.33,
      "open": 88742.68,
      "volumefrom": 32178.91,
      "volumeto": 2884180579.57,
      "close": 89959.25,
      "conversionType": "direct",
      "conversionSymbol": ""
    },
    {
      "time": 1767398400,
      "high": 90375.05,
      "low": 89930.34,
      "open": 89959.25,
      "volumefrom": 1203.65,
      "volumeto": 108504584.74,
      "close": 90175.8,
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

**Average Response Time**: 738.59ms  
**Min Response Time**: 650.64ms  
**Max Response Time**: 885.39ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC, tsym=USD, limit=10 | ✅ Success | 885.39ms |
| 2 | fsym=BTC, tsym=USD, limit=100 | ✅ Success | 683.14ms |
| 3 | fsym=ETH, tsym=USD, limit=30 | ✅ Success | 650.64ms |
| 4 | fsym=BTC, tsym=USD, limit=7, aggregate=1 | ✅ Success | 681.49ms |
| 5 | fsym=BTC, tsym=USD, toTs=1767324882 | ✅ Success | 851.6ms |
| 6 | fsym=BTC, tsym=USD, toTs=1766806482, limit=7 | ✅ Success | 679.28ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
