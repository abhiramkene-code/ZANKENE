import requests
import json
import logging

class ZankeneLLMEngine:
    def __init__(self, model_name: str = "llama3", base_url: str = "http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        logging.info(f"🧠 [ZANKENE LLM] Engine Initialized with Model: '{self.model_name}'")

    def list_local_models(self) -> list:
        """Fetch available models from local Ollama instance."""
        try:
            res = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if res.status_code == 200:
                models = res.json().get("models", [])
                return [m["name"].split(":")[0] for m in models]
        except Exception:
            pass
        return [self.model_name]

    def generate_agent_response(self, system_prompt: str, user_prompt: str, override_model: str = None) -> str:
        """Sends structured system and user prompts to Ollama endpoint."""
        target_model = override_model if override_model else self.model_name
        endpoint = f"{self.base_url}/api/generate"
        full_prompt = f"System: {system_prompt}\nUser: {user_prompt}"
        
        payload = {
            "model": target_model,
            "prompt": full_prompt,
            "stream": False
        }
        
        try:
            res = requests.post(endpoint, json=payload, timeout=90)
            if res.status_code == 200:
                response_data = res.json()
                logging.info(f"✅ [OLLAMA RESPONSE GENERATED - Model: {target_model}]")
                return response_data.get("response", "No output generated.")
            else:
                return f"Error from Ollama ({res.status_code}): {res.text}"
        except Exception as e:
            logging.error(f"❌ [OLLAMA ERROR]: {e}")
            return f"Failed to reach local Ollama LLM on model '{target_model}': {e}"