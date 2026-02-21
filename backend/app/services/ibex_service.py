import requests

class IbexService:
    def __init__(self, base_url: str, jwt: str):
        self.base_url = base_url.rstrip("/")
        self.jwt = jwt

    def _headers(self):
        if not self.jwt:
            raise RuntimeError("Missing IBEX_JWT in .env")
        return {"Authorization": f"Bearer {self.jwt}", "Content-Type": "application/json"}

    def post(self, path: str, payload: dict):
        url = f"{self.base_url}{path}"
        r = requests.post(url, headers=self._headers(), json=payload, timeout=60)
        # safe parse
        try:
            return r.status_code, r.json()
        except Exception:
            return r.status_code, r.text