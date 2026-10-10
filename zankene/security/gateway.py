import asyncio
import logging

class ZankeneSecurityGateway:
    def __init__(self, rate_limit_max=3):
        self.valid_tokens = {"ZANKENE_SECRET_TOKEN_999", "ZANKENE_ADMIN_KEY_100"}
        self.rate_limit_max = rate_limit_max
        self.request_counts = {}
        logging.info("🛡️ [ZANKENE SECURITY] Gateway & Rate Limiter Active.")

    async def authenticate_and_route(self, client_id, auth_token, endpoint):
        if auth_token not in self.valid_tokens:
            logging.error(f"❌ [AUTH FAILED] Client '{client_id}' -> Blocked!")
            return {"status": 401, "error": "UNAUTHORIZED"}

        count = self.request_counts.get(client_id, 0)
        if count >= self.rate_limit_max:
            logging.warning(f"⚠️ [RATE LIMIT] Client '{client_id}' Throttled!")
            return {"status": 429, "error": "TOO_MANY_REQUESTS"}

        self.request_counts[client_id] = count + 1
        logging.info(f"⚡ [GATEWAY] Client '{client_id}' -> Passed to '{endpoint}'")
        return {"status": 200, "data": "OK"}