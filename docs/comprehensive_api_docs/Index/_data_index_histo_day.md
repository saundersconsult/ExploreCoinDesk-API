# MVIS Historical Day Data

**Endpoint**: `/data/index/histo/day`  
**Category**: Index  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Index/mvisHistoDay](https://developers.coindesk.com/documentation/legacy/Index/mvisHistoDay)

## Description

MVIS index daily historical data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `index_id` | string | TBD | TBD |
| `limit` | string | TBD | TBD |

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/index/histo/day?index_id=1"
```

### Python

```python
import requests

# Endpoint: /data/index/histo/day
url = "https://min-api.cryptocompare.com/data/index/histo/day?index_id=1"

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
// Endpoint: /data/index/histo/day
const url = "https://min-api.cryptocompare.com/data/index/histo/day?index_id=1";

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

**Average Response Time**: 824.25ms  
**Min Response Time**: 677.76ms  
**Max Response Time**: 1106.49ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | index_id=1 | ✅ Success | 1106.49ms |
| 2 | index_id=2 | ✅ Success | 688.5ms |
| 3 | index_id=3 | ✅ Success | 677.76ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
