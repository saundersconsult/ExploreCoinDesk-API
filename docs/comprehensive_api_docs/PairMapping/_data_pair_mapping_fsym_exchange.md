# Pair Mapping by Symbol and Exchange

**Endpoint**: `/data/pair/mapping/fsym/exchange`  
**Category**: PairMapping  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingExchangeSymbolEndpoint](https://developers.coindesk.com/documentation/legacy/PairMapping/pairMappingExchangeSymbolEndpoint)

## Description

Get trading pairs for a symbol on a specific exchange

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `e` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/pair/mapping/fsym/exchange"
```

### Python

```python
import requests

# Endpoint: /data/pair/mapping/fsym/exchange
url = "https://min-api.cryptocompare.com/data/pair/mapping/fsym/exchange"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/pair/mapping/fsym/exchange
const url = "https://min-api.cryptocompare.com/data/pair/mapping/fsym/exchange";

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

**Average Response Time**: 659.52ms  
**Min Response Time**: 659.52ms  
**Max Response Time**: 659.52ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 659.52ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
