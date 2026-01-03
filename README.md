# CoinDesk API Explorer

Comprehensive exploration and documentation of the CoinDesk REST Data API.

## Overview

This repository contains tools, scripts, and documentation for exploring and testing the CoinDesk Digital Asset Data REST API. The API provides comprehensive coverage of digital assets including:

- Centralized and decentralized spot, futures, and options exchanges
- Up-to-the-minute news and social metrics
- On-chain metrics and DeFi data
- Historical order book snapshots
- Reference prices and indices

## API Information

- **Base URL**: https://data-api.coindesk.com
- **Documentation**: https://developers.coindesk.com/documentation/data-api/introduction
- **Rate Limit Endpoint**: https://data-api.coindesk.com/admin/v2/rate/limit
- **Status Page**: https://status.coindesk.com/

## Authentication

CoinDesk API supports three authentication methods:

1. **Query Parameter**: `?api_key={YOUR_API_KEY}`
2. **Authorization Header**: 
   - Bearer Token: `Authorization: Bearer {YOUR_API_KEY}`
   - API Key: `Authorization: Apikey {YOUR_API_KEY}`
3. **X-API-Key Header**: `x-api-key: {YOUR_API_KEY}`

## Rate Limiting

- Account-level rate limiting (not per API key)
- Based on calls, not credits
- Multiple time windows: per second, minute, hour, day, month
- Response headers provide detailed rate limit info:
  - `X-Ratelimit-Limit` — Maximum requests per time window
  - `X-Ratelimit-Remaining` — Remaining requests
  - `X-Ratelimit-Reset` — Time until reset

## Project Structure

```
ExploreCoinDesk-API/
├── config/              # API configuration files
│   ├── coindesk.env     # Environment variables (API keys)
│   └── coindesk.env.example
├── docs/                # API documentation
├── scripts/             # Probe scripts for testing endpoints
├── src/                 # Shared utilities and API client
└── tests/               # Test files
```

## Getting Started

1. **Configure API Key**:
   ```bash
   # Copy example config
   cp config/coindesk.env.example config/coindesk.env
   # Edit config/coindesk.env with your API key
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Check Rate Limits**:
   ```bash
   python scripts/check_rate_limits.py
   ```

## Features

- ✅ Comprehensive data depth across all digital asset classes
- ✅ Standardized instrument mapping
- ✅ Multiple exchange support (spot, futures, options, DeFi)
- ✅ Unified data format (JSON, CSV available)
- ✅ CCSEQ (CoinDesk Sequence) for reliable data ordering
- ✅ Transparent rate limiting with detailed headers
- ✅ ISO 27001 certified for security

## Documentation

- [API Endpoint Reference](docs/endpoints.md)
- [Integration Guide](docs/integration-guide.md)

## Next Steps

- [ ] Explore REST Data API endpoints
- [ ] Document rate limits and usage patterns
- [ ] Create probe scripts for major endpoint categories
- [ ] Test authentication methods
- [ ] Document response formats

## Support

- **Email**: support@ccdata.io
- **Status**: https://status.coindesk.com/
- **Documentation**: https://developers.coindesk.com/

---

*Created: January 2, 2026*  
*Last Updated: January 2, 2026*
