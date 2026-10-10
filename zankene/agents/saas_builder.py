import os
import json
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class SaaSBuilderAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

    def build_micro_saas_blueprint(self, saas_idea: str) -> dict:
        print(f"🛠️ [SAAS BUILDER] Architecting Micro-SaaS Product for: '{saas_idea}'...")
        
        prompt = f"""
        You are Agent 7 (Autonomous Micro-SaaS Builder) of ZANKENE AI.
        SaaS Concept: {saas_idea}
        
        Generate a complete technical specification, FastAPI backend skeleton, and monetization strategy for this Micro-SaaS.
        
        Return pure JSON without markdown or backticks in this exact format:
        {{
            "product_name": "Name of the Micro-SaaS",
            "tagline": "High converting tagline",
            "monetization_tier": "$29/month Pro Plan, $99/month Agency Plan",
            "fastapi_backend_code": "from fastapi import FastAPI...",
            "landing_page_html": "<html><body>...</body></html>",
            "key_features": ["Feature 1", "Feature 2", "Feature 3"]
        }}
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        if isinstance(response.content, list):
            raw_text = "".join([item.get("text", "") if isinstance(item, dict) else str(item) for item in response.content])
        else:
            raw_text = str(response.content)
            
        clean_json = raw_text.replace("```json", "").replace("```", "").strip()
        
        try:
            return json.loads(clean_json)
        except Exception:
            return {"parsed_saas": clean_json}

if __name__ == "__main__":
    builder = SaaSBuilderAgent()
    result = builder.build_micro_saas_blueprint("AI Lead Magnet Generator for LinkedIn Creators")
    print(json.dumps(result, indent=2))