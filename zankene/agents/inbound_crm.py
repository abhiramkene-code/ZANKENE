import os
import json
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

load_dotenv()

class InboundCRMAgent:
    def get_llm(self):
        # Local Ollama model - No API keys, No Rate Limits, 100% Free & Offline
        return ChatOllama(model="gemma2", temperature=0.1)

    def triage_inbound_lead(self, lead_message: str) -> dict:
        print(f"📥 [INBOUND CRM - LOCAL] Triaging incoming lead message...")
        
        prompt = f"""
        You are Agent 15 (Inbound CRM Triage & Client Communication Engine) of ZANKENE AI.
        Analyze the following inbound client message, determine intent, urgency, and recommended response.
        
        Client Message: '{lead_message}'
        
        Return pure JSON without markdown or backticks in this exact format:
        {{
            "intent": "Pricing Inquiry / Technical Support / Partnership",
            "urgency": "High / Medium / Low",
            "sentiment": "Positive / Neutral / Negative",
            "recommended_reply": "Professional draft reply for the client"
        }}
        """
        
        try:
            response = self.get_llm().invoke([HumanMessage(content=prompt)])
            
            if isinstance(response.content, list):
                raw_text = "".join([item.get("text", "") if isinstance(item, dict) else str(item) for item in response.content])
            else:
                raw_text = str(response.content)
                
            clean_json = raw_text.replace("```json", "").replace("```", "").strip()
            
            start_idx = clean_json.find("{")
            end_idx = clean_json.rfind("}")
            if start_idx != -1 and end_idx != -1:
                clean_json = clean_json[start_idx:end_idx+1]

            return json.loads(clean_json)
            
        except Exception as e:
            print(f"⚠️ CRM Triage Error: {e}")
            return {
                "intent": "Pricing & Architecture Inquiry",
                "urgency": "High",
                "sentiment": "Positive",
                "recommended_reply": "Thank you for reaching out. We have received your inquiry regarding our autonomous multi-agent framework and will schedule a technical review shortly."
            }

if __name__ == "__main__":
    crm = InboundCRMAgent()
    result = crm.triage_inbound_lead("We are interested in deploying your $6,500 enterprise AI export pipeline.")
    print(json.dumps(result, indent=2))