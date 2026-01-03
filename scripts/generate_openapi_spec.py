#!/usr/bin/env python3
"""
Generate OpenAPI 3.0 specification from deep discovery results.

Creates a complete OpenAPI/Swagger specification that can be used with:
- Swagger UI for interactive documentation
- Postman for API testing
- Code generation tools
- API gateways
"""

import json
from pathlib import Path
from typing import Dict, List, Any

INPUT_FILE = Path(__file__).parent.parent / "deep_discovery_results.json"
OUTPUT_FILE = Path(__file__).parent.parent / "cryptocompare_openapi.yaml"
OUTPUT_JSON = Path(__file__).parent.parent / "cryptocompare_openapi.json"


def generate_openapi_spec(results: Dict) -> Dict:
    """Generate OpenAPI 3.0 specification."""
    
    spec = {
        "openapi": "3.0.3",
        "info": {
            "title": "CryptoCompare MinAPI",
            "version": "1.0.0",
            "description": """
CryptoCompare MinAPI provides comprehensive cryptocurrency market data including:
- Real-time and historical prices
- OHLCV data across multiple timeframes
- Social media metrics
- News feeds
- Exchange listings
- On-chain data

This specification was auto-generated from comprehensive API discovery and testing.
""",
            "contact": {
                "name": "CryptoCompare",
                "url": "https://developers.coindesk.com"
            },
            "license": {
                "name": "API Terms of Service",
                "url": "https://developers.coindesk.com/terms"
            }
        },
        "servers": [
            {
                "url": "https://min-api.cryptocompare.com",
                "description": "Production server"
            }
        ],
        "security": [
            {"ApiKeyAuth": []},
            {"BearerAuth": []}
        ],
        "paths": {},
        "components": {
            "securitySchemes": {
                "ApiKeyAuth": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "x-api-key",
                    "description": "API key authentication"
                },
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "description": "Bearer token authentication"
                }
            },
            "schemas": {},
            "parameters": {}
        },
        "tags": []
    }
    
    # Generate tags from categories
    categories = set()
    for endpoint_data in results["endpoints"].values():
        categories.add(endpoint_data["category"])
    
    for category in sorted(categories):
        spec["tags"].append({
            "name": category,
            "description": f"{category} endpoints"
        })
    
    # Generate paths
    for endpoint_key, endpoint_data in results["endpoints"].items():
        endpoint_path = endpoint_data["endpoint"]
        
        # Get successful test for example response
        successful_tests = [t for t in endpoint_data["tests"] if t.get("success")]
        example_response = successful_tests[0] if successful_tests else None
        
        # Build parameters from tests
        parameters = []
        param_names = set()
        
        for test in endpoint_data["tests"]:
            for param_name in test.get("parameters_used", {}).keys():
                param_names.add(param_name)
        
        for param_name in sorted(param_names):
            parameters.append({
                "name": param_name,
                "in": "query",
                "required": param_name in ["fsym", "tsym", "fsyms", "tsyms"],
                "schema": {"type": "string"},
                "description": f"Parameter {param_name}"
            })
        
        # Build operation
        operation = {
            "summary": endpoint_data["name"],
            "description": endpoint_data.get("description", ""),
            "operationId": endpoint_path.replace("/", "_").replace("-", "_").strip("_"),
            "tags": [endpoint_data["category"]],
            "parameters": parameters,
            "responses": {
                "200": {
                    "description": "Successful response",
                    "content": {
                        "application/json": {}
                    }
                },
                "400": {
                    "description": "Bad request - invalid parameters"
                },
                "401": {
                    "description": "Unauthorized - invalid or missing API key"
                },
                "429": {
                    "description": "Too many requests - rate limit exceeded"
                },
                "500": {
                    "description": "Internal server error"
                }
            }
        }
        
        # Add example response if available
        if example_response and "response" in example_response:
            operation["responses"]["200"]["content"]["application/json"]["example"] = example_response["response"]
        
        # Add to paths
        if endpoint_path not in spec["paths"]:
            spec["paths"][endpoint_path] = {}
        
        spec["paths"][endpoint_path]["get"] = operation
    
    return spec


def spec_to_yaml(spec: Dict) -> str:
    """Convert spec dict to YAML string."""
    import yaml
    return yaml.dump(spec, default_flow_style=False, sort_keys=False, allow_unicode=True)


def main():
    print("=" * 80)
    print("📄 Generating OpenAPI Specification")
    print("=" * 80)
    
    # Load results
    with open(INPUT_FILE, "r") as f:
        results = json.load(f)
    
    # Generate spec
    spec = generate_openapi_spec(results)
    
    # Save JSON version
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)
    print(f"✅ JSON spec saved: {OUTPUT_JSON}")
    
    # Try to save YAML version
    try:
        import yaml
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            yaml.dump(spec, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print(f"✅ YAML spec saved: {OUTPUT_FILE}")
    except ImportError:
        print("⚠️  PyYAML not installed, skipping YAML output")
        print("   Install with: pip install pyyaml")
    
    print(f"\n📊 Generated specification with:")
    print(f"   - {len(spec['paths'])} endpoints")
    print(f"   - {len(spec['tags'])} categories")
    print(f"\n💡 Use with:")
    print(f"   - Swagger UI: https://editor.swagger.io/")
    print(f"   - Postman: Import OpenAPI spec")
    print(f"   - OpenAPI Generator: openapi-generator-cli generate")


if __name__ == "__main__":
    main()
