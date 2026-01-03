# Price at Specific Time

**Endpoint**: `/data/pricehistorical`  
**Category**: Historical  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Historical/dataPriceHistorical](https://developers.coindesk.com/documentation/legacy/Historical/dataPriceHistorical)

## Description

Get historical price at a specific timestamp

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `tsyms` | string | TBD | TBD |
| `ts` | string | TBD | TBD |
| `e` | string | TBD | TBD |

## Test Results

**Total Tests**: 6  
**Successful**: 6  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsym=USD&limit=10"
```

### Python

```python
import requests

# Endpoint: /data/pricehistorical
url = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsym=USD&limit=10"

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
// Endpoint: /data/pricehistorical
const url = "https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsym=USD&limit=10";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "tsyms is a required param.",
  "HasWarning": false,
  "Type": 2,
  "RateLimit": {},
  "Data": {},
  "ParamWithError": "tsyms"
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`, `ParamWithError`

**Data object keys**: 

## Performance

**Average Response Time**: 690.99ms  
**Min Response Time**: 664.99ms  
**Max Response Time**: 766.85ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC, tsym=USD, limit=10 | ✅ Success | 675.68ms |
| 2 | fsym=BTC, tsym=USD, limit=100 | ✅ Success | 696.06ms |
| 3 | fsym=ETH, tsym=USD, limit=30 | ✅ Success | 766.85ms |
| 4 | fsym=BTC, tsym=USD, limit=7, aggregate=1 | ✅ Success | 664.99ms |
| 5 | fsym=BTC, tsyms=USD, ts=1767324920 | ✅ Success | 674.48ms |
| 6 | fsym=ETH, tsyms=USD,EUR, ts=1766806520 | ✅ Success | 667.87ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
