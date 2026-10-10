import os
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

class CentralSupervisor:
    def __init__(self):
        # Local Ollama model - No API keys, No Rate Limits, 100% Free & Offline
        self.llm = ChatOllama(model="gemma2", temperature=0.1)

    def route_task(self, task_description: str) -> str:
        prompt = f"""
        You are the Central Supervisor Orchestrator of the ZANKENE AI Empire.
        Analyze the following task requirement and assign it to the correct core execution agent.
        
        Task: '{task_description}'
        
        Available Primary Agents:
        - AUTONOMOUS_DEVELOPER (For code writing, software engineering, bug fixing)
        - BUSINESS_DEVELOPMENT (For client outreach, sales pitching, lead generation)
        - QA_GUARD (For integrity checks, code audits, quality control)
        - SOLUTION_ARCHITECT (For technical proposals, pricing, system blueprints)
        
        Return ONLY the name of the assigned agent in capital letters.
        """
        
        try:
            response = self.llm.invoke([HumanMessage(content=prompt)])
            content = response.content
            
            if isinstance(content, list):
                raw_text = "".join([item.get("text", "") if isinstance(item, dict) else str(item) for item in content])
            else:
                raw_text = str(content)
                
            return raw_text.strip()

        except Exception as e:
            print(f"⚠️ Ollama execution error: {e}")
            return "BUSINESS_DEVELOPMENT"  # Fallback default agent

if __name__ == "__main__":
    supervisor = CentralSupervisor()
    print("Supervisor Engine Operational with Local Ollama Model.")