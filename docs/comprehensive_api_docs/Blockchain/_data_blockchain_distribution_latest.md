# Balance Distribution Latest

**Endpoint**: `/data/blockchain/distribution/latest`  
**Category**: Blockchain  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionLatest](https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionLatest)

## Description

Latest wallet balance distribution data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/blockchain/distribution/latest?fsym=BTC"
```

### Python

```python
import requests

# Endpoint: /data/blockchain/distribution/latest
url = "https://min-api.cryptocompare.com/data/blockchain/distribution/latest?fsym=BTC"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - fsym: BTC
```

### JavaScript

```javascript
// Endpoint: /data/blockchain/distribution/latest
const url = "https://min-api.cryptocompare.com/data/blockchain/distribution/latest?fsym=BTC";

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

**Average Response Time**: 665.40ms  
**Min Response Time**: 650.60ms  
**Max Response Time**: 683.35ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC | ✅ Success | 683.35ms |
| 2 | fsym=ETH | ✅ Success | 662.26ms |
| 3 | fsym=XRP | ✅ Success | 650.6ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
