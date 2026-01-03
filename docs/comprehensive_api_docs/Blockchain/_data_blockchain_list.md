# List of Blockchain Coins

**Endpoint**: `/data/blockchain/list`  
**Category**: Blockchain  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainListOfCoins](https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainListOfCoins)

## Description

List all cryptocurrencies with blockchain data available

## Parameters

No parameters required.

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/blockchain/list?fsym=BTC"
```

### Python

```python
import requests

# Endpoint: /data/blockchain/list
url = "https://min-api.cryptocompare.com/data/blockchain/list?fsym=BTC"

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
// Endpoint: /data/blockchain/list
const url = "https://min-api.cryptocompare.com/data/blockchain/list?fsym=BTC";

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

**Average Response Time**: 669.88ms  
**Min Response Time**: 658.77ms  
**Max Response Time**: 679.67ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC | ✅ Success | 658.77ms |
| 2 | fsym=ETH | ✅ Success | 679.67ms |
| 3 | fsym=XRP | ✅ Success | 671.21ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
