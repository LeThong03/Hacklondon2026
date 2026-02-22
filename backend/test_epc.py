# test_epc.py

from dotenv import load_dotenv
load_dotenv()   # MUST be first before any app imports

from app import create_app
from app.services.epc_service import get_epc_by_postcode

# Create Flask app — this initialises MongoDB
app = create_app()

with app.app_context():
    r = get_epc_by_postcode('E5')
    print(f'Got {len(r)} records')
    print(f'First address: {r[0]["address"]}')
    print(f'First EPC band: {r[0]["epc_band"]}')