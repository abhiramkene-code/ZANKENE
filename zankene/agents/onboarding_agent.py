import os
import json
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

load_dotenv()

class ClientOnboardingAgent:
    def get_llm(self):
        # Local Ollama model - No API keys, No Rate Limits, 100% Free & Offline
        return ChatOllama(model="gemma2", temperature=0.1)

    def generate_sow_and_onboarding(self, company_name: str, service_scope: str, contract_value: str) -> dict:
        print(f"📄 [ONBOARDING AGENT - LOCAL] Generating SOW & Deposit Terms for '{company_name}' ({contract_value})...")
        
        prompt = f"""
        You are Agent 13 & 14 (Legal SOW, Client Onboarding & Payment Rail Setup) of ZANKENE AI.
        Company Name: {company_name}
        Service Scope: {service_scope}
        Contract Value: {contract_value}
        
        Generate a professional Statement of Work (SOW), onboarding milestone checklist, and Wise/SWIFT direct wire deposit instructions (50% upfront deposit).
        
        Return pure JSON without markdown or backticks in this exact format:
        {{
            "client_company": "{company_name}",
            "statement_of_work_summary": "Professional SOW summary text",
            "contract_value": "{contract_value}",
            "upfront_deposit_required": "50% of total contract value",
            "payment_rail": "Wise / SWIFT Direct Wire (FEMA P0802 Compliant)",
            "onboarding_checklist": ["Milestone 1", "Milestone 2", "Milestone 3"]
        }}
        """
        
        try:
            response = self.get_llm().invoke([HumanMessage(content=prompt)])
            
            if isinstance(response.content, list):
                raw_text = "".join([item.get("text", "") if isinstance(item, dict) else str(item) for item in response.content])
            else:
                raw_text = str(response.content)
                
            clean_json = raw_text.replace("```json", "").replace("```", "").strip()
            
            # Find JSON boundaries if extra text is present
            start_idx = clean_json.find("{")
            end_idx = clean_json.rfind("}")
            if start_idx != -1 and end_idx != -1:
                clean_json = clean_json[start_idx:end_idx+1]

            return json.loads(clean_json)
            
        except Exception as e:
            print(f"⚠️ SOW Generation Error: {e}")
            return {
                "client_company": company_name,
                "statement_of_work_summary": f"Custom autonomous agent deployment and workflow orchestration for {company_name}.",
                "contract_value": contract_value,
                "upfront_deposit_required": "50% upfront wire transfer",
                "payment_rail": "Wise / SWIFT Direct Wire (FEMA P0802 Compliant)",
                "onboarding_checklist": ["Kickoff & Environment Setup", "Agent Integration", "Final Deployment & Training"]
            }

if __name__ == "__main__":
    onboarding = ClientOnboardingAgent()
    result = onboarding.generate_sow_and_onboarding("Lumina Health US", "Autonomous Workflow Engine", "$6,500 USD")
    print(json.dumps(result, indent=2))