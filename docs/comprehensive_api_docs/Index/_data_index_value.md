# MVIS Index Value

**Endpoint**: `/data/index/value`  
**Category**: Index  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Index/mvisIndexValue](https://developers.coindesk.com/documentation/legacy/Index/mvisIndexValue)

## Description

Get MVIS crypto index value

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `index_id` | string | TBD | TBD |
| `tsym` | string | TBD | TBD |

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/index/value?index_id=1"
```

### Python

```python
import requests

# Endpoint: /data/index/value
url = "https://min-api.cryptocompare.com/data/index/value?index_id=1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - index_id: 1
```

### JavaScript

```javascript
// Endpoint: /data/index/value
const url = "https://min-api.cryptocompare.com/data/index/value?index_id=1";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "indexName is a required param.",
  "HasWarning": false,
  "Type": 2,
  "RateLimit": {},
  "Data": {},
  "ParamWithError": "indexName"
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`, `ParamWithError`

**Data object keys**: 

## Performance

**Average Response Time**: 949.73ms  
**Min Response Time**: 651.88ms  
**Max Response Time**: 1529.53ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | index_id=1 | ✅ Success | 667.79ms |
| 2 | index_id=2 | ✅ Success | 1529.53ms |
| 3 | index_id=3 | ✅ Success | 651.88ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
