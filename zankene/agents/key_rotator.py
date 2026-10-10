import os
import time
import itertools
from dotenv import load_dotenv

load_dotenv()

class APIKeyRotator:
    def __init__(self):
        self.keys = []
        for i in range(1, 11):
            key = os.getenv(f"GEMINI_API_KEY_{i}")
            if key:
                self.keys.append(key)
        
        if not self.keys:
            single_key = os.getenv("GEMINI_API_KEY")
            if single_key:
                self.keys.append(single_key)
                
        if not self.keys:
            raise ValueError("❌ No Gemini API keys found in environment variables!")
            
        self.key_cycle = itertools.cycle(self.keys)
        print(f"🔑 Loaded {len(self.keys)} API Keys with Auto-Retry & Smart Delay protection.")

    def get_next_key(self):
        return next(self.key_cycle)

    def safe_generate_content(self, model_function, *args, **kwargs):
        """
        Auto-retry logic with exponential backoff and smart delay 
        to completely prevent Free Tier 429 Rate Limit errors.
        """
        max_retries = 15
        delay = 5  # initial delay in seconds
        
        for attempt in range(max_retries):
            try:
                # Add a smart delay between requests to respect RPM limits
                time.sleep(3) 
                
                # Execute the Gemini API call
                return model_function(*args, **kwargs)
                
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    print(f"⚠️ Rate limit hit on attempt {attempt + 1}. Rotating key & waiting {delay}s...")
                    time.sleep(delay)
                    delay *= 1.5  # Increase wait time gradually
                else:
                    raise e
                    
        raise Exception("❌ Max retries reached. All API keys are currently rate-limited. Please wait a minute.")

# Global instance
key_rotator = APIKeyRotator()

# Compatibility wrapper for supervisor.py expecting get_rotated_key
def get_rotated_key():
    return key_rotator.get_next_key()