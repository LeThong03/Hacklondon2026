from flask import Blueprint, request, jsonify
from app.services.scoring_service import analyse_postcode

bp = Blueprint("analysis", __name__)

@bp.route("/analyse", methods=["GET"])
def analyse():
    postcode = request.args.get("postcode", "").strip()
    if not postcode:
        return jsonify({"error": "postcode parameter required"}), 400
    try:
        result = analyse_postcode(postcode)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

'''@bp.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200
'''