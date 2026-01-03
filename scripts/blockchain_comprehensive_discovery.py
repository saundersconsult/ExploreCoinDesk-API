#!/usr/bin/env python3
"""
Comprehensive Blockchain Data Discovery for CryptoCompare MinAPI.
Exploring all blockchain-related endpoints and data structures.
"""

import requests
import json
from pathlib import Path
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(Path(__file__).parent.parent / "config" / "cryptocompare.env")

BASE_URL = "https://min-api.cryptocompare.com"
API_KEY = os.getenv("CRYPTOCOMPARE_API_KEY", "")

# Comprehensive blockchain endpoints to test
BLOCKCHAIN_ENDPOINTS = {
    # Historical Blockchain Data
    "/data/blockchain/histo/day": {
        "desc": "Daily historical blockchain statistics",
        "params": {"fsym": "BTC", "limit": 10},
        "test_variations": [
            {"fsym": "BTC", "limit": 30},
            {"fsym": "ETH", "limit": 10},
            {"fsym": "LTC", "limit": 5},
        ]
    },
    "/data/blockchain/histo/hour": {
        "desc": "Hourly historical blockchain statistics",
        "params": {"fsym": "BTC", "limit": 24}
    },
    "/data/blockchain/histo/minute": {
        "desc": "Minute historical blockchain statistics",
        "params": {"fsym": "BTC", "limit": 60}
    },
    
    # Latest Blockchain Data
    "/data/blockchain/latest": {
        "desc": "Latest blockchain data for a coin",
        "params": {"fsym": "BTC"},
        "test_variations": [
            {"fsym": "BTC"},
            {"fsym": "ETH"},
            {"fsym": "LTC"},
            {"fsym": "DOGE"},
        ]
    },
    
    # Blockchain Lists & Available Data
    "/data/blockchain/list": {
        "desc": "List all available blockchain data coins",
        "params": None
    },
    "/data/blockchain/available_coins": {
        "desc": "Get available blockchain coins",
        "params": None
    },
    "/data/blockchain/coins": {
        "desc": "List of coins with blockchain data",
        "params": None
    },
    
    # Mining Data
    "/data/blockchain/mining/calculator": {
        "desc": "Mining profitability calculator",
        "params": {"fsyms": "BTC", "tsym": "USD"}
    },
    "/data/blockchain/mining/stats": {
        "desc": "Mining statistics",
        "params": {"fsym": "BTC"}
    },
    
    # Block Data
    "/data/blockchain/block/latest": {
        "desc": "Latest block information",
        "params": {"fsym": "BTC"}
    },
    "/data/blockchain/block/height": {
        "desc": "Block by height",
        "params": {"fsym": "BTC", "height": "800000"}
    },
    "/data/blockchain/block/hash": {
        "desc": "Block by hash",
        "params": {"fsym": "BTC", "hash": "00000000000000000001"}
    },
    
    # Transaction Data
    "/data/blockchain/tx/latest": {
        "desc": "Latest transactions",
        "params": {"fsym": "BTC", "limit": 10}
    },
    "/data/blockchain/mempool": {
        "desc": "Mempool statistics",
        "params": {"fsym": "BTC"}
    },
    
    # Network Stats
    "/data/blockchain/stats": {
        "desc": "General blockchain statistics",
        "params": {"fsym": "BTC"}
    },
    "/data/blockchain/stats/latest": {
        "desc": "Latest blockchain stats",
        "params": {"fsym": "BTC"}
    },
    "/data/blockchain/difficulty": {
        "desc": "Mining difficulty data",
        "params": {"fsym": "BTC"}
    },
    "/data/blockchain/hashrate": {
        "desc": "Network hashrate data",
        "params": {"fsym": "BTC"}
    },
    
    # Address & Balance
    "/data/blockchain/address/balance": {
        "desc": "Address balance lookup",
        "params": {"fsym": "BTC", "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}
    },
    "/data/blockchain/address/transactions": {
        "desc": "Address transaction history",
        "params": {"fsym": "BTC", "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "limit": 10}
    },
    
    # Supply & Distribution
    "/data/blockchain/supply": {
        "desc": "Circulating supply data",
        "params": {"fsym": "BTC"}
    },
    "/data/blockchain/supply/total": {
        "desc": "Total supply",
        "params": {"fsym": "BTC"}
    },
    "/data/blockchain/distribution": {
        "desc": "Wealth distribution",
        "params": {"fsym": "BTC"}
    },
}

def test_endpoint(path, params=None, use_api_key=True):
    """Test a blockchain endpoint with optional API key"""
    url = BASE_URL + path
    
    headers = {}
    if use_api_key and API_KEY:
        headers["authorization"] = f"Apikey {API_KEY}"
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        try:
            json_data = response.json()
            
            # Analyze response structure
            if isinstance(json_data, dict):
                response_type = json_data.get("Response", "Unknown")
                message = json_data.get("Message", "")
                has_data = "Data" in json_data
                data_type = type(json_data.get("Data")).__name__ if has_data else None
                
                # Success case
                if response_type == "Success" or (has_data and response.status_code == 200):
                    # Try to get sample data structure
                    sample_data = None
                    if has_data:
                        data = json_data["Data"]
                        if isinstance(data, list) and len(data) > 0:
                            sample_data = data[0]
                        elif isinstance(data, dict):
                            sample_data = {k: type(v).__name__ for k, v in list(data.items())[:5]}
                    
                    return {
                        "status_code": response.status_code,
                        "success": True,
                        "response_type": response_type,
                        "message": message,
                        "has_data": has_data,
                        "data_type": data_type,
                        "sample_data": sample_data,
                        "fields": list(json_data.keys()),
                        "error": None
                    }
                
                # Error case
                return {
                    "status_code": response.status_code,
                    "success": False,
                    "response_type": response_type,
                    "message": message,
                    "has_data": False,
                    "data_type": None,
                    "sample_data": None,
                    "fields": list(json_data.keys()),
                    "error": message
                }
            
            # Non-standard response
            return {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response_type": "Non-standard",
                "message": str(json_data)[:200],
                "has_data": bool(json_data),
                "data_type": type(json_data).__name__,
                "sample_data": None,
                "fields": [],
                "error": None if response.status_code == 200 else "Non-standard response"
            }
            
        except json.JSONDecodeError:
            return {
                "status_code": response.status_code,
                "success": False,
                "response_type": "Invalid JSON",
                "message": response.text[:200],
                "has_data": False,
                "data_type": None,
                "sample_data": None,
                "fields": [],
                "error": "Invalid JSON response"
            }
            
    except requests.RequestException as e:
        return {
            "status_code": None,
            "success": False,
            "response_type": "Connection Error",
            "message": str(e),
            "has_data": False,
            "data_type": None,
            "sample_data": None,
            "fields": [],
            "error": str(e)
        }

def main():
    """Main blockchain discovery function"""
    print("=" * 80)
    print("CryptoCompare MinAPI - Comprehensive Blockchain Data Discovery")
    print(f"Base URL: {BASE_URL}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"API Key Configured: {'Yes' if API_KEY else 'No (limited access)'}")
    print(f"Total Endpoints to Test: {len(BLOCKCHAIN_ENDPOINTS)}")
    print("=" * 80)
    
    results = {}
    categories = {
        "working_with_auth": [],
        "working_no_auth": [],
        "auth_required": [],
        "path_not_found": [],
        "param_errors": [],
        "other_errors": []
    }
    
    for endpoint, config in BLOCKCHAIN_ENDPOINTS.items():
        print(f"\n{'='*80}")
        print(f"Testing: {endpoint}")
        print(f"Description: {config['desc']}")
        print(f"{'='*80}")
        
        # Test with API key first
        print("\n[With API Key]" if API_KEY else "\n[Without API Key]")
        result_with_key = test_endpoint(endpoint, params=config['params'], use_api_key=True)
        
        # Test without API key
        result_without_key = None
        if API_KEY:
            print("\n[Without API Key]")
            result_without_key = test_endpoint(endpoint, params=config['params'], use_api_key=False)
        
        # Store results
        results[endpoint] = {
            "description": config['desc'],
            "params": config['params'],
            "with_auth": result_with_key,
            "without_auth": result_without_key
        }
        
        # Categorize
        if result_with_key["success"]:
            categories["working_with_auth"].append(endpoint)
            print(f"✓ SUCCESS (with auth)")
            print(f"  Response Type: {result_with_key['response_type']}")
            print(f"  Has Data: {result_with_key['has_data']}")
            if result_with_key['has_data']:
                print(f"  Data Type: {result_with_key['data_type']}")
                print(f"  Fields: {', '.join(result_with_key['fields'])}")
                if result_with_key['sample_data']:
                    print(f"  Sample: {str(result_with_key['sample_data'])[:200]}...")
            
            # Check if works without auth
            if result_without_key and result_without_key["success"]:
                categories["working_no_auth"].append(endpoint)
                print(f"  ✓ Also works WITHOUT auth")
        elif "auth" in result_with_key["error"].lower() or "api key" in result_with_key["error"].lower():
            categories["auth_required"].append(endpoint)
            print(f"🔒 AUTH REQUIRED: {result_with_key['error']}")
        elif "path does not exist" in result_with_key["error"].lower():
            categories["path_not_found"].append(endpoint)
            print(f"✗ PATH NOT FOUND")
        elif "param" in result_with_key["error"].lower() or "required" in result_with_key["error"].lower():
            categories["param_errors"].append(endpoint)
            print(f"⚠ PARAM ERROR: {result_with_key['error']}")
        else:
            categories["other_errors"].append(endpoint)
            print(f"✗ ERROR: {result_with_key['error']}")
        
        # Test variations if endpoint works
        if result_with_key["success"] and "test_variations" in config:
            print(f"\n  Testing variations...")
            for i, variation in enumerate(config['test_variations']):
                var_result = test_endpoint(endpoint, params=variation, use_api_key=True)
                if var_result["success"]:
                    print(f"    ✓ Variation {i+1}: {variation}")
                else:
                    print(f"    ✗ Variation {i+1}: {variation} - {var_result['error']}")
    
    # Summary Report
    print("\n" + "=" * 80)
    print("COMPREHENSIVE BLOCKCHAIN DATA DISCOVERY SUMMARY")
    print("=" * 80)
    print(f"Total Endpoints Tested: {len(BLOCKCHAIN_ENDPOINTS)}")
    print(f"✓ Working with Auth: {len(categories['working_with_auth'])}")
    print(f"✓ Working without Auth: {len(categories['working_no_auth'])}")
    print(f"🔒 Auth Required: {len(categories['auth_required'])}")
    print(f"✗ Path Not Found: {len(categories['path_not_found'])}")
    print(f"⚠ Parameter Errors: {len(categories['param_errors'])}")
    print(f"✗ Other Errors: {len(categories['other_errors'])}")
    
    # Detailed breakdown
    if categories["working_with_auth"]:
        print("\n" + "=" * 80)
        print("WORKING BLOCKCHAIN ENDPOINTS (with authentication)")
        print("=" * 80)
        for endpoint in categories["working_with_auth"]:
            result = results[endpoint]["with_auth"]
            print(f"\n✓ {endpoint}")
            print(f"  Description: {results[endpoint]['description']}")
            print(f"  Response Fields: {', '.join(result['fields'])}")
            if result['data_type']:
                print(f"  Data Type: {result['data_type']}")
    
    if categories["working_no_auth"]:
        print("\n" + "=" * 80)
        print("WORKING WITHOUT AUTHENTICATION")
        print("=" * 80)
        for endpoint in categories["working_no_auth"]:
            print(f"  ✓ {endpoint}")
    
    if categories["auth_required"]:
        print("\n" + "=" * 80)
        print("AUTHENTICATION REQUIRED")
        print("=" * 80)
        for endpoint in categories["auth_required"]:
            print(f"  🔒 {endpoint} - {results[endpoint]['description']}")
    
    if categories["path_not_found"]:
        print("\n" + "=" * 80)
        print(f"PATH NOT FOUND ({len(categories['path_not_found'])} endpoints)")
        print("=" * 80)
        for endpoint in categories["path_not_found"][:15]:
            print(f"  ✗ {endpoint}")
        if len(categories["path_not_found"]) > 15:
            print(f"  ... and {len(categories['path_not_found']) - 15} more")
    
    # Save detailed results
    results_file = Path(__file__).parent.parent / "blockchain_discovery_results.json"
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "api_key_used": bool(API_KEY),
        "summary": {
            "total": len(BLOCKCHAIN_ENDPOINTS),
            "working_with_auth": len(categories["working_with_auth"]),
            "working_no_auth": len(categories["working_no_auth"]),
            "auth_required": len(categories["auth_required"]),
            "path_not_found": len(categories["path_not_found"]),
            "param_errors": len(categories["param_errors"]),
            "other_errors": len(categories["other_errors"])
        },
        "categories": categories,
        "detailed_results": results
    }
    
    with open(results_file, "w") as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\n{'='*80}")
    print(f"Detailed results saved to: {results_file}")
    print("=" * 80)
    
    # Generate documentation
    generate_documentation(output_data, results)

def generate_documentation(output_data, results):
    """Generate comprehensive blockchain data documentation"""
    doc_file = Path(__file__).parent.parent / "docs" / "BLOCKCHAIN_DATA_COMPREHENSIVE.md"
    
    with open(doc_file, "w", encoding="utf-8") as f:
        f.write("# CryptoCompare MinAPI - Comprehensive Blockchain Data Documentation\n\n")
        f.write(f"**Discovery Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Base URL**: `{BASE_URL}`\n\n")
        f.write(f"**API Key Required**: {'Yes (configured)' if API_KEY else 'Not configured - limited access'}\n\n")
        
        f.write("---\n\n")
        f.write("## Discovery Summary\n\n")
        f.write(f"- **Total Endpoints Tested**: {output_data['summary']['total']}\n")
        f.write(f"- **Working with Auth**: {output_data['summary']['working_with_auth']}\n")
        f.write(f"- **Working without Auth**: {output_data['summary']['working_no_auth']}\n")
        f.write(f"- **Auth Required**: {output_data['summary']['auth_required']}\n")
        f.write(f"- **Not Available**: {output_data['summary']['path_not_found']}\n\n")
        
        f.write("---\n\n")
        
        # Working endpoints
        if output_data['categories']['working_with_auth']:
            f.write("## Working Blockchain Endpoints\n\n")
            for endpoint in output_data['categories']['working_with_auth']:
                result = results[endpoint]
                f.write(f"### `{endpoint}`\n\n")
                f.write(f"**Description**: {result['description']}\n\n")
                f.write(f"**Parameters**: `{result['params']}`\n\n")
                
                auth_result = result['with_auth']
                if auth_result['has_data']:
                    f.write(f"**Response Data Type**: `{auth_result['data_type']}`\n\n")
                    f.write(f"**Response Fields**: {', '.join([f'`{field}`' for field in auth_result['fields']])}\n\n")
                    
                    if auth_result['sample_data']:
                        f.write("**Sample Data Structure**:\n```json\n")
                        f.write(json.dumps(auth_result['sample_data'], indent=2))
                        f.write("\n```\n\n")
                
                # Check if works without auth
                if endpoint in output_data['categories']['working_no_auth']:
                    f.write("✓ **Works without authentication**\n\n")
                else:
                    f.write("🔒 **Requires authentication**\n\n")
                
                f.write("---\n\n")
        
        # Auth required
        if output_data['categories']['auth_required']:
            f.write("## Endpoints Requiring Authentication\n\n")
            f.write("These endpoints require a valid API key:\n\n")
            for endpoint in output_data['categories']['auth_required']:
                f.write(f"- 🔒 `{endpoint}` - {results[endpoint]['description']}\n")
            f.write("\n---\n\n")
        
        # Not available
        if output_data['categories']['path_not_found']:
            f.write("## Endpoints Not Available\n\n")
            f.write("These endpoints were tested but are not available in the current API:\n\n")
            for endpoint in output_data['categories']['path_not_found']:
                f.write(f"- ✗ `{endpoint}` - {results[endpoint]['description']}\n")
            f.write("\n---\n\n")
        
        f.write("## Usage Examples\n\n")
        f.write("### With API Key\n\n")
        f.write("```python\n")
        f.write("import requests\n\n")
        f.write('headers = {"authorization": "Apikey YOUR_API_KEY"}\n')
        f.write(f'url = "{BASE_URL}/data/blockchain/latest"\n')
        f.write('params = {"fsym": "BTC"}\n')
        f.write("response = requests.get(url, params=params, headers=headers)\n")
        f.write("data = response.json()\n")
        f.write("```\n\n")
        
        f.write("### Without API Key (if supported)\n\n")
        f.write("```python\n")
        f.write("import requests\n\n")
        f.write(f'url = "{BASE_URL}/data/blockchain/latest"\n')
        f.write('params = {"fsym": "BTC"}\n')
        f.write("response = requests.get(url, params=params)\n")
        f.write("data = response.json()\n")
        f.write("```\n\n")
        
        f.write("---\n\n")
        f.write("## Supported Cryptocurrencies\n\n")
        f.write("Common cryptocurrencies with blockchain data:\n")
        f.write("- BTC (Bitcoin)\n")
        f.write("- ETH (Ethereum)\n")
        f.write("- LTC (Litecoin)\n")
        f.write("- DOGE (Dogecoin)\n")
        f.write("- And more (check `/data/blockchain/list` endpoint)\n\n")
    
    print(f"Documentation generated: {doc_file}")

if __name__ == "__main__":
    main()
