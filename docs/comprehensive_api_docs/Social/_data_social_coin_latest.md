# Latest Coin Social Stats

**Endpoint**: `/data/social/coin/latest`  
**Category**: Social  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Social/latestCoinSocialStats](https://developers.coindesk.com/documentation/legacy/Social/latestCoinSocialStats)

## Description

Get latest social media statistics for a coin

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `coinId` | string | TBD | TBD |

## Test Results

**Total Tests**: 2  
**Successful**: 2  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/social/coin/latest?coinId=1"
```

### Python

```python
import requests

# Endpoint: /data/social/coin/latest
url = "https://min-api.cryptocompare.com/data/social/coin/latest?coinId=1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Parameters used:
# - coinId: 1
```

### JavaScript

```javascript
// Endpoint: /data/social/coin/latest
const url = "https://min-api.cryptocompare.com/data/social/coin/latest?coinId=1";

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

**Average Response Time**: 668.95ms  
**Min Response Time**: 661.30ms  
**Max Response Time**: 676.60ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | coinId=1 | ✅ Success | 676.6ms |
| 2 | coinId=7605 | ✅ Success | 661.3ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
