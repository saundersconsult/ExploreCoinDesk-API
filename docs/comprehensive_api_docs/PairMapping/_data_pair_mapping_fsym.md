# Pair Mapping by From Symbol

**Endpoint**: `/data/pair/mapping/fsym`  
**Category**: PairMapping  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingMappedSymbolEndpoint](https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingMappedSymbolEndpoint)

## Description

Get all trading pairs for a from symbol

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
curl -X GET "https://min-api.cryptocompare.com/data/pair/mapping/fsym"
```

### Python

```python
import requests

# Endpoint: /data/pair/mapping/fsym
url = "https://min-api.cryptocompare.com/data/pair/mapping/fsym"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/pair/mapping/fsym
const url = "https://min-api.cryptocompare.com/data/pair/mapping/fsym";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "You need a valid auth key or api key to access this endpoint",
  "HasWarning": false,
  "Type": 1,
  "RateLimit": {},
  "Data": {}
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

**Data object keys**: 

## Performance

**Average Response Time**: 674.90ms  
**Min Response Time**: 674.90ms  
**Max Response Time**: 674.90ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 674.9ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
