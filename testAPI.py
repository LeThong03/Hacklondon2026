import os
import requests

BASE_URL = "https://ibex.seractech.co.uk"
JWT = os.getenv("IBEX_JWT")
if not JWT:
    raise SystemExit("Set IBEX_JWT env var first")

headers = {
    "Authorization": f"Bearer {JWT}",
    "Content-Type": "application/json",
}

# Example: POST /search (radius search)
payload = {
    "input": {
        "srid": 27700,
        "radius": 300,
        "coordinates": [528583, 186088],  # easting, northing example
        "page": 1,
        "page_size": 50,
        "date_range_type": "any"
    },
    "extensions": {
        "centre_point": True,
        "heading": True,
        "project_type": True,
        "num_new_houses": True,
        "document_metadata": True
    }
}

r = requests.post(f"{BASE_URL}/search", headers=headers, json=payload, timeout=60)
print("status:", r.status_code)
print(r.text[:2000])