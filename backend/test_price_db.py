# test_price_db.py
from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.extensions import db

app = create_app()
with app.app_context():
    count = db().price_paid.count_documents({})
    print(f"Total records in MongoDB: {count}")

    # Check what postcodes look like in the DB
    sample = db().price_paid.find_one({})
    print(f"Sample postcode: {sample.get('postcode')}")
    print(f"Sample postcode_clean: {sample.get('postcode_clean')}")

    # Try direct lookup for E5
    e5_count = db().price_paid.count_documents(
        {"postcode_clean": {"$regex": "^E50"}}
    )
    print(f"E5 0xx records: {e5_count}")