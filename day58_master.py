import asyncio
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 58 API-GATEWAY] - %(levelname)s - %(message)s'
)

class Day58APIGatewayEngine:
    def __init__(self, rate_limit_max=3):
        self.valid_tokens = {"ZANKENE_SECRET_TOKEN_999", "ZANKENE_ADMIN_KEY_100"}
        self.rate_limit_max = rate_limit_max
        self.client_request_counts = {}
        logging.info("🛡️ ZANKENE Day 58 Enterprise API Gateway & Security Core Active.")

    async def handle_request(self, client_id, auth_token, endpoint):
        # 1. Authentication Check
        if auth_token not in self.valid_tokens:
            logging.error(f"❌ [AUTH FAILED] Client '{client_id}' -> Invalid Auth Token! Request Blocked.")
            return {"status": 401, "error": "UNAUTHORIZED"}

        # 2. Rate Limiting Check
        current_count = self.client_request_counts.get(client_id, 0)
        if current_count >= self.rate_limit_max:
            logging.warning(f"⚠️ [RATE LIMIT EXCEEDED] Client '{client_id}' exceeded limit ({self.rate_limit_max} reqs). Request Throttled!")
            return {"status": 429, "error": "TOO_MANY_REQUESTS"}

        self.client_request_counts[client_id] = current_count + 1

        # 3. Route Execution
        logging.info(f"⚡ [GATEWAY ROUTE] Client '{client_id}' -> Valid Request to '{endpoint}' [Req #{current_count + 1}]")
        await asyncio.sleep(0.3)
        return {"status": 200, "data": f"Success response from {endpoint}"}

    async def run_day58_pipeline(self):
        print("\n=================================================================")
        print("🛡️ ZANKENE DAY 58: ENTERPRISE API GATEWAY & RATE LIMITING 🛡️")
        print("=================================================================\n")

        requests = [
            ("Client_Alpha", "ZANKENE_SECRET_TOKEN_999", "/api/v1/leads"),
            ("Client_Alpha", "ZANKENE_SECRET_TOKEN_999", "/api/v1/analytics"),
            ("Client_Alpha", "ZANKENE_SECRET_TOKEN_999", "/api/v1/audit"),
            ("Client_Alpha", "ZANKENE_SECRET_TOKEN_999", "/api/v1/abuse_test"),  # Should hit Rate Limit
            ("Client_Hacker", "INVALID_EXPIRED_TOKEN", "/api/v1/admin_dump")      # Should hit Auth Failure
        ]

        for cid, token, ep in requests:
            await self.handle_request(cid, token, ep)
            await asyncio.sleep(0.1)

        print("\n🎉 Day 58 API Gateway & Rate Limiting Enforcement Complete!")

if __name__ == "__main__":
    gateway = Day58APIGatewayEngine()
    asyncio.run(gateway.run_day58_pipeline())
    