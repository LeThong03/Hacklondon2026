# test_epc_raw.py
from dotenv import load_dotenv
load_dotenv()
import requests
import os

token = os.getenv("EPC_API_KEY").strip()
r = requests.get(
    "https://epc.opendatacommunities.org/api/v1/domestic/search",
    headers={"Authorization": f"Basic {token}", "Accept": "application/json"},
    params={"postcode": "E5 0LP", "size": 5}
)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    rows = r.json().get("rows", [])
    print(f"Records: {len(rows)}")
    if rows:
        print(f"First: {rows[0].get('address')} — {rows[0].get('current-energy-rating')}")
else:
    print(f"Error: {r.text[:200]}")