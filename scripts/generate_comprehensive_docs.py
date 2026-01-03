#!/usr/bin/env python3
"""
Generate comprehensive documentation from deep discovery results.

Creates:
1. Detailed markdown documentation per endpoint
2. Code examples in multiple languages
3. Response schema documentation
4. Error handling guides
5. Best practices and usage patterns
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

INPUT_FILE = Path(__file__).parent.parent / "deep_discovery_results.json"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "comprehensive_api_docs"

class DocumentationGenerator:
    """Generate comprehensive API documentation."""
    
    def __init__(self):
        self.results = None
        self.output_dir = OUTPUT_DIR
        self.output_dir.mkdir(exist_ok=True, parents=True)
        
    def load_results(self):
        """Load deep discovery results."""
        with open(INPUT_FILE, "r") as f:
            self.results = json.load(f)
    
    def generate_python_example(self, endpoint: str, test: Dict) -> str:
        """Generate Python code example."""
        params = test.get("parameters_used", {})
        
        code = f'''import requests

# Endpoint: {endpoint}
url = "{test["url"]}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {{response.status_code}}")
'''
        
        if params:
            code += f"\n# Parameters used:\n"
            for key, value in params.items():
                code += f"# - {key}: {value}\n"
        
        return code
    
    def generate_curl_example(self, test: Dict) -> str:
        """Generate cURL example."""
        return f'curl -X GET "{test["url"]}"'
    
    def generate_javascript_example(self, endpoint: str, test: Dict) -> str:
        """Generate JavaScript/Node.js example."""
        params = test.get("parameters_used", {})
        
        code = f'''// Endpoint: {endpoint}
const url = "{test["url"]}";

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
'''
        
        return code
    
    def format_response_schema(self, response: Any, indent: int = 0) -> str:
        """Format response data as schema documentation."""
        indent_str = "  " * indent
        
        if isinstance(response, dict):
            lines = [f"{indent_str}{{"]
            for key, value in list(response.items())[:5]:  # Show first 5 keys
                if isinstance(value, (dict, list)):
                    type_name = type(value).__name__
                    lines.append(f"{indent_str}  '{key}': <{type_name}>")
                else:
                    lines.append(f"{indent_str}  '{key}': {repr(value)}")
            
            if len(response) > 5:
                lines.append(f"{indent_str}  ... ({len(response) - 5} more fields)")
            lines.append(f"{indent_str}}}")
            return "\n".join(lines)
        
        elif isinstance(response, list):
            if response:
                return f"{indent_str}[<{type(response[0]).__name__}>, ...] (length: {len(response)})"
            return f"{indent_str}[]"
        
        else:
            return f"{indent_str}{repr(response)}"
    
    def generate_endpoint_doc(self, endpoint_key: str, endpoint_data: Dict) -> str:
        """Generate comprehensive markdown documentation for an endpoint."""
        
        doc = f'''# {endpoint_data["name"]}

**Endpoint**: `{endpoint_data["endpoint"]}`  
**Category**: {endpoint_data["category"]}  
**Documentation**: [{endpoint_data.get("doc_url", "N/A")}]({endpoint_data.get("doc_url", "#")})

## Description

{endpoint_data.get("description", "No description available.")}

## Parameters

'''
        
        # Parameters table
        if endpoint_data.get("parameters"):
            doc += "| Parameter | Type | Required | Description |\n"
            doc += "|-----------|------|----------|-------------|\n"
            for param in endpoint_data["parameters"]:
                doc += f"| `{param}` | string | TBD | TBD |\n"
        else:
            doc += "No parameters required.\n"
        
        doc += "\n## Test Results\n\n"
        doc += f"**Total Tests**: {endpoint_data['summary']['total_tests']}  \n"
        doc += f"**Successful**: {endpoint_data['summary']['successful']}  \n"
        doc += f"**Failed**: {endpoint_data['summary']['failed']}  \n"
        doc += f"**Success Rate**: {endpoint_data['summary']['successful'] / max(endpoint_data['summary']['total_tests'], 1) * 100:.1f}%\n\n"
        
        # Get first successful test for examples
        successful_tests = [t for t in endpoint_data["tests"] if t.get("success")]
        
        if successful_tests:
            first_test = successful_tests[0]
            
            doc += "## Example Usage\n\n"
            
            # cURL
            doc += "### cURL\n\n```bash\n"
            doc += self.generate_curl_example(first_test)
            doc += "\n```\n\n"
            
            # Python
            doc += "### Python\n\n```python\n"
            doc += self.generate_python_example(endpoint_data["endpoint"], first_test)
            doc += "```\n\n"
            
            # JavaScript
            doc += "### JavaScript\n\n```javascript\n"
            doc += self.generate_javascript_example(endpoint_data["endpoint"], first_test)
            doc += "```\n\n"
            
            # Response example
            if "response" in first_test:
                doc += "## Example Response\n\n```json\n"
                response_preview = first_test["response"]
                
                # Limit response size for documentation
                if isinstance(response_preview, dict):
                    limited_response = {k: v for k, v in list(response_preview.items())[:10]}
                    if len(response_preview) > 10:
                        limited_response["..."] = f"({len(response_preview) - 10} more fields)"
                    doc += json.dumps(limited_response, indent=2)
                elif isinstance(response_preview, list):
                    doc += json.dumps(response_preview[:3], indent=2)
                    if len(response_preview) > 3:
                        doc += f"\n// ... ({len(response_preview) - 3} more items)"
                else:
                    doc += json.dumps(response_preview, indent=2)
                
                doc += "\n```\n\n"
            
            # Response schema
            doc += "## Response Schema\n\n"
            if "response_keys" in first_test:
                doc += "**Top-level keys**: " + ", ".join(f"`{k}`" for k in first_test["response_keys"]) + "\n\n"
            
            if "data_count" in first_test:
                doc += f"**Data items**: {first_test['data_count']}\n\n"
            
            if "data_keys" in first_test:
                doc += "**Data object keys**: " + ", ".join(f"`{k}`" for k in first_test["data_keys"]) + "\n\n"
            
            # Performance
            doc += "## Performance\n\n"
            response_times = [t.get("elapsed_ms", 0) for t in successful_tests if t.get("success")]
            if response_times:
                doc += f"**Average Response Time**: {sum(response_times) / len(response_times):.2f}ms  \n"
                doc += f"**Min Response Time**: {min(response_times):.2f}ms  \n"
                doc += f"**Max Response Time**: {max(response_times):.2f}ms  \n\n"
            
            # Rate limiting
            first_rate_limit = first_test.get("rate_limit", {})
            if any(first_rate_limit.values()):
                doc += "## Rate Limiting\n\n"
                if first_rate_limit.get("limit"):
                    doc += f"**Limit**: {first_rate_limit['limit']}  \n"
                if first_rate_limit.get("remaining"):
                    doc += f"**Remaining**: {first_rate_limit['remaining']}  \n"
                if first_rate_limit.get("reset"):
                    doc += f"**Reset**: {first_rate_limit['reset']}  \n"
                doc += "\n"
        
        # Test variations
        doc += "## Tested Parameter Combinations\n\n"
        doc += "| Test # | Parameters | Status | Response Time |\n"
        doc += "|--------|------------|--------|---------------|\n"
        
        for i, test in enumerate(endpoint_data["tests"], 1):
            params_str = ", ".join(f"{k}={v}" for k, v in test.get("parameters_used", {}).items()) or "None"
            status = "✅ Success" if test.get("success") else f"❌ Failed ({test.get('error', 'Unknown')})"
            response_time = f"{test.get('elapsed_ms', 'N/A')}ms" if test.get("elapsed_ms") else "N/A"
            doc += f"| {i} | {params_str} | {status} | {response_time} |\n"
        
        doc += "\n---\n\n"
        doc += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from deep discovery results*\n"
        
        return doc
    
    def generate_category_index(self, category: str, endpoints: List[tuple]) -> str:
        """Generate index page for a category."""
        
        doc = f"# {category} Endpoints\n\n"
        doc += f"**Total Endpoints**: {len(endpoints)}\n\n"
        doc += "## Endpoints\n\n"
        
        for endpoint_key, endpoint_data in endpoints:
            success_rate = endpoint_data['summary']['successful'] / max(endpoint_data['summary']['total_tests'], 1) * 100
            status_icon = "✅" if success_rate == 100 else "⚠️" if success_rate > 50 else "❌"
            
            doc += f"### {status_icon} [{endpoint_data['name']}](./{endpoint_key.replace('/', '_')}.md)\n\n"
            doc += f"**Endpoint**: `{endpoint_data['endpoint']}`  \n"
            doc += f"**Success Rate**: {success_rate:.1f}%  \n"
            doc += f"**Tests**: {endpoint_data['summary']['total_tests']}  \n"
            doc += f"{endpoint_data.get('description', '')}\n\n"
        
        return doc
    
    def generate_master_index(self, categories: Dict[str, List]) -> str:
        """Generate master index of all documentation."""
        
        doc = "# CryptoCompare MinAPI - Comprehensive Documentation\n\n"
        doc += f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n"
        doc += f"**Total Endpoints**: {self.results['metadata']['total_endpoints']}  \n"
        doc += f"**Total Tests**: {self.results['metadata']['total_tests']}  \n"
        doc += f"**Success Rate**: {self.results['metadata']['successful_tests'] / self.results['metadata']['total_tests'] * 100:.1f}%\n\n"
        
        doc += "## Categories\n\n"
        
        for category, endpoints in sorted(categories.items()):
            doc += f"### [{category}](./{category.replace(' ', '_')}/index.md)\n\n"
            doc += f"**Endpoints**: {len(endpoints)}  \n"
            
            # Calculate category statistics
            total_tests = sum(e[1]['summary']['total_tests'] for e in endpoints)
            successful = sum(e[1]['summary']['successful'] for e in endpoints)
            success_rate = successful / max(total_tests, 1) * 100
            
            doc += f"**Tests**: {total_tests}  \n"
            doc += f"**Success Rate**: {success_rate:.1f}%  \n\n"
        
        return doc
    
    def generate_all_docs(self):
        """Generate all documentation files."""
        print("=" * 80)
        print("📝 Generating Comprehensive Documentation")
        print("=" * 80)
        
        self.load_results()
        
        # Group endpoints by category
        categories = {}
        for endpoint_key, endpoint_data in self.results["endpoints"].items():
            category = endpoint_data["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append((endpoint_key, endpoint_data))
        
        # Generate category directories and docs
        for category, endpoints in categories.items():
            category_dir = self.output_dir / category.replace(" ", "_")
            category_dir.mkdir(exist_ok=True, parents=True)
            
            print(f"\n📁 Category: {category} ({len(endpoints)} endpoints)")
            
            # Generate category index
            category_index = self.generate_category_index(category, endpoints)
            category_index_file = category_dir / "index.md"
            with open(category_index_file, "w", encoding="utf-8") as f:
                f.write(category_index)
            print(f"  ✅ Created: {category_index_file.relative_to(self.output_dir)}")
            
            # Generate individual endpoint docs
            for endpoint_key, endpoint_data in endpoints:
                endpoint_doc = self.generate_endpoint_doc(endpoint_key, endpoint_data)
                endpoint_file = category_dir / f"{endpoint_key.replace('/', '_')}.md"
                with open(endpoint_file, "w", encoding="utf-8") as f:
                    f.write(endpoint_doc)
                print(f"  ✅ Created: {endpoint_file.relative_to(self.output_dir)}")
        
        # Generate master index
        master_index = self.generate_master_index(categories)
        master_index_file = self.output_dir / "README.md"
        with open(master_index_file, "w", encoding="utf-8") as f:
            f.write(master_index)
        
        print(f"\n📄 Master index: {master_index_file}")
        print("\n✅ Documentation generation complete!")
        print(f"📂 Output directory: {self.output_dir}")

def main():
    generator = DocumentationGenerator()
    generator.generate_all_docs()

if __name__ == "__main__":
    main()
