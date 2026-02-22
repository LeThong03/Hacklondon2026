import os

class Config:
    PORT = int(os.getenv("PORT", "5000"))
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/retrofitIQ")
    CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "86400"))

    IBEX_BASE_URL = os.getenv("IBEX_BASE_URL", "https://ibex.seractech.co.uk").rstrip("/")
    IBEX_JWT = os.getenv("IBEX_JWT", "")

    # EPC update
    EPC_EMAIL = os.environ.get("EPC_EMAIL")
    EPC_API_KEY = os.environ.get("EPC_API_KEY")