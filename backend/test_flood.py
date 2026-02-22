# test_flood.py

from app.extensions import mongo
mongo.db.cache.delete_one({"key": "latlong:E5"})

from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.services.flood_service import postcode_to_latlong, get_flood_risk

app = create_app()
with app.app_context():
    # Test with a FULL postcode to confirm geocoding works at all
    lat, lng = postcode_to_latlong('E5 0LP')
    print(f'Full postcode coords: {lat}, {lng}')

    lat2, lng2 = postcode_to_latlong('E5')
    print(f'Outcode coords: {lat2}, {lng2}')
    print(f'Flood risk: {get_flood_risk(lat2, lng2)}')