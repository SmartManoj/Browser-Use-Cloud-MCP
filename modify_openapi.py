import httpx
import json
import os

def modify_openapi_spec():
    """Fetch and modify OpenAPI specification to create clean tool names"""
    
    # Fetch the original OpenAPI spec
    spec_url = 'https://api.browser-use.com/openapi.json'
    response = httpx.get(spec_url)
    spec = response.json()
    
    # Create a copy of the spec to modify
    modified_spec = spec.copy()
        
    # Modify operationId in the paths
    for path, path_item in modified_spec['paths'].items():
        for method, operation in path_item.items():
            if isinstance(operation, dict) and 'operationId' in operation:
                operation['operationId'] = operation['operationId'].split('_api_v1_')[0]
    
    # Save the modified spec
    output_file = 'modified_openapi.json'
    with open(output_file, 'w') as f:
        json.dump(modified_spec, f, indent=2)
    
    print(f"\nModified OpenAPI spec saved to: {output_file}")
    return output_file

if __name__ == "__main__":
    modify_openapi_spec()