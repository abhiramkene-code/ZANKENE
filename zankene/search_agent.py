import urllib.parse
import urllib.request
import json
import logging
from bs4 import BeautifulSoup
from zankene.llm import ZankeneLLMEngine

class ZankeneWebSearchAgent:
    def __init__(self, model_name: str = "llama3"):
        self.llm = ZankeneLLMEngine(model_name=model_name)

    def search_duckduckgo(self, query: str, max_results: int = 3) -> str:
        """Searches DuckDuckGo HTML and extracts top snippet text."""
        try:
            url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            req = urllib.request.Request(url, headers=headers)
            
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8')
                soup = BeautifulSoup(html, 'html.parser')
                snippets = []
                for a in soup.find_all('a', class_='result__snippet', limit=max_results):
                    snippets.append(a.get_text(strip=True))
                
                return "\n".join(snippets) if snippets else "No direct live search results found."
        except Exception as e:
            logging.error(f"❌ [WEB SEARCH] Search failed: {e}")
            return f"Search execution error: {e}"

    def run_live_search_task(self, query: str) -> str:
        """Searches live web and generates LLM summary based on real-time findings."""
        logging.info(f"🌐 [WEB SEARCH] Fetching live web results for: '{query}'")
        search_results = self.search_duckduckgo(query)
        
        prompt = f"Live Web Search Context:\n{search_results}\n\nTask:\nSummarize the key insights from the live web context for query: '{query}'."
        system_role = "You are WebSearchAgent, a real-time intelligence gathering specialist."
        
        return self.llm.generate_agent_response(system_role, prompt)