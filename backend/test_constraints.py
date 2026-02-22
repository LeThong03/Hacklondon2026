# test_constraints.py
from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.services.flood_service import postcode_to_latlong
from app.services.constraints_service import get_all_constraints

app = create_app()
with app.app_context():
    lat, lng = postcode_to_latlong('E5')
    print(f'Coords: {lat}, {lng}')
    print(f'Constraints: {get_all_constraints(lat, lng)}')