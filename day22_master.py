import asyncio
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 22 GOVERNOR] - %(levelname)s - %(message)s'
)

class Day22RateLimiterGovernor:
    def __init__(self, max_concurrent=2, delay_between_requests=0.5):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.delay = delay_between_requests
        logging.info(f"ZANKENE Day 22 Rate Limiter Governor Active (Max Concurrent: {max_concurrent}).")

    async def execute_rate_limited_api_call(self, call_id, endpoint):
        async with self.semaphore:
            logging.info(f"🔒 [TOKEN ACQUIRED] Processing API Request #{call_id} -> {endpoint}")
            await asyncio.sleep(self.delay)
            logging.info(f"🔓 [TOKEN RELEASED] Successfully executed Request #{call_id}")
            return f"Result #{call_id}"

    async def run_day22_pipeline(self):
        print("\n=======================================================")
        print("🚦 ZANKENE DAY 22: ADAPTIVE RATE LIMITER GOVERNOR 🚦")
        print("=======================================================\n")
        
        requests = [
            (1, "https://api.openai.com/v1/chat/completions"),
            (2, "https://api.gemini.google.com/v1/generate"),
            (3, "https://api.stripe.com/v1/charges"),
            (4, "https://api.github.com/user/repos"),
            (5, "https://api.sendgrid.com/v3/mail/send")
        ]

        tasks = [self.execute_rate_limited_api_call(cid, ep) for cid, ep in requests]
        await asyncio.gather(*tasks)

        print("\n🎉 Day 22 Rate Limiter & API Traffic Control Completed Successfully!")

if __name__ == "__main__":
    governor = Day22RateLimiterGovernor()
    asyncio.run(governor.run_day22_pipeline())