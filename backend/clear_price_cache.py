# clear_price_cache.py
from dotenv import load_dotenv
load_dotenv()
from app import create_app
from app.extensions import db

app = create_app()
with app.app_context():
    r = db().cache.delete_many({"key": {"$regex": "^price:"}})
    print(f"Cleared {r.deleted_count} price cache entries")