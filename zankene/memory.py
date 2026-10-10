import json
import os
import logging
from typing import Dict, Any

class ZankeneMemoryVault:
    def __init__(self, vault_path: str = "agent_memory_vault.json"):
        self.vault_path = vault_path
        self._init_vault()

    def _init_vault(self):
        if not os.path.exists(self.vault_path):
            with open(self.vault_path, "w", encoding="utf-8") as f:
                json.dump({"agent_memories": {}, "global_context": {}}, f, indent=4)
            logging.info(f"🧠 [MEMORY VAULT] Initialized new memory vault at '{self.vault_path}'.")

    def _read_vault(self) -> Dict[str, Any]:
        try:
            with open(self.vault_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
                if "agent_memories" not in data or not isinstance(data["agent_memories"], dict):
                    data["agent_memories"] = {}
                if "global_context" not in data or not isinstance(data["global_context"], dict):
                    data["global_context"] = {}
                return data
        except Exception as e:
            logging.error(f"❌ [MEMORY VAULT] Error reading vault: {e}")
            return {"agent_memories": {}, "global_context": {}}

    def save_agent_memory(self, agent_name: str, key: str, value: Any):
        data = self._read_vault()
        if agent_name not in data["agent_memories"]:
            data["agent_memories"][agent_name] = {}
        
        data["agent_memories"][agent_name][key] = value

        with open(self.vault_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info(f"💾 [MEMORY SAVED] Updated memory for '{agent_name}' -> Key: '{key}'")

    def get_agent_memory(self, agent_name: str, key: str = None) -> Any:
        data = self._read_vault()
        agent_data = data["agent_memories"].get(agent_name, {})
        if key:
            return agent_data.get(key, None)
        return agent_data