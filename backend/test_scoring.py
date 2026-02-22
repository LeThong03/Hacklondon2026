# test_scoring.py
from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.services.scoring_service import analyse_postcode

app = create_app()
with app.app_context():
    result = analyse_postcode('E5')
    print(f'Postcode: {result["postcode"]}')
    print(f'Avg score: {result["avg_score"]}')
    print(f'Flood zone: {result["flood_zone"]}')
    print(f'Constraints: {result["constraints"]}')
    print(f'Top property: {result["properties"][0]["address"]} — {result["properties"][0]["score"]} ({result["properties"][0]["rating"]})')