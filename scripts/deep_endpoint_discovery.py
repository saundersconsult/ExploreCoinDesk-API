#!/usr/bin/env python3
"""
Deep Discovery: Comprehensive endpoint documentation with parameter exploration.

This script performs exhaustive testing of all 52 CryptoCompare MinAPI endpoints:
1. Tests multiple parameter combinations per endpoint
2. Documents full response schemas with examples
3. Tests edge cases and error handling
4. Captures rate limit headers
5. Generates usage examples and best practices
"""

import requests
import json
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://min-api.cryptocompare.com"
ENDPOINTS_FILE = Path(__file__).parent.parent / "docs" / "ALL_52_ENDPOINTS_FROM_ISSUE_12.json"
OUTPUT_FILE = Path(__file__).parent.parent / "deep_discovery_results.json"

class EndpointExplorer:
    """Comprehensive endpoint exploration and documentation."""
    
    def __init__(self):
        self.results = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "base_url": BASE_URL,
                "total_endpoints": 0,
                "total_tests": 0,
                "successful_tests": 0
            },
            "endpoints": {}
        }
        
    def load_endpoints(self) -> List[Dict]:
        """Load endpoint specifications."""
        with open(ENDPOINTS_FILE, "r") as f:
            data = json.load(f)
        
        endpoints = []
        for category, items in data.items():
            if category in ["metadata", "summary"]:
                continue
            
            if isinstance(items, list):
                for endpoint_spec in items:
                    endpoint_spec["category"] = category
                    endpoints.append(endpoint_spec)
        
        self.results["metadata"]["total_endpoints"] = len(endpoints)
        return endpoints
    
    def make_request(self, url: str) -> Dict[str, Any]:
        """Make API request and capture comprehensive response details."""
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10, verify=False)
            elapsed = time.time() - start_time
            
            # Capture rate limit headers
            rate_limit_info = {
                "limit": response.headers.get("X-Ratelimit-Limit"),
                "remaining": response.headers.get("X-Ratelimit-Remaining"),
                "reset": response.headers.get("X-Ratelimit-Reset"),
                "retry_after": response.headers.get("Retry-After")
            }
            
            result = {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "elapsed_ms": round(elapsed * 1000, 2),
                "rate_limit": rate_limit_info,
                "url": url,
                "timestamp": datetime.now().isoformat()
            }
            
            # Parse response
            try:
                data = response.json()
                result["response_type"] = type(data).__name__
                result["response"] = data
                
                if isinstance(data, dict):
                    result["response_keys"] = list(data.keys())
                    result["response_size_bytes"] = len(response.content)
                    
                    # Extract error message if present
                    if "Message" in data or "message" in data:
                        result["error_message"] = data.get("Message") or data.get("message")
                    
                    # Count nested items
                    if "Data" in data:
                        if isinstance(data["Data"], list):
                            result["data_count"] = len(data["Data"])
                        elif isinstance(data["Data"], dict):
                            result["data_keys"] = list(data["Data"].keys())
                            
                elif isinstance(data, list):
                    result["response_count"] = len(data)
                    
            except json.JSONDecodeError:
                result["response_type"] = "non-json"
                result["response_text"] = response.text[:500]
                
            return result
            
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Timeout",
                "url": url,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "url": url,
                "timestamp": datetime.now().isoformat()
            }
    
    def get_parameter_combinations(self, endpoint_spec: Dict) -> List[Dict[str, str]]:
        """Generate multiple parameter combinations for testing."""
        endpoint = endpoint_spec["endpoint"]
        params = endpoint_spec.get("parameters", [])
        category = endpoint_spec["category"]
        
        # Base test cases
        combinations = []
        
        # Price endpoints
        if category == "Price":
            if "fsym" in params:
                combinations.extend([
                    {"fsym": "BTC", "tsyms": "USD"},
                    {"fsym": "ETH", "tsyms": "USD,EUR,GBP"},
                    {"fsym": "BTC", "tsyms": "USD", "e": "Coinbase"},
                    {"fsym": "BTC", "tsyms": "USD", "e": "Binance"}
                ])
            if "fsyms" in params:
                combinations.extend([
                    {"fsyms": "BTC,ETH", "tsyms": "USD"},
                    {"fsyms": "BTC,ETH,XRP", "tsyms": "USD,EUR"},
                    {"fsyms": "BTC", "tsyms": "USD", "e": "CCCAGG"}
                ])
        
        # Historical endpoints
        elif category == "Historical":
            # Calculate timestamps once
            yesterday = int((datetime.now() - timedelta(days=1)).timestamp())
            week_ago = int((datetime.now() - timedelta(days=7)).timestamp())
            
            if "fsym" in params:
                combinations.extend([
                    {"fsym": "BTC", "tsym": "USD", "limit": "10"},
                    {"fsym": "BTC", "tsym": "USD", "limit": "100"},
                    {"fsym": "ETH", "tsym": "USD", "limit": "30"},
                    {"fsym": "BTC", "tsym": "USD", "limit": "7", "aggregate": "1"},
                ])
                
                # Add timestamp variations
                if "toTs" in params:
                    combinations.extend([
                        {"fsym": "BTC", "tsym": "USD", "toTs": str(yesterday)},
                        {"fsym": "BTC", "tsym": "USD", "toTs": str(week_ago), "limit": "7"}
                    ])
                    
                if "ts" in params:  # Price historical
                    combinations.extend([
                        {"fsym": "BTC", "tsyms": "USD", "ts": str(yesterday)},
                        {"fsym": "ETH", "tsyms": "USD,EUR", "ts": str(week_ago)}
                    ])
        
        # Blockchain endpoints
        elif category == "Blockchain":
            combinations.extend([
                {"fsym": "BTC"},
                {"fsym": "ETH"},
                {"fsym": "XRP"}
            ])
        
        # Trading Signals
        elif category == "Trading Signals":
            combinations.extend([
                {"fsym": "BTC"},
                {"fsym": "ETH"}
            ])
        
        # Pair Mapping
        elif category == "Pair Mapping":
            if "fsym" in params:
                combinations.extend([
                    {"fsym": "BTC"},
                    {"fsym": "ETH"}
                ])
            if "e" in params and "fsym" not in params:
                combinations.extend([
                    {"e": "Coinbase"},
                    {"e": "Binance"},
                    {"e": "Kraken"}
                ])
            if not params or "extraParams" in params:
                combinations.append({})
        
        # Top Lists
        elif category == "Top Lists":
            if "limit" in params:
                combinations.extend([
                    {"limit": "10", "tsym": "USD"},
                    {"limit": "50", "tsym": "USD"},
                    {"limit": "100", "tsym": "USD"}
                ])
            if "tsym" in params and "limit" not in params:
                combinations.extend([
                    {"tsym": "USD"},
                    {"tsym": "BTC"}
                ])
        
        # Social endpoints
        elif category == "Social":
            if "coinId" in params:
                combinations.extend([
                    {"coinId": "1"},  # BTC
                    {"coinId": "7605"}  # ETH
                ])
            else:
                combinations.append({})
        
        # News endpoints
        elif category == "News":
            if "feeds" in params or "categories" in params:
                combinations.extend([
                    {},
                    {"feeds": "cryptocompare"},
                    {"categories": "BTC,ETH"},
                    {"lang": "EN"}
                ])
            else:
                combinations.append({})
        
        # Order Book
        elif category == "Order Book":
            combinations.extend([
                {"fsym": "BTC", "tsym": "USD"},
                {"fsym": "ETH", "tsym": "USD"},
                {"fsym": "BTC", "tsym": "USD", "e": "Coinbase"}
            ])
        
        # General Info
        elif category == "General Info":
            combinations.append({})
        
        # Helper/Streaming
        elif category == "Helper":
            combinations.append({})
        
        # Index
        elif category == "Index":
            if "index_id" in params:
                combinations.extend([
                    {"index_id": "1"},
                    {"index_id": "2"},
                    {"index_id": "3"}
                ])
            else:
                combinations.append({})
        
        # Default fallback
        if not combinations:
            combinations.append({})
        
        return combinations
    
    def explore_endpoint(self, endpoint_spec: Dict) -> Dict:
        """Comprehensively explore a single endpoint."""
        endpoint = endpoint_spec["endpoint"]
        name = endpoint_spec["name"]
        category = endpoint_spec["category"]
        
        print(f"\n🔍 Exploring: [{category}] {name} ({endpoint})")
        
        endpoint_results = {
            "name": name,
            "endpoint": endpoint,
            "category": category,
            "doc_url": endpoint_spec.get("doc_url"),
            "description": endpoint_spec.get("description"),
            "parameters": endpoint_spec.get("parameters", []),
            "tests": [],
            "summary": {
                "total_tests": 0,
                "successful": 0,
                "failed": 0
            }
        }
        
        # Get parameter combinations
        param_combinations = self.get_parameter_combinations(endpoint_spec)
        
        # Test each combination
        for params in param_combinations:
            # Build URL
            url = f"{BASE_URL}{endpoint}"
            if params:
                query_string = "&".join(f"{k}={v}" for k, v in params.items())
                url = f"{url}?{query_string}"
            
            # Make request
            print(f"  Testing: {url}")
            test_result = self.make_request(url)
            test_result["parameters_used"] = params
            
            endpoint_results["tests"].append(test_result)
            endpoint_results["summary"]["total_tests"] += 1
            
            if test_result["success"]:
                endpoint_results["summary"]["successful"] += 1
                print(f"    ✅ Success ({test_result.get('elapsed_ms')}ms)")
            else:
                endpoint_results["summary"]["failed"] += 1
                error = test_result.get("error") or test_result.get("error_message", "Unknown")
                print(f"    ❌ Failed: {error}")
            
            self.results["metadata"]["total_tests"] += 1
            if test_result["success"]:
                self.results["metadata"]["successful_tests"] += 1
            
            # Rate limiting delay
            time.sleep(0.5)
        
        # Save progress after each endpoint
        self._save_progress()
        
        return endpoint_results
    
    def _save_progress(self):
        """Save current progress to file."""
        try:
            with open(OUTPUT_FILE, "w") as f:
                json.dump(self.results, f, indent=2)
        except:
            pass  # Continue even if save fails
    
    def run_exploration(self):
        """Run comprehensive exploration of all endpoints."""
        print("=" * 80)
        print("🚀 Starting Deep Endpoint Discovery")
        print("=" * 80)
        
        endpoints = self.load_endpoints()
        
        for endpoint_spec in endpoints:
            endpoint_results = self.explore_endpoint(endpoint_spec)
            self.results["endpoints"][endpoint_spec["endpoint"]] = endpoint_results
        
        # Final summary
        print("\n" + "=" * 80)
        print("📊 EXPLORATION COMPLETE")
        print("=" * 80)
        print(f"Total Endpoints: {self.results['metadata']['total_endpoints']}")
        print(f"Total Tests: {self.results['metadata']['total_tests']}")
        print(f"Successful: {self.results['metadata']['successful_tests']}")
        print(f"Failed: {self.results['metadata']['total_tests'] - self.results['metadata']['successful_tests']}")
        print(f"Success Rate: {self.results['metadata']['successful_tests'] / self.results['metadata']['total_tests'] * 100:.1f}%")
        
        # Save results
        with open(OUTPUT_FILE, "w") as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n💾 Results saved to: {OUTPUT_FILE}")

def main():
    explorer = EndpointExplorer()
    explorer.run_exploration()

if __name__ == "__main__":
    main()
