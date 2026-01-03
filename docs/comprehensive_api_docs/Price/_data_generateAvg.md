# Generate Average

**Endpoint**: `/data/generateAvg`  
**Category**: Price  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Price/generateAverageEndpoint](https://developers.coindesk.com/documentation/legacy/Price/generateAverageEndpoint)

## Description

Get weighted average price across exchanges

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `tsym` | string | TBD | TBD |
| `e` | string | TBD | TBD |
| `extraParams` | string | TBD | TBD |
| `sign` | string | TBD | TBD |

## Test Results

**Total Tests**: 4  
**Successful**: 4  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsyms=USD"
```

### Python

```python
import requests

# Endpoint: /data/generateAvg
url = "https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsyms=USD"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - fsym: BTC
# - tsyms: USD
```

### JavaScript

```javascript
// Endpoint: /data/generateAvg
const url = "https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsyms=USD";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "tsym is a required param.",
  "HasWarning": false,
  "Type": 2,
  "RateLimit": {},
  "Data": {},
  "ParamWithError": "tsym"
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`, `ParamWithError`

**Data object keys**: 

## Performance

**Average Response Time**: 668.49ms  
**Min Response Time**: 660.93ms  
**Max Response Time**: 683.35ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC, tsyms=USD | ✅ Success | 660.93ms |
| 2 | fsym=ETH, tsyms=USD,EUR,GBP | ✅ Success | 683.35ms |
| 3 | fsym=BTC, tsyms=USD, e=Coinbase | ✅ Success | 665.5ms |
| 4 | fsym=BTC, tsyms=USD, e=Binance | ✅ Success | 664.17ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
