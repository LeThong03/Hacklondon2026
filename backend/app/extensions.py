from pymongo import MongoClient

_client: MongoClient | None = None

def init_mongo(uri: str) -> None:
    global _client
    _client = MongoClient(uri)

def db():
    if _client is None:
        raise RuntimeError("Mongo not initialised")
    return _client.get_default_database()