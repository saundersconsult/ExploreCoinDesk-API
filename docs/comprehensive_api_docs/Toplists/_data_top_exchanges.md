# Top Exchanges by Pair

**Endpoint**: `/data/top/exchanges`  
**Category**: Toplists  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Toplists/topExchangesEndpoint](https://developers.coindesk.com/documentation/legacy/Toplists/topExchangesEndpoint)

## Description

Top exchanges for a specific trading pair

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fsym` | string | TBD | TBD |
| `tsym` | string | TBD | TBD |
| `limit` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/top/exchanges"
```

### Python

```python
import requests

# Endpoint: /data/top/exchanges
url = "https://min-api.cryptocompare.com/data/top/exchanges"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/top/exchanges
const url = "https://min-api.cryptocompare.com/data/top/exchanges";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "fsym is a required param.",
  "HasWarning": false,
  "Type": 2,
  "RateLimit": {},
  "Data": {},
  "ParamWithError": "fsym"
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`, `ParamWithError`

**Data object keys**: 

## Performance

**Average Response Time**: 654.74ms  
**Min Response Time**: 654.74ms  
**Max Response Time**: 654.74ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 654.74ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
