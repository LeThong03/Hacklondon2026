import requests
import random
from app.config import Config
from app.repos.cache_repo import get_cached, set_cached

HEATING_MAP = {
    "mains gas": "gas boiler",
    "gas":       "gas boiler",
    "electric":  "electric heating",
    "oil":       "oil boiler",
    "heat pump": "heat pump",
    "community": "district heating",
}

def _clean_heating(raw: str) -> str:
    if not raw:
        return "unknown"
    raw = raw.lower()
    for key, label in HEATING_MAP.items():
        if key in raw:
            return label
    return raw

def _get_latlong(postcode: str) -> tuple:
    """Geocode postcode via postcodes.io — tries full then outcode."""
    try:
        clean = postcode.replace(" ", "")
        resp = requests.get(
            f"https://api.postcodes.io/postcodes/{clean}", timeout=5
        )
        result = resp.json().get("result")
        if not result:
            resp = requests.get(
                f"https://api.postcodes.io/outcodes/{clean}", timeout=5
            )
            result = resp.json().get("result", {})
        return (
            float(result.get("latitude",  51.5074)),
            float(result.get("longitude", -0.1278))
        )
    except Exception:
        return (51.5074, -0.1278)


def get_epc_by_postcode(postcode: str) -> list:
    cache_key = f"epc:{postcode.replace(' ', '').upper()}"
    cached = get_cached(cache_key, Config.CACHE_TTL_SECONDS)
    if cached:
        print(f"[EPC] Cache hit for {cache_key}")
        return cached

    print(f"[EPC] Calling EPC API for {postcode}")

    headers = {
        "Authorization": f"Basic {Config.EPC_API_KEY.strip()}",
        "Accept": "application/json"
    }
    params = {"postcode": postcode.strip(), "size": 100}

    try:
        resp = requests.get(
            "https://epc.opendatacommunities.org/api/v1/domestic/search",
            headers=headers,
            params=params,
            timeout=8
        )
        print(f"[EPC] Status {resp.status_code}")
        if resp.status_code == 401:
            print("EPC API: 401 Unauthorized — using mock")
            return _mock_epc_data(postcode)

        rows = resp.json().get("rows", [])
    except Exception as e:
        print(f"EPC API failed for {postcode}: {e} — using mock")
        return _mock_epc_data(postcode)

    # Geocode once for base coordinates
    base_lat, base_lng = _get_latlong(postcode)

    records = []
    for i, r in enumerate(rows):
        try:
            # Spread properties in a ~400m radius around postcode centre
            random.seed(hash(r.get("uprn", str(i))) & 0xFFFF)
            lat = base_lat + random.uniform(-0.003, 0.003)
            lng = base_lng + random.uniform(-0.005, 0.005)

            records.append({
                "uprn":                 r.get("uprn", ""),
                "address":              f"{r.get('address1', '')} {r.get('address2', '')}".strip(),
                "postcode":             r.get("postcode", postcode),
                "epc_band":             r.get("current-energy-rating", "D"),
                "floor_area_m2":        float(r.get("total-floor-area") or 0),
                "heating_type":         _clean_heating(r.get("main-fuel", "")),
                "current_kwh_per_year": float(r.get("energy-consumption-current") or 0),
                "construction_age":     r.get("construction-age-band", "unknown"),
                "lat":                  round(lat, 6),
                "lng":                  round(lng, 6),
            })
        except Exception as e:
            print(f"[EPC] Row parse error: {e}")
            continue

    if not records:
        print(f"EPC API returned 0 rows for {postcode} — using mock data")
        return _mock_epc_data(postcode)

    set_cached(cache_key, records)
    return records


def get_epc_by_uprn(uprn: str, postcode: str) -> dict:
    all_records = get_epc_by_postcode(postcode)
    for r in all_records:
        if r["uprn"] == uprn:
            return r
    return all_records[0] if all_records else {}


def get_epc_by_area(postcode: str) -> list:
    """Get EPC records across multiple postcodes within an outcode area."""
    outcode = postcode.strip().split()[0]  # 'E5 0LP' → 'E5', 'E5' → 'E5'
    try:
        resp = requests.get(
            f"https://api.postcodes.io/postcodes?q={outcode}&limit=5",
            timeout=5
        )
        full_postcodes = [r["postcode"] for r in resp.json().get("result", [])]
        if not full_postcodes:
            full_postcodes = [postcode]
    except Exception:
        full_postcodes = [postcode]

    all_records = []
    seen_uprns = set()
    for pc in full_postcodes:
        for record in get_epc_by_postcode(pc):
            if record["uprn"] not in seen_uprns:
                seen_uprns.add(record["uprn"])
                all_records.append(record)

    return all_records if all_records else get_epc_by_postcode(postcode)


def _mock_epc_data(postcode: str) -> list:
    random.seed(hash(postcode) & 0xFFFF)
    bands = ["C", "C", "D", "D", "E", "E", "E", "F", "F", "G"]
    lat, lng = _get_latlong(postcode)
    return [
        {
            "uprn":                 f"MOCK{i:06d}",
            "address":              f"{i*2} Mock Street, {postcode}",
            "postcode":             postcode,
            "epc_band":             bands[i % len(bands)],
            "floor_area_m2":        round(random.uniform(60, 120), 2),
            "heating_type":         "gas boiler",
            "current_kwh_per_year": round(random.uniform(12000, 22000), 2),
            "construction_age":     "1900-1929",
            "lat":                  lat + random.uniform(-0.01, 0.01),
            "lng":                  lng + random.uniform(-0.01, 0.01),
        }
        for i in range(10)
    ]