# Top Total Top Tier Volume

**Endpoint**: `/data/top/volume/tier`  
**Category**: Helper  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Streaming/topTotalTopTierVolumeEndpoint](https://developers.coindesk.com/documentation/legacy/Streaming/topTotalTopTierVolumeEndpoint)

## Description

Helper endpoint for top tier volumes

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
curl -X GET "https://min-api.cryptocompare.com/data/top/volume/tier"
```

### Python

```python
import requests

# Endpoint: /data/top/volume/tier
url = "https://min-api.cryptocompare.com/data/top/volume/tier"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/top/volume/tier
const url = "https://min-api.cryptocompare.com/data/top/volume/tier";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "Path does not exist",
  "Type": 0,
  "Data": {}
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `Type`, `Data`

**Data object keys**: 

## Performance

**Average Response Time**: 669.06ms  
**Min Response Time**: 669.06ms  
**Max Response Time**: 669.06ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 669.06ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
