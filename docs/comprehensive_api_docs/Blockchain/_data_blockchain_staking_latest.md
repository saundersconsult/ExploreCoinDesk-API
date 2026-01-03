# Staking Rate Latest

**Endpoint**: `/data/blockchain/staking/latest`  
**Category**: Blockchain  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Blockchain/dataStakingRateLatest](https://developers.coindesk.com/documentation/legacy/Blockchain/dataStakingRateLatest)

## Description

Latest staking rate data for coins

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
curl -X GET "https://min-api.cryptocompare.com/data/blockchain/staking/latest?fsym=BTC"
```

### Python

```python
import requests

# Endpoint: /data/blockchain/staking/latest
url = "https://min-api.cryptocompare.com/data/blockchain/staking/latest?fsym=BTC"

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
// Endpoint: /data/blockchain/staking/latest
const url = "https://min-api.cryptocompare.com/data/blockchain/staking/latest?fsym=BTC";

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

**Average Response Time**: 683.97ms  
**Min Response Time**: 672.06ms  
**Max Response Time**: 696.15ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC | ✅ Success | 683.69ms |
| 2 | fsym=ETH | ✅ Success | 696.15ms |
| 3 | fsym=XRP | ✅ Success | 672.06ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
