# test_final.py
from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.services.scoring_service import analyse_postcode

app = create_app()
# Add this temporarily to test_final.py, right after app = create_app()
with app.app_context():
    from app.extensions import db
    result = db().cache.delete_many({"key": {"$regex": "^price:"}})
    print(f"Cleared {result.deleted_count} price cache entries")

with app.app_context():
    result = analyse_postcode('E5 0LP')
    p = result["properties"][0]

    print(f"Total real properties: {len(result['properties'])}")
    print(f"Avg score:   {result['avg_score']}")
    print(f"Flood zone:  {result['flood_zone']}")
    print(f"Constraints: {result['constraints']}")

    print(f"\n--- Top Property ---")
    print(f"Address:    {p['address']}")
    print(f"lat/lng:    {p['lat']}, {p['lng']}")
    print(f"Score:      {p['score']} ({p['rating']})")
    print(f"EPC band:   {p['epc_band']}")
    print(f"Heating:    {p['heating_type']}")

    print(f"\n--- Price Data ---")
    pd = result["price_data"]
    print(f"Transactions: {pd['transactions']}")
    print(f"Avg price:  £{pd['avg_price']:,}" if pd['avg_price'] else "Avg price: No data")
    print(f"Min price:  £{pd['min_price']:,}" if pd['min_price'] else "Min price: No data")
    print(f"Max price:  £{pd['max_price']:,}" if pd['max_price'] else "Max price: No data")
    if pd['recent_sales']:
        s = pd['recent_sales'][0]
        print(f"Latest sale: {s['address']} — £{s['price']:,} ({s['date']}, {s['property_type']}, {s['tenure']})")

    print("\n✅ Backend fully ready for frontend integration")