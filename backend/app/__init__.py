from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from .config import Config
from .extensions import init_mongo

def create_app() -> Flask:
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    init_mongo(app.config["MONGO_URI"])

    from .routes.health import bp as health_bp
    from .routes.ibex_proxy import bp as ibex_bp
    from .routes.retrofit import bp as retrofit_bp
    from .routes.analysis import bp as analysis_bp


    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(ibex_bp, url_prefix="/api")
    app.register_blueprint(retrofit_bp, url_prefix="/api")
    app.register_blueprint(analysis_bp, url_prefix="/api")
    return app