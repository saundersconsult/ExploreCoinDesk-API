# IntoTheBlock Trading Signals Latest

**Endpoint**: `/data/tradingsignals/intotheblock/latest`  
**Category**: TradingSignals  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/TradingSignals/tradingSignalsIntoTheBlockLatest](https://developers.coindesk.com/documentation/legacy/TradingSignals/tradingSignalsIntoTheBlockLatest)

## Description

Latest IntoTheBlock trading signals

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest"
```

### Python

```python
import requests

# Endpoint: /data/tradingsignals/intotheblock/latest
url = "https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/tradingsignals/intotheblock/latest
const url = "https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "fsym is a required param.",
  "HasWarning": false,
  "Type": 2,
  "RateLimit": {},
  "Data": {},
  "ParamWithError": "fsym"
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`, `ParamWithError`

**Data object keys**: 

## Performance

**Average Response Time**: 658.90ms  
**Min Response Time**: 658.90ms  
**Max Response Time**: 658.90ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 658.9ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
