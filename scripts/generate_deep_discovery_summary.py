#!/usr/bin/env python3
"""
Generate a comprehensive summary report from deep discovery results.

Creates:
1. Executive summary with statistics
2. Category breakdowns
3. Performance analysis
4. Error patterns
5. Recommendations
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

INPUT_FILE = Path(__file__).parent.parent / "deep_discovery_results.json"
OUTPUT_FILE = Path(__file__).parent.parent / "DEEP_DISCOVERY_SUMMARY.md"

def load_results():
    """Load deep discovery results."""
    with open(INPUT_FILE, "r") as f:
        return json.load(f)

def generate_summary(results):
    """Generate comprehensive summary report."""
    
    md = f"""# Deep Discovery Summary - CryptoCompare MinAPI

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Discovery Started**: {results['metadata']['timestamp']}  
**Base URL**: {results['metadata']['base_url']}

---

## 📊 Executive Summary

| Metric | Value |
|--------|-------|
| **Total Endpoints** | {results['metadata']['total_endpoints']} |
| **Total Tests Performed** | {results['metadata']['total_tests']} |
| **Successful Tests** | {results['metadata']['successful_tests']} |
| **Failed Tests** | {results['metadata']['total_tests'] - results['metadata']['successful_tests']} |
| **Overall Success Rate** | {results['metadata']['successful_tests'] / results['metadata']['total_tests'] * 100:.2f}% |

---

## 📁 Category Breakdown

