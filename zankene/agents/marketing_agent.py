import os
import json
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class DigitalMarketingAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_content_campaign(self, topic: str, target_audience: str) -> dict:
        print(f"📣 [MARKETING AGENT] Crafting Viral B2B Campaign for: '{topic}' [{target_audience}]...")
        
        prompt = f"""
        You are Agent 3 (Digital Marketing Engine) of the ZANKENE AI Empire.
        Topic: {topic}
        Audience: {target_audience}
        
        Create a high-converting B2B content marketing package including a LinkedIn Thought Leadership Post and a Lead Magnet Hook.
        
        Return pure JSON without markdown or backticks in this exact format:
        {{
            "campaign_topic": "{topic}",
            "linkedin_post": "Hook + Body + Call-to-Action for LinkedIn Founders/CTOs",
            "lead_magnet_title": "Title of a free PDF/Audit to capture leads",
            "lead_magnet_outline": "3-4 bullet points describing what the audit contains"
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
            return {"parsed_campaign": clean_json}

if __name__ == "__main__":
    marketing = DigitalMarketingAgent()
    result = marketing.generate_content_campaign("How AI Agents Reduce Customer Support Costs by 70%", "DTC Founders")
    print(json.dumps(result, indent=2))