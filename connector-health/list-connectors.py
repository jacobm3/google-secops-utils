#!/usr/bin/env python3
#
# List SOAR connectors info, including connector ID
#
# jmarts@google.com
#

import json
import os
import requests

path = "/api/external/v1/connectors/cards"
api_key = os.environ.get("SOAR_API_KEY")
hostname = os.environ.get("SOAR_HOSTNAME")

if api_key is None:
    raise ValueError("SOAR_API_KEY environment variable not set.")

if hostname is None:
    raise ValueError("SOAR_HOSTNAME environment variable not set.")

url = f"https://{hostname}{path}"
headers = {"AppKey": api_key}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Process the response data
    data = response.json()
    print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"Error during API request: {e}")
