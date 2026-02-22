# backend/app/services/constraints_service.py
import requests
from app.config import Config
from app.repos.cache_repo import get_cached, set_cached

def _check_constraint(dataset: str, lat: float, lng: float) -> bool:
    cache_key = f"{dataset}:{round(lat,3)}:{round(lng,3)}"
    cached = get_cached(cache_key, Config.CACHE_TTL_SECONDS)
    if cached is not None:
        return cached
    try:
        resp = requests.get(
            "https://www.planning.data.gov.uk/entity.json",
            params={"dataset": dataset, "latitude": lat,
                    "longitude": lng, "radius": 100},
            timeout=8
        )
        result = len(resp.json().get("entities", [])) > 0
    except Exception:
        result = False
    set_cached(cache_key, result)
    return result

def get_all_constraints(lat: float, lng: float) -> dict:
    return {
        "article4":     _check_constraint("article-4-direction", lat, lng),
        "conservation": _check_constraint("conservation-area", lat, lng),
        "green_belt":   _check_constraint("green-belt", lat, lng)
    }