"""
Enumerate detailed information for all 52 CryptoCompare MinAPI endpoints.
Fetches real responses, documents structure, and provides comprehensive metadata.
"""

import json
import requests
import time
from datetime import datetime

BASE_URL = "https://min-api.cryptocompare.com"

# Load endpoint definitions
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(os.path.dirname(script_dir), 'ALL_52_ENDPOINTS_FROM_ISSUE_12.json')
with open(json_path, 'r') as f:
    endpoint_data = json.load(f)

def make_request(endpoint, params):
    """Make API request with error handling"""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=10)
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'response': response.json() if response.status_code == 200 else response.text,
            'size_bytes': len(response.content)
        }
    except Exception as e:
        return {'error': str(e)}

def analyze_response_structure(data, prefix=""):
    """Recursively analyze response structure"""
    structure = {}
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                structure[key] = f"Object ({len(value)} fields)"
            elif isinstance(value, list):
                if len(value) > 0:
                    structure[key] = f"Array[{len(value)}] of {type(value[0]).__name__}"
                else:
                    structure[key] = "Array (empty)"
            else:
                structure[key] = type(value).__name__
    elif isinstance(data, list) and len(data) > 0:
        structure = f"Array[{len(data)}] of {type(data[0]).__name__}"
    
    return structure

def enumerate_endpoint(endpoint_info):
    """Gather detailed information about an endpoint"""
    endpoint = endpoint_info['endpoint']
    method = endpoint_info.get('method', 'GET')
    params = endpoint_info.get('sample_params', {})
    
    print(f"Enumerating: {endpoint}")
    
    # Make the API call
    result = make_request(endpoint, params)
    
    # Analyze response
    details = {
        'endpoint': endpoint,
        'method': method,
        'sample_params': params,
        'status_code': result.get('status_code'),
        'response_size_bytes': result.get('size_bytes'),
        'response_time': None,  # Could add timing
    }
    
    if 'response' in result and isinstance(result['response'], dict):
        details['response_structure'] = analyze_response_structure(result['response'])
        details['sample_response'] = result['response']
        
        # Extract common fields
        if 'Response' in result['response']:
            details['api_response_type'] = result['response']['Response']
        if 'Message' in result['response']:
            details['api_message'] = result['response']['Message']
        if 'Data' in result['response']:
            details['has_data_field'] = True
            details['data_type'] = type(result['response']['Data']).__name__
    
    # Add headers info
    if 'headers' in result:
        details['cache_control'] = result['headers'].get('Cache-Control')
        details['content_type'] = result['headers'].get('Content-Type')
    
    return details

# Define sample parameters for each category
sample_params = {
    '/data/price': {'fsym': 'BTC', 'tsyms': 'USD,EUR'},
    '/data/pricemulti': {'fsyms': 'BTC,ETH', 'tsyms': 'USD,EUR'},
    '/data/pricemultifull': {'fsyms': 'BTC,ETH', 'tsyms': 'USD'},
    '/data/generateAvg': {'fsym': 'BTC', 'tsym': 'USD', 'e': 'Coinbase'},
    
    '/data/v2/histoday': {'fsym': 'BTC', 'tsym': 'USD', 'limit': 5},
    '/data/v2/histohour': {'fsym': 'BTC', 'tsym': 'USD', 'limit': 5},
    '/data/v2/histominute': {'fsym': 'BTC', 'tsym': 'USD', 'limit': 5},
    '/data/pricehistorical': {'fsym': 'BTC', 'tsyms': 'USD', 'ts': 1609459200},
    '/data/dayAvg': {'fsym': 'BTC', 'tsym': 'USD', 'toTs': int(time.time())},
    '/data/exchange/histoday': {'tsym': 'USD', 'limit': 5},
    
    '/data/blockchain/list': {},
    '/data/blockchain/latest': {'fsym': 'BTC'},
    '/data/blockchain/histo/day': {'fsym': 'BTC', 'limit': 5},
    '/data/blockchain/mining/calculator': {'fsyms': 'BTC', 'tsyms': 'USD'},
    '/data/blockchain/mining/equipment/list': {},
    '/data/blockchain/staking/latest': {'fsym': 'ETH'},
    
    '/data/tradingsignals/intotheblock/latest': {'fsym': 'BTC'},
    
    '/data/pair/mapping/fsym': {'fsym': 'BTC'},
    '/data/pair/mapping/exchange': {'e': 'Coinbase'},
    '/data/pair/mapping/fsym/exchange': {'fsym': 'BTC', 'e': 'Coinbase'},
    '/data/pair/remapping/planned': {},
    
    '/data/top/totalvolumefull': {'tsym': 'USD', 'limit': 5},
    '/data/top/totalvolume/tier': {'tsym': 'USD', 'limit': 5},
    '/data/top/mktcapfull': {'tsym': 'USD', 'limit': 5},
    '/data/top/exchanges': {'fsym': 'BTC', 'tsym': 'USD', 'limit': 5},
    '/data/top/exchangesfull': {'fsym': 'BTC', 'tsym': 'USD', 'limit': 5},
    
    '/data/social/coin/latest': {'coinId': '1182'},
    '/data/social/coin/histo/day': {'coinId': '1182', 'limit': 5},
    '/data/social/coin/histo/hour': {'coinId': '1182', 'limit': 5},
    
    '/data/v2/news/': {'lang': 'EN'},
    '/data/news/feeds': {},
    '/data/news/categories': {},
    '/data/news/feedsandcategories': {},
    
    '/data/ob/exchanges': {},
    '/data/ob/l1/top': {'fsym': 'BTC', 'tsym': 'USD', 'limit': 5},
    '/data/ob/l2/snapshot': {'fsym': 'BTC', 'tsym': 'USD', 'e': 'Coinbase'},
    
    '/data/all/exchanges': {},
    '/data/all/coinlist': {},
    '/data/cccagg/pairs': {},
    '/data/cccagg/pairs/excluded': {},
    '/data/cccagg/pairs/absent': {},
    
    '/data/top/volumes': {'tsym': 'USD'},
    '/data/top/volume/tier': {'tsym': 'USD'},
    '/data/top/mktcap': {'tsym': 'USD'},
    '/data/top/volume/direct': {'tsym': 'USD'},
    '/data/top/price': {'tsym': 'USD'},
    
    '/data/index/list': {},
    '/data/index/value': {'indexName': 'MVDA25', 'tsym': 'USD'},
    '/data/index/histo/minute': {'indexName': 'MVDA25', 'tsym': 'USD', 'limit': 5},
    '/data/index/histo/hour': {'indexName': 'MVDA25', 'tsym': 'USD', 'limit': 5},
    '/data/index/histo/day': {'indexName': 'MVDA25', 'tsym': 'USD', 'limit': 5},
    '/data/index/underlying/list': {'indexName': 'MVDA25'},
}

# Process all endpoints
all_details = {}
categories = endpoint_data.get('categories', {})

for category_name, endpoints in categories.items():
    print(f"\n{'='*80}")
    print(f"Processing Category: {category_name}")
    print(f"{'='*80}")
    
    category_details = []
    
    for ep in endpoints:
        endpoint_path = ep['endpoint']
        
        # Add sample params
        ep['sample_params'] = sample_params.get(endpoint_path, {})
        
        # Enumerate details
        details = enumerate_endpoint(ep)
        category_details.append(details)
        
        # Rate limiting
        time.sleep(0.5)
    
    all_details[category_name] = category_details

# Save results
output_file = 'endpoint_detailed_enumeration.json'
with open(output_file, 'w') as f:
    json.dump(all_details, f, indent=2)

print(f"\n{'='*80}")
print(f"✅ Detailed enumeration complete!")
print(f"Results saved to: {output_file}")
print(f"{'='*80}")

# Generate summary statistics
total_endpoints = sum(len(eps) for eps in all_details.values())
successful_calls = sum(
    1 for cat in all_details.values() 
    for ep in cat 
    if ep.get('status_code') == 200
)

print(f"\nSummary:")
print(f"- Total endpoints enumerated: {total_endpoints}")
print(f"- Successful API calls: {successful_calls}/{total_endpoints}")
print(f"- Timestamp: {datetime.now().isoformat()}")
