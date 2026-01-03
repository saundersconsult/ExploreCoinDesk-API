# Planned Pair Remapping

**Endpoint**: `/data/pair/remapping/planned`  
**Category**: PairMapping  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/PairMapping/plannedPairRemappingEndpoint](https://developers.coindesk.com/documentation/legacy/PairMapping/plannedPairRemappingEndpoint)

## Description

Get planned pair remapping updates

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
curl -X GET "https://min-api.cryptocompare.com/data/pair/remapping/planned"
```

### Python

```python
import requests

# Endpoint: /data/pair/remapping/planned
url = "https://min-api.cryptocompare.com/data/pair/remapping/planned"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/pair/remapping/planned
const url = "https://min-api.cryptocompare.com/data/pair/remapping/planned";

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

**Average Response Time**: 664.46ms  
**Min Response Time**: 664.46ms  
**Max Response Time**: 664.46ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 664.46ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