"""
    
    # Organize by category
    categories = defaultdict(list)
    for endpoint_key, endpoint_data in results['endpoints'].items():
        categories[endpoint_data['category']].append((endpoint_key, endpoint_data))
    
    # Category table
    md += "| Category | Endpoints | Tests | Successful | Failed | Success Rate |\n"
    md += "|----------|-----------|-------|------------|--------|-------------|\n"
    
    for category in sorted(categories.keys()):
        endpoints = categories[category]
        total_tests = sum(e[1]['summary']['total_tests'] for e in endpoints)
        successful = sum(e[1]['summary']['successful'] for e in endpoints)
        failed = total_tests - successful
        success_rate = successful / total_tests * 100 if total_tests > 0 else 0
        
        status = "✅" if success_rate == 100 else "⚠️" if success_rate >= 90 else "❌"
        
        md += f"| {status} **{category}** | {len(endpoints)} | {total_tests} | {successful} | {failed} | {success_rate:.1f}% |\n"
    
    md += "\n---\n\n## 🎯 Detailed Category Analysis\n\n"
    
    # Detailed category sections
    for category in sorted(categories.keys()):
        endpoints = categories[category]
        total_tests = sum(e[1]['summary']['total_tests'] for e in endpoints)
        successful = sum(e[1]['summary']['successful'] for e in endpoints)
        success_rate = successful / total_tests * 100 if total_tests > 0 else 0
        
        md += f"### {category}\n\n"
        md += f"**Endpoints**: {len(endpoints)} | **Tests**: {total_tests} | **Success Rate**: {success_rate:.1f}%\n\n"
        
        md += "| Endpoint | Tests | Success | Failed | Rate |\n"
        md += "|----------|-------|---------|--------|------|\n"
        
        for endpoint_key, endpoint_data in sorted(endpoints, key=lambda x: x[1]['summary']['successful'] / max(x[1]['summary']['total_tests'], 1), reverse=True):
            tests = endpoint_data['summary']['total_tests']
            succ = endpoint_data['summary']['successful']
            fail = endpoint_data['summary']['failed']
            rate = succ / tests * 100 if tests > 0 else 0
            status = "✅" if rate == 100 else "⚠️" if rate >= 50 else "❌"
            
            md += f"| {status} `{endpoint_data['endpoint']}` | {tests} | {succ} | {fail} | {rate:.1f}% |\n"
        
        md += "\n"
    
    md += "---\n\n## ⚡ Performance Analysis\n\n"
    
    # Performance metrics
    all_response_times = []
    endpoint_performance = []
    
    for endpoint_key, endpoint_data in results['endpoints'].items():
        response_times = [t['elapsed_ms'] for t in endpoint_data['tests'] if t.get('success') and 'elapsed_ms' in t]
        if response_times:
            avg_time = sum(response_times) / len(response_times)
            endpoint_performance.append((
                endpoint_data['name'],
                endpoint_data['endpoint'],
                avg_time,
                min(response_times),
                max(response_times),
                len(response_times)
            ))
            all_response_times.extend(response_times)
    
    if all_response_times:
        md += f"**Overall Average Response Time**: {sum(all_response_times) / len(all_response_times):.2f}ms  \n"
        md += f"**Fastest Response**: {min(all_response_times):.2f}ms  \n"
        md += f"**Slowest Response**: {max(all_response_times):.2f}ms  \n"
        md += f"**Total Response Time Samples**: {len(all_response_times)}\n\n"
        
        md += "### Top 10 Fastest Endpoints\n\n"
        md += "| Rank | Endpoint | Avg (ms) | Min (ms) | Max (ms) | Samples |\n"
        md += "|------|----------|----------|----------|----------|-------|\n"
        
        for i, (name, endpoint, avg, min_t, max_t, samples) in enumerate(sorted(endpoint_performance, key=lambda x: x[2])[:10], 1):
            md += f"| {i} | `{endpoint}` | {avg:.2f} | {min_t:.2f} | {max_t:.2f} | {samples} |\n"
        
        md += "\n### Top 10 Slowest Endpoints\n\n"
        md += "| Rank | Endpoint | Avg (ms) | Min (ms) | Max (ms) | Samples |\n"
        md += "|------|----------|----------|----------|----------|-------|\n"
        
        for i, (name, endpoint, avg, min_t, max_t, samples) in enumerate(sorted(endpoint_performance, key=lambda x: x[2], reverse=True)[:10], 1):
            md += f"| {i} | `{endpoint}` | {avg:.2f} | {min_t:.2f} | {max_t:.2f} | {samples} |\n"
    
    md += "\n---\n\n## ❌ Error Analysis\n\n"
    
    # Collect errors
    errors = []
    for endpoint_key, endpoint_data in results['endpoints'].items():
        for test in endpoint_data['tests']:
            if not test.get('success'):
                errors.append({
                    'endpoint': endpoint_data['endpoint'],
                    'name': endpoint_data['name'],
                    'error': test.get('error') or test.get('error_message', 'Unknown error'),
                    'params': test.get('parameters_used', {})
                })
    
    if errors:
        md += f"**Total Errors**: {len(errors)}\n\n"
        
        # Group by error type
        error_types = defaultdict(list)
        for error in errors:
            error_types[error['error']].append(error)
        
        md += "### Error Types\n\n"
        md += "| Error Type | Count | Endpoints Affected |\n"
        md += "|------------|-------|-------------------|\n"
        
        for error_type, error_list in sorted(error_types.items(), key=lambda x: len(x[1]), reverse=True):
            affected_endpoints = set(e['endpoint'] for e in error_list)
            md += f"| {error_type} | {len(error_list)} | {len(affected_endpoints)} |\n"
        
        md += "\n### Failed Tests Details\n\n"
        for error in errors[:20]:  # Show first 20
            md += f"**Endpoint**: `{error['endpoint']}`  \n"
            md += f"**Error**: {error['error']}  \n"
            if error['params']:
                md += f"**Parameters**: {', '.join(f'{k}={v}' for k, v in error['params'].items())}  \n"
            md += "\n"
    else:
        md += "🎉 **No errors encountered!** All tests passed successfully.\n\n"
    
    md += "---\n\n## 💡 Key Findings\n\n"
    
    # Calculate some insights
    perfect_endpoints = sum(1 for e in results['endpoints'].values() if e['summary']['failed'] == 0)
    problematic_endpoints = sum(1 for e in results['endpoints'].values() if e['summary']['successful'] / max(e['summary']['total_tests'], 1) < 0.5)
    
    md += f"1. **{perfect_endpoints}** out of **{results['metadata']['total_endpoints']}** endpoints had 100% success rate\n"
    md += f"2. **{problematic_endpoints}** endpoints had less than 50% success rate\n"
    md += f"3. **{results['metadata']['total_tests']}** total parameter combinations tested\n"
    
    if all_response_times:
        md += f"4. Average API response time: **{sum(all_response_times) / len(all_response_times):.2f}ms**\n"
    
    md += "\n---\n\n## 🎓 Recommendations\n\n"
    
    md += "1. **Production Readiness**: All endpoints with 100% success rate are ready for production use\n"
    md += "2. **Error Handling**: Implement proper error handling for endpoints with failures\n"
    md += "3. **Rate Limiting**: Monitor rate limit headers on all requests\n"
    md += "4. **Caching**: Consider caching responses for frequently accessed, slow endpoints\n"
    md += "5. **Testing**: Continue testing with edge cases and invalid parameters\n\n"
    
    md += "---\n\n"
    md += f"*Report generated from deep discovery results at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
    
    return md

def main():
    print("📊 Generating Deep Discovery Summary...")
    results = load_results()
    summary = generate_summary(results)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(summary)
    
    print(f"✅ Summary saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
