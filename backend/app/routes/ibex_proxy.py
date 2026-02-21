from flask import Blueprint, current_app, jsonify, request
from ..services.ibex_service import IbexService

bp = Blueprint("ibex_proxy", __name__)

def svc():
    return IbexService(current_app.config["IBEX_BASE_URL"], current_app.config["IBEX_JWT"])

@bp.post("/ibex/search")
def proxy_search():
    status, data = svc().post("/search", request.get_json(force=True))
    return jsonify(data), status

@bp.post("/ibex/applications")
def proxy_applications():
    status, data = svc().post("/applications", request.get_json(force=True))
    return jsonify(data), status

@bp.post("/ibex/stats")
def proxy_stats():
    status, data = svc().post("/stats", request.get_json(force=True))
    return jsonify(data), status