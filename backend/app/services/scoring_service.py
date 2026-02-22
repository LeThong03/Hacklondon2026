# backend/app/services/scoring_service.py
from app.services.epc_service import get_epc_by_postcode, get_epc_by_area
from app.services.flood_service import postcode_to_latlong, get_flood_risk
from app.services.constraints_service import get_all_constraints
from app.services.price_service import get_price_stats

EPC_SCORES   = {"A": 100, "B": 85, "C": 70, "D": 50, "E": 30, "F": 15, "G": 5}
FLOOD_SCORES = {"Zone 1": 100, "Zone 2": 50, "Zone 3": 10}

def score_property(epc_band: str, flood_zone: str, constraints: dict) -> dict:
    epc_score   = EPC_SCORES.get(epc_band.upper(), 50)
    flood_score = FLOOD_SCORES.get(flood_zone, 50)

    constraint_penalty = 0
    if constraints.get("article4"):     constraint_penalty += 15
    if constraints.get("conservation"): constraint_penalty += 10
    if constraints.get("green_belt"):   constraint_penalty += 20

    raw = (epc_score * 0.4) + (flood_score * 0.4) + ((100 - constraint_penalty) * 0.2)
    final = round(max(0, min(100, raw)), 1)

    if final >= 75:   rating = "Excellent"
    elif final >= 55: rating = "Good"
    elif final >= 35: rating = "Fair"
    else:             rating = "Poor"

    return {
        "score":             final,
        "rating":            rating,
        "epc_score":         epc_score,
        "flood_score":       flood_score,
        "constraint_penalty": constraint_penalty,
        "breakdown": {
            "epc":         round(epc_score * 0.4, 1),
            "flood":       round(flood_score * 0.4, 1),
            "constraints": round((100 - constraint_penalty) * 0.2, 1)
        }
    }

def analyse_postcode(postcode: str) -> dict:
    #epc_records = get_epc_by_postcode(postcode)
    epc_records = get_epc_by_area(postcode)
    lat, lng    = postcode_to_latlong(postcode)
    flood_zone  = get_flood_risk(lat, lng)
    constraints = get_all_constraints(lat, lng)
    price_data  = get_price_stats(postcode)          # ← add this

    scored = []
    for prop in epc_records:
        s = score_property(prop["epc_band"], flood_zone, constraints)
        scored.append({**prop, **s, "flood_zone": flood_zone,
                       "constraints": constraints})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return {
        "postcode":    postcode,
        "flood_zone":  flood_zone,
        "constraints": constraints,
        "price_data":  price_data,                   # ← add this
        "properties":  scored,
        "avg_score":   round(sum(p["score"] for p in scored) / len(scored), 1) if scored else 0
    }