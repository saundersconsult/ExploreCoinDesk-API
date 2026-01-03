# Latest Blockchain Data

**Endpoint**: `/data/blockchain/latest`  
**Category**: Blockchain  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainLatest](https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainLatest)

## Description

Get latest blockchain statistics for a coin

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
curl -X GET "https://min-api.cryptocompare.com/data/blockchain/latest?fsym=BTC"
```

### Python

```python
import requests

# Endpoint: /data/blockchain/latest
url = "https://min-api.cryptocompare.com/data/blockchain/latest?fsym=BTC"

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
// Endpoint: /data/blockchain/latest
const url = "https://min-api.cryptocompare.com/data/blockchain/latest?fsym=BTC";

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

**Average Response Time**: 720.51ms  
**Min Response Time**: 662.89ms  
**Max Response Time**: 829.39ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC | ✅ Success | 669.24ms |
| 2 | fsym=ETH | ✅ Success | 662.89ms |
| 3 | fsym=XRP | ✅ Success | 829.39ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
