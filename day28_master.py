import asyncio
import logging
import re

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 28 SANITIZER] - %(levelname)s - %(message)s'
)

class Day28SecuritySanitizer:
    def __init__(self):
        logging.info("ZANKENE Day 28 Security Guard & API Sanitizer Active.")

    def sanitize_payload(self, data_str):
        # Redact API Keys, Passwords, and Secrets using Regex patterns
        sanitized = re.sub(r'(sk-[a-zA-Z0-9]{20,})', '[REDACTED_API_KEY]', data_str)
        sanitized = re.sub(r'(password=[\w@#$]+)', 'password=[REDACTED_SECRET]', sanitized)
        sanitized = re.sub(r'(\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b)', '[REDACTED_EMAIL]', sanitized)
        return sanitized

    async def scan_and_forward(self, payload_id, raw_payload):
        logging.info(f"🔍 Scanning Payload #{payload_id} for sensitive credentials...")
        await asyncio.sleep(0.6)
        
        cleaned = self.sanitize_payload(raw_payload)
        logging.info(f"🛡️ Cleaned Output #{payload_id}: {cleaned}")
        return cleaned

    async def run_day28_pipeline(self):
        print("\n=======================================================")
        print("🛡️ ZANKENE DAY 28: SECURITY GUARD & DATA SANITIZER 🛡️")
        print("=======================================================\n")
        
        test_payloads = [
            (101, "Connecting to OpenAI using sk-proj1234567890abcdefghij123456"),
            (102, "User auth payload with password=SecretPassword123"),
            (103, "Dispatching notification to lead contact user@example.com")
        ]

        tasks = [self.scan_and_forward(pid, raw) for pid, raw in test_payloads]
        await asyncio.gather(*tasks)

        print("\n🎉 Day 28 Security Guard & Data Sanitizer Setup Complete!")

if __name__ == "__main__":
    sanitizer = Day28SecuritySanitizer()
    asyncio.run(sanitizer.run_day28_pipeline())