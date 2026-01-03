# CryptoCompare MinAPI - Comprehensive Blockchain Data Documentation

**Discovery Date**: 2026-01-02 18:28:15

**Base URL**: `https://min-api.cryptocompare.com`

**API Key Required**: Not configured - limited access

---

## Discovery Summary

- **Total Endpoints Tested**: 23
- **Working with Auth**: 23
- **Working without Auth**: 0
- **Auth Required**: 0
- **Not Available**: 0

---

## Working Blockchain Endpoints

### `/data/blockchain/histo/day`

**Description**: Daily historical blockchain statistics

**Parameters**: `{'fsym': 'BTC', 'limit': 10}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/histo/hour`

**Description**: Hourly historical blockchain statistics

**Parameters**: `{'fsym': 'BTC', 'limit': 24}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/histo/minute`

**Description**: Minute historical blockchain statistics

**Parameters**: `{'fsym': 'BTC', 'limit': 60}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/latest`

**Description**: Latest blockchain data for a coin

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/list`

**Description**: List all available blockchain data coins

**Parameters**: `None`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/available_coins`

**Description**: Get available blockchain coins

**Parameters**: `None`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/coins`

**Description**: List of coins with blockchain data

**Parameters**: `None`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/mining/calculator`

**Description**: Mining profitability calculator

**Parameters**: `{'fsyms': 'BTC', 'tsym': 'USD'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `HasWarning`, `Type`, `RateLimit`, `Data`, `ParamWithError`

🔒 **Requires authentication**

---

### `/data/blockchain/mining/stats`

**Description**: Mining statistics

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/block/latest`

**Description**: Latest block information

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/block/height`

**Description**: Block by height

**Parameters**: `{'fsym': 'BTC', 'height': '800000'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/block/hash`

**Description**: Block by hash

**Parameters**: `{'fsym': 'BTC', 'hash': '00000000000000000001'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/tx/latest`

**Description**: Latest transactions

**Parameters**: `{'fsym': 'BTC', 'limit': 10}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/mempool`

**Description**: Mempool statistics

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/stats`

**Description**: General blockchain statistics

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/stats/latest`

**Description**: Latest blockchain stats

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/difficulty`

**Description**: Mining difficulty data

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/hashrate`

**Description**: Network hashrate data

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/address/balance`

**Description**: Address balance lookup

**Parameters**: `{'fsym': 'BTC', 'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/address/transactions`

**Description**: Address transaction history

**Parameters**: `{'fsym': 'BTC', 'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'limit': 10}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/supply`

**Description**: Circulating supply data

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/supply/total`

**Description**: Total supply

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

### `/data/blockchain/distribution`

**Description**: Wealth distribution

**Parameters**: `{'fsym': 'BTC'}`

**Response Data Type**: `dict`

**Response Fields**: `Response`, `Message`, `Type`, `Data`

🔒 **Requires authentication**

---

## Usage Examples

### With API Key

```python
import requests

headers = {"authorization": "Apikey YOUR_API_KEY"}
url = "https://min-api.cryptocompare.com/data/blockchain/latest"
params = {"fsym": "BTC"}
response = requests.get(url, params=params, headers=headers)
data = response.json()
```

### Without API Key (if supported)

```python
import requests

url = "https://min-api.cryptocompare.com/data/blockchain/latest"
params = {"fsym": "BTC"}
response = requests.get(url, params=params)
data = response.json()
```

---

## Supported Cryptocurrencies

Common cryptocurrencies with blockchain data:
- BTC (Bitcoin)
- ETH (Ethereum)
- LTC (Litecoin)
- DOGE (Dogecoin)
- And more (check `/data/blockchain/list` endpoint)

