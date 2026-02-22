from app.extensions import db
from app.repos.cache_repo import get_cached, set_cached
from app.config import Config

PROPERTY_TYPE_MAP = {
    "D": "Detached",
    "S": "Semi-detached",
    "T": "Terraced",
    "F": "Flat",
    "O": "Other"
}

def get_price_stats(postcode: str) -> dict:
    cache_key = f"price:{postcode.replace(' ', '').upper()}"
    cached = get_cached(cache_key, Config.CACHE_TTL_SECONDS)
    if cached:
        return cached

    clean = postcode.replace(" ", "").upper()
    outcode = clean[:-3] if len(clean) > 3 else clean  # E50LP → E5

    query = {"postcode_clean": {"$regex": f"^{outcode}"}}  # ← outcode not clean
    docs = list(db().price_paid.find(query, {"_id": 0}).sort("date", -1).limit(50))

    if not docs:
        return {"avg_price": None, "min_price": None,
                "max_price": None, "transactions": 0, "recent_sales": []}

    prices = [d["price"] for d in docs]
    result = {
        "avg_price":    round(sum(prices) / len(prices)),
        "min_price":    min(prices),
        "max_price":    max(prices),
        "transactions": len(docs),
        "recent_sales": [
            {
                "address":       f"{d.get('paon','')} {d.get('saon','')} {d.get('street','')}".strip(),
                "price":         d["price"],
                "date":          d["date"][:10],
                "property_type": PROPERTY_TYPE_MAP.get(d.get("property_type",""), "Unknown"),
                "tenure":        "Freehold" if d.get("tenure") == "F" else "Leasehold",
                "new_build":     d.get("new_build") == "Y"
            }
            for d in docs[:10]
        ]
    }
    set_cached(cache_key, result)
    return result