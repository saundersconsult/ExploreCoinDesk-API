# Balance Distribution Daily

**Endpoint**: `/data/blockchain/distribution/day`  
**Category**: Blockchain  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionDay](https://developers.coindesk.com/documentation/legacy/Blockchain/balanceDistributionDay)

## Description

Historical daily balance distribution data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `limit` | string | TBD | TBD |

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/blockchain/distribution/day?fsym=BTC"
```

### Python

```python
import requests

# Endpoint: /data/blockchain/distribution/day
url = "https://min-api.cryptocompare.com/data/blockchain/distribution/day?fsym=BTC"

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
// Endpoint: /data/blockchain/distribution/day
const url = "https://min-api.cryptocompare.com/data/blockchain/distribution/day?fsym=BTC";

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

**Average Response Time**: 663.27ms  
**Min Response Time**: 657.64ms  
**Max Response Time**: 666.91ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC | ✅ Success | 665.27ms |
| 2 | fsym=ETH | ✅ Success | 657.64ms |
| 3 | fsym=XRP | ✅ Success | 666.91ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
