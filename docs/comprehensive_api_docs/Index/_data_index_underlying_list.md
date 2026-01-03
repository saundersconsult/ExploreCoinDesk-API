# List of Underlying Indices

**Endpoint**: `/data/index/underlying/list`  
**Category**: Index  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Index/listOfUnderlyingIndices](https://developers.coindesk.com/documentation/legacy/Index/listOfUnderlyingIndices)

## Description

List underlying indices that make up composite indices

## Parameters

No parameters required.

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/index/underlying/list"
```

### Python

```python
import requests

# Endpoint: /data/index/underlying/list
url = "https://min-api.cryptocompare.com/data/index/underlying/list"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/index/underlying/list
const url = "https://min-api.cryptocompare.com/data/index/underlying/list";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Success",
  "Message": "",
  "HasWarning": false,
  "Type": 100,
  "RateLimit": {},
  "Data": {}
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

**Data object keys**: 

## Performance

**Average Response Time**: 681.47ms  
**Min Response Time**: 681.47ms  
**Max Response Time**: 681.47ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 681.47ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
