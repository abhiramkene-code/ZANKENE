import asyncio
import json
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 23 MEMORY VAULT] - %(levelname)s - %(message)s'
)

class Day23MemoryVault:
    def __init__(self, storage_file="agent_memory_vault.json"):
        self.storage_file = Path(storage_file)
        self.memory = self._load_memory()
        logging.info("ZANKENE Day 23 Context Memory Vault Active.")

    def _load_memory(self):
        if self.storage_file.exists():
            with open(self.storage_file, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_context(self, session_id, key, value):
        if session_id not in self.memory:
            self.memory[session_id] = {}
        self.memory[session_id][key] = value
        with open(self.storage_file, "w") as f:
            json.dump(self.memory, f, indent=4)
        logging.info(f"💾 Saved Memory State [{session_id}] -> {key}: {value}")

    def get_context(self, session_id, key):
        val = self.memory.get(session_id, {}).get(key, None)
        logging.info(f"🧠 Retrieved Memory State [{session_id}] -> {key}: {val}")
        return val

    async def run_day23_pipeline(self):
        print("\n=======================================================")
        print("🧠 ZANKENE DAY 23: CONTEXT MEMORY & SESSION VAULT 🧠")
        print("=======================================================\n")
        
        session_id = "session_lead_001"
        
        # Step 1: Agent A stores discovered lead context
        self.save_context(session_id, "lead_name", "Acme Tech Solutions")
        self.save_context(session_id, "budget", "$10,000")
        await asyncio.sleep(0.5)

        # Step 2: Agent B retrieves lead context to draft proposal
        retrieved_lead = self.get_context(session_id, "lead_name")
        retrieved_budget = self.get_context(session_id, "budget")
        
        logging.info(f"📄 Proposal Agent generating pitch for {retrieved_lead} with budget {retrieved_budget}...")
        await asyncio.sleep(0.5)

        print("\n🎉 Day 23 Context Memory & Persistence Vault Setup Complete!")

if __name__ == "__main__":
    vault = Day23MemoryVault()
    asyncio.run(vault.run_day23_pipeline())
    