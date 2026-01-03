# Top by Market Cap Full Data

**Endpoint**: `/data/top/mktcapfull`  
**Category**: Toplists  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalMktCapEndpointFull](https://developers.coindesk.com/documentation/legacy/Toplists/TopTotalMktCapEndpointFull)

## Description

Get top cryptocurrencies by market cap with full data

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tsym` | string | TBD | TBD |
| `limit` | string | TBD | TBD |
| `page` | string | TBD | TBD |

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/top/mktcapfull"
```

### Python

```python
import requests

# Endpoint: /data/top/mktcapfull
url = "https://min-api.cryptocompare.com/data/top/mktcapfull"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/top/mktcapfull
const url = "https://min-api.cryptocompare.com/data/top/mktcapfull";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
{
  "Response": "Error",
  "Message": "tsym is a required param.",
  "HasWarning": false,
  "Type": 2,
  "RateLimit": {},
  "Data": {},
  "ParamWithError": "tsym"
}
```

## Response Schema

**Top-level keys**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`, `ParamWithError`

**Data object keys**: 

## Performance

**Average Response Time**: 664.67ms  
**Min Response Time**: 664.67ms  
**Max Response Time**: 664.67ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 664.67ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
