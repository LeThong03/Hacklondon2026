from flask import Blueprint, current_app, jsonify, request
from ..repos.cache_repo import get_cached, set_cached
from ..services.rps_service import calculate_rps

bp = Blueprint("retrofit", __name__)

@bp.get("/retrofit")
def retrofit():
    postcode = request.args.get("postcode", "").strip()
    if not postcode:
        return jsonify({"message": "Bad Request", "error": "postcode is required"}), 400

    key = f"retrofit:{postcode.upper()}"
    cached = get_cached(key, current_app.config["CACHE_TTL_SECONDS"])
    if cached:
        return jsonify({"cached": True, **cached}), 200

    result = calculate_rps(postcode)
    set_cached(key, result)
    return jsonify({"cached": False, **result}), 200