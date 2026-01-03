# Historical Hourly Social Stats

**Endpoint**: `/data/social/coin/histo/hour`  
**Category**: Social  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Social/historicalHourSocialStats](https://developers.coindesk.com/documentation/legacy/Social/historicalHourSocialStats)

## Description

Historical hourly social media statistics

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `coinId` | string | TBD | TBD |
| `limit` | string | TBD | TBD |

## Test Results

**Total Tests**: 2  
**Successful**: 2  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/social/coin/histo/hour?coinId=1"
```

### Python

```python
import requests

# Endpoint: /data/social/coin/histo/hour
url = "https://min-api.cryptocompare.com/data/social/coin/histo/hour?coinId=1"

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
// Endpoint: /data/social/coin/histo/hour
const url = "https://min-api.cryptocompare.com/data/social/coin/histo/hour?coinId=1";

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

**Average Response Time**: 1166.48ms  
**Min Response Time**: 1164.61ms  
**Max Response Time**: 1168.35ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | coinId=1 | ✅ Success | 1168.35ms |
| 2 | coinId=7605 | ✅ Success | 1164.61ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
