# test_env.py
from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.config import Config

app = create_app()
with app.app_context():
    print(f"EPC_API_KEY from Config: {repr(Config.EPC_API_KEY)}")
    print(f"Length: {len(Config.EPC_API_KEY) if Config.EPC_API_KEY else 0}")