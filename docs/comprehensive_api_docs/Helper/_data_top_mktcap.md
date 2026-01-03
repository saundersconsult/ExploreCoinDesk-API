# Top Market Cap

**Endpoint**: `/data/top/mktcap`  
**Category**: Helper  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalMktCapEndpoint](https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalMktCapEndpoint)

## Description

Helper endpoint for top market caps

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
curl -X GET "https://min-api.cryptocompare.com/data/top/mktcap"
```

### Python

```python
import requests

# Endpoint: /data/top/mktcap
url = "https://min-api.cryptocompare.com/data/top/mktcap"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/top/mktcap
const url = "https://min-api.cryptocompare.com/data/top/mktcap";

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

**Average Response Time**: 666.54ms  
**Min Response Time**: 666.54ms  
**Max Response Time**: 666.54ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 666.54ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
