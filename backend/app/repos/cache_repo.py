from datetime import datetime, timedelta, timezone
from ..extensions import db

def col():
    return db()["retrofit_cache"]

def get_cached(key: str, ttl_seconds: int):
    doc = col().find_one({"key": key})
    if not doc:
        return None
    created_at = doc.get("createdAt")
    if not created_at:
        return None
    if datetime.now(timezone.utc) - created_at > timedelta(seconds=ttl_seconds):
        return None
    doc["_id"] = str(doc["_id"])
    return doc.get("value")

def set_cached(key: str, value: dict):
    col().update_one(
        {"key": key},
        {"$set": {"key": key, "value": value, "createdAt": datetime.now(timezone.utc)}},
        upsert=True
    )