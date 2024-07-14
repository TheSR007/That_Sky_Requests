import os
import json
from urllib.parse import urlparse

# Function to extract endpoints from JSON recursively
def extract_endpoints(data, endpoints=set()):
    for entry in data:
        url = entry.get('url', '')
        parsed_url = urlparse(url)
        if parsed_url.scheme == 'https' and parsed_url.netloc == 'live.radiance.thatgamecompany.com':
            endpoint = parsed_url.path.strip('/')
            endpoints.add(endpoint)

# Function to save request and response to {endpoint}.json files
def save_requests_responses(data, endpoint, directory):
    request_header = data.get('request', {}).get('header', '')
    response_header = data.get('response', {}).get('header', '')

    # Create the request and response strings
    request_response_str = f"""/*
{request_header}
*/
//Request


/*
{response_header}
*/
//Response

"""

    # Write to endpoint.json only if it doesn't already exist
    json_filename = os.path.join(directory, f"{endpoint.replace('/', '_')}.json")
    if not os.path.exists(json_filename):
        with open(json_filename, 'w') as f:
            f.write(request_response_str)
            print(f"Created: {json_filename}")

# Read the JSON file
json_file = "Sky_Full.json"
with open(json_file, 'r') as f:
    data = json.load(f)

# Extract endpoints
endpoints = set()
extract_endpoints(data, endpoints)

# Sort endpoints by uniqueness
sorted_endpoints = sorted(endpoints)

# Create directories and save JSON files for each endpoint
cwd = os.getcwd()
for endpoint in sorted_endpoints:
    endpoint_parts = endpoint.split('/')
    for i in range(1, len(endpoint_parts)):
        directory = os.path.join(cwd, '/'.join(endpoint_parts[:i]))
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Find any entry with this endpoint and save its request and response
    for entry in data:
        url = entry.get('url', '')
        parsed_url = urlparse(url)
        if parsed_url.scheme == 'https' and parsed_url.netloc == 'live.radiance.thatgamecompany.com' and parsed_url.path.strip('/') == endpoint:
            save_requests_responses(entry, endpoint, directory)
            break

print("Directories and endpoint JSON files created or updated successfully.")
