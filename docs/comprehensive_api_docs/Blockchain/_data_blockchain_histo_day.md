# Daily Blockchain Historical Data

**Endpoint**: `/data/blockchain/histo/day`  
**Category**: Blockchain  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainDay](https://developers.coindesk.com/documentation/legacy/Blockchain/blockchainDay)

## Description

Historical daily blockchain data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `limit` | string | TBD | TBD |
| `toTs` | string | TBD | TBD |

## Test Results

**Total Tests**: 3  
**Successful**: 3  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym=BTC"
```

### Python

```python
import requests

# Endpoint: /data/blockchain/histo/day
url = "https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym=BTC"

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
// Endpoint: /data/blockchain/histo/day
const url = "https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym=BTC";

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

**Average Response Time**: 721.11ms  
**Min Response Time**: 669.42ms  
**Max Response Time**: 812.94ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | fsym=BTC | ✅ Success | 812.94ms |
| 2 | fsym=ETH | ✅ Success | 680.98ms |
| 3 | fsym=XRP | ✅ Success | 669.42ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
