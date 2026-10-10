import os
import json
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class BusinessDevelopmentAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_outreach_strategy(self, niche: str, target_geography: str) -> dict:
        print(f"🎯 [BD AGENT] Prospecting Strategy for Niche: '{niche}' [{target_geography}]...")
        
        prompt = f"""
        You are Agent 8 (Business Development Engine) of the ZANKENE AI Empire.
        Target Niche: {niche}
        Geography: {target_geography}
        
        Generate a highly targeted cold outreach pitch and ideal customer profile (ICP).
        Comply with international B2B regulations. 
        
        Return pure JSON without markdown or backticks in this exact format:
        {{
            "target_industry": "{niche}",
            "ideal_client_profile": "Description of decision maker",
            "cold_email_subject": "High converting subject line",
            "cold_email_body": "Persuasive cold pitch focusing on ROI and AI automation",
            "suggested_pricing_usd": "$2,500 - $5,000/month"
        }}
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        # Handle dict/list response structure cleanly
        if isinstance(response.content, list):
            raw_text = "".join([item.get("text", "") if isinstance(item, dict) else str(item) for item in response.content])
        else:
            raw_text = str(response.content)
            
        clean_json = raw_text.replace("```json", "").replace("```", "").strip()
        
        try:
            return json.loads(clean_json)
        except Exception:
            return {"parsed_pitch": clean_json}

if __name__ == "__main__":
    bd = BusinessDevelopmentAgent()
    result = bd.generate_outreach_strategy("SaaS Companies", "US/UK")
    print(json.dumps(result, indent=2))