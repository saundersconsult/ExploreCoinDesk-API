# Top Price

**Endpoint**: `/data/top/price`  
**Category**: Helper  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Streaming/TopPriceEndpoint](https://developers.coindesk.com/documentation/legacy/Streaming/TopPriceEndpoint)

## Description

Helper endpoint for top prices

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tsym` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/top/price"
```

### Python

```python
import requests

# Endpoint: /data/top/price
url = "https://min-api.cryptocompare.com/data/top/price"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/top/price
const url = "https://min-api.cryptocompare.com/data/top/price";

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

**Average Response Time**: 1356.31ms  
**Min Response Time**: 1356.31ms  
**Max Response Time**: 1356.31ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 1356.31ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
