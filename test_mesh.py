import logging
from zankene.llm import ZankeneLLMEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_multi_model():
    print("\n=================================================================")
    print("🧠 ZANKENE V10 MULTI-MODEL MESH ROUTER TEST 🧠")
    print("=================================================================\n")

    llm = ZankeneLLMEngine(model_name="llama3")
    
    # Available Models
    available = llm.list_local_models()
    print(f"📦 Local Ollama Available Models: {available}\n")

    # Dynamic Execution
    response = llm.generate_agent_response(
        system_prompt="You are a speed optimization expert.",
        user_prompt="Give 2 lines on why Multi-LLM routing improves system elasticity.",
        override_model="llama3"
    )

    print("🤖 [DYNAMIC MESH RESPONSE]:")
    print(response)
    print("\n=================================================================")

if __name__ == "__main__":
    test_multi_model()