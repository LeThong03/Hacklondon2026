from datetime import datetime, timedelta, timezone
from ..extensions import db

def col():
    return db()["retrofit_cache"]

def _to_utc_naive(dt):
    if dt is None:
        return None
    # if dt is timezone-aware, convert to UTC then drop tz
    if dt.tzinfo is not None:
        return dt.astimezone(timezone.utc).replace(tzinfo=None)
    # if dt is naive, assume it is already UTC
    return dt

def get_cached(key: str, ttl_seconds: int):
    doc = col().find_one({"key": key})
    if not doc:
        return None

    created_at = _to_utc_naive(doc.get("createdAt"))
    if not created_at:
        return None

    now = datetime.utcnow()  # naive UTC
    if now - created_at > timedelta(seconds=ttl_seconds):
        return None

    return doc.get("value")

def set_cached(key: str, value: dict):
    col().update_one(
        {"key": key},
        {"$set": {"key": key, "value": value, "createdAt": datetime.utcnow()}},
        upsert=True
    )