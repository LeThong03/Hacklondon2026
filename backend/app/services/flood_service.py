import requests
from app.config import Config
from app.repos.cache_repo import get_cached, set_cached

def postcode_to_latlong(postcode: str) -> tuple:
    cache_key = f"latlong:{postcode.replace(' ', '')}"
    cached = get_cached(cache_key, Config.CACHE_TTL_SECONDS)
    if cached:
        return tuple(cached)
    try:
        clean = postcode.replace(' ', '')
        # Try full postcode first
        resp = requests.get(
            f"https://api.postcodes.io/postcodes/{clean}",
            timeout=5
        )
        result = resp.json().get("result")

        # If that fails, try outcode endpoint
        if not result:
            resp = requests.get(
                f"https://api.postcodes.io/outcodes/{clean}",
                timeout=5
            )
            result = resp.json().get("result", {})

        lat = float(result.get("latitude", 51.5074))
        lng = float(result.get("longitude", -0.1278))
    except Exception:
        lat, lng = 51.5074, -0.1278
    set_cached(cache_key, [lat, lng])
    return (lat, lng)


def get_flood_risk(lat: float, lng: float) -> str:
    cache_key = f"flood:{round(lat,3)}:{round(lng,3)}"
    cached = get_cached(cache_key, Config.CACHE_TTL_SECONDS)
    if cached:
        return cached
    try:
        resp = requests.get(
            "https://www.planning.data.gov.uk/entity.json",
            params={"dataset": "flood-risk-zone",
                    "latitude": lat, "longitude": lng, "radius": 200},
            timeout=8
        )
        entities = resp.json().get("entities", [])
        zone = "Zone 1"
        for e in entities:
            flood_type = str(e.get("flood-risk-type", ""))
            if "3" in flood_type:
                zone = "Zone 3"
                break
            elif "2" in flood_type:
                zone = "Zone 2"
    except Exception:
        zone = "Zone 1"
    set_cached(cache_key, zone)
    return zone