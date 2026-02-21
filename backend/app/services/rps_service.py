def calculate_rps(postcode: str) -> dict:
    # TODO: plug EPC, Flood, Price Paid, IBEX planning here
    # For now: return stub so frontend can integrate immediately.
    return {
        "postcode": postcode,
        "rps": 74,
        "breakdown": {
            "epc_score": 60,
            "flood_risk": 70,
            "price_delta": 55,
            "planning_history": 80
        }
    }