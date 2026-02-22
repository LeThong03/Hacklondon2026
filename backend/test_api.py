# test_api.py - updated
from dotenv import load_dotenv
load_dotenv()

from app import create_app

app = create_app()

# Print ALL registered routes
print("=== Registered Routes ===")
for rule in app.url_map.iter_rules():
    print(f"{rule.methods} {rule.rule}")

with app.test_client() as client:
    r = client.get('/api/health')
    print(f'\nHealth: {r.get_json()}')

    # URL-encode the space
    r = client.get('/api/analyse?postcode=E5%200LP')
    print(f'Status: {r.status_code}')
    print(f'Response: {r.get_json()}')