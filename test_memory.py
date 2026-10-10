import logging
from zankene import ZankeneMemoryVault, ZankeneLLMEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_memory():
    print("\n=================================================================")
    print("🧠 ZANKENE V10 MEMORY VAULT PERSISTENCE TEST 🧠")
    print("=================================================================\n")

    vault = ZankeneMemoryVault()
    llm = ZankeneLLMEngine(model_name="llama3")

    # 1. Save initial lead context into Memory Vault
    vault.save_agent_memory("lead_hunter_assistant", "last_target_industry", "FinTech SaaS")

    # 2. Retrieve memory
    saved_industry = vault.get_agent_memory("lead_hunter_assistant", "last_target_industry")
    print(f"📋 Retrived Memory from Vault: {saved_industry}")

    # 3. Use memory context in Agent LLM Prompt
    prompt = f"Using our remembered target industry '{saved_industry}', suggest 1 quick outreach angle."
    response = llm.generate_agent_response("You are LeadHunter Assistant with persistent memory.", prompt)

    print("\n🤖 [AGENT RESPONSE WITH MEMORY CONTEXT]:")
    print(response)
    print("\n=================================================================")

if __name__ == "__main__":
    test_memory()