# Top Total Volume

**Endpoint**: `/data/top/volumes`  
**Category**: Helper  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalVolumeEndpoint](https://developers.coindesk.com/documentation/legacy/Streaming/TopTotalVolumeEndpoint)

## Description

Helper endpoint for top total volumes

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
curl -X GET "https://min-api.cryptocompare.com/data/top/volumes"
```

### Python

```python
import requests

# Endpoint: /data/top/volumes
url = "https://min-api.cryptocompare.com/data/top/volumes"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/top/volumes
const url = "https://min-api.cryptocompare.com/data/top/volumes";

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

**Average Response Time**: 651.01ms  
**Min Response Time**: 651.01ms  
**Max Response Time**: 651.01ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 651.01ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
