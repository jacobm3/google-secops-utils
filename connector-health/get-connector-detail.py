#!/usr/bin/env python3
#
# Get details of a SOAR connector based on connector ID
#
# jmarts@google.com
#

import argparse
import json
import os
import requests

path = "/api/external/v1/connectors/{identifier}"
api_key = os.environ.get("SOAR_API_KEY")
hostname = os.environ.get("SOAR_HOSTNAME")

if api_key is None:
    raise ValueError("SOAR_API_KEY environment variable not set.")

if hostname is None:
    raise ValueError("SOAR_HOSTNAME environment variable not set.")

# Argument parsing
parser = argparse.ArgumentParser(description="Get Siemplify connector details.")
parser.add_argument("identifier", help="Connector identifier")
args = parser.parse_args()

# Construct URL with identifier
url = f"https://{hostname}{path.format(identifier=args.identifier)}"
headers = {"AppKey": api_key}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"Error during API request: {e}")
