# clear_epc_cache.py
from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.extensions import db

app = create_app()
with app.app_context():
    result = db().cache.delete_many({"key": {"$regex": "^epc:"}})
    print(f"Cleared {result.deleted_count} EPC cache entries")
    