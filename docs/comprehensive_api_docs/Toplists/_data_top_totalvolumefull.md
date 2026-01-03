# Top by Total Volume Full Data

**Endpoint**: `/data/top/totalvolumefull`  
**Category**: Toplists  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalVolumeEndpointFull](https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalVolumeEndpointFull)

## Description

Get top cryptocurrencies by total trading volume with full data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tsym` | string | TBD | TBD |
| `limit` | string | TBD | TBD |
| `page` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/top/totalvolumefull"
```

### Python

```python
import requests

# Endpoint: /data/top/totalvolumefull
url = "https://min-api.cryptocompare.com/data/top/totalvolumefull"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/top/totalvolumefull
const url = "https://min-api.cryptocompare.com/data/top/totalvolumefull";

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

**Average Response Time**: 681.28ms  
**Min Response Time**: 681.28ms  
**Max Response Time**: 681.28ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 681.28ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
