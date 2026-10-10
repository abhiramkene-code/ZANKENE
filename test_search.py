import logging
from zankene import ZankeneWebSearchAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_search():
    print("\n=================================================================")
    print("🌐 ZANKENE V10 LIVE WEB SEARCH AGENT TEST 🌐")
    print("=================================================================\n")

    agent = ZankeneWebSearchAgent(model_name="llama3")
    query = "Latest AI trends 2026"
    
    result = agent.run_live_search_task(query)

    print("\n🤖 [LIVE SEARCH AGENT SUMMARY]:")
    print(result)
    print("\n=================================================================")

if __name__ == "__main__":
    test_search()