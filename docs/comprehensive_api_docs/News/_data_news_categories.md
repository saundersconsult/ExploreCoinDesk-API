# News Article Categories

**Endpoint**: `/data/news/categories`  
**Category**: News  
**Documentation**: [https://developers.coindesk.com/documentation/legacy/News/newsArticleCategoriesEndpoint](https://developers.coindesk.com/documentation/legacy/News/newsArticleCategoriesEndpoint)

## Description

List available news article categories

## Parameters

No parameters required.

## Test Results

**Total Tests**: 1  
**Successful**: 1  
**Failed**: 0  
**Success Rate**: 100.0%

## Example Usage

### cURL

```bash
curl -X GET "https://min-api.cryptocompare.com/data/news/categories"
```

### Python

```python
import requests

# Endpoint: /data/news/categories
url = "https://min-api.cryptocompare.com/data/news/categories"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### JavaScript

```javascript
// Endpoint: /data/news/categories
const url = "https://min-api.cryptocompare.com/data/news/categories";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Example Response

```json
[
  {
    "categoryName": "1INCH",
    "wordsAssociatedWithCategory": [
      "1INCH"
    ],
    "includedPhrases": [
      "1INCH NETWORK"
    ]
  },
  {
    "categoryName": "AAVE",
    "wordsAssociatedWithCategory": [
      "AAVE"
    ],
    "includedPhrases": [
      "AAVE PROTOCOL"
    ]
  },
  {
    "categoryName": "ADA",
    "wordsAssociatedWithCategory": [
      "ADA",
      "Cardano",
      "cardano"
    ]
  }
]
// ... (184 more items)
```

## Response Schema

## Performance

**Average Response Time**: 695.34ms  
**Min Response Time**: 695.34ms  
**Max Response Time**: 695.34ms  

## Tested Parameter Combinations

| Test # | Parameters | Status | Response Time |
|--------|------------|--------|---------------|
| 1 | None | ✅ Success | 695.34ms |

---

*Generated on 2026-01-02 19:40:52 from deep discovery results*
