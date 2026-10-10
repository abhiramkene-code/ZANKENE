import logging
from zankene import ZankeneLLMEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_ollama():
    print("\n=================================================================")
    print("🦙 ZANKENE V10 LOCAL OLLAMA LLM REASONING TEST 🦙")
    print("=================================================================\n")

    # നിങ്ങളുടെ Ollama-യിൽ ഉള്ള exact model name നൽകുക (e.g., 'llama3', 'mistral', 'qwen2')
    llm = ZankeneLLMEngine(model_name="llama3")

    agent_role = "You are LeadHunter_V10, an autonomous market research agent."
    task = "Give 3 key lead qualification steps for B2B Enterprise SaaS in 2 bullet points."

    response = llm.generate_agent_response(agent_role, task)
    
    print("\n📋 [OLLAMA AGENT OUTPUT]:")
    print(response)
    print("\n=================================================================")

if __name__ == "__main__":
    test_ollama()