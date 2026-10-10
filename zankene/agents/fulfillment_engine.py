import os
import json
from dotenv import load_dotenv
from agents.key_rotator import get_rotated_key
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class ProjectFulfillmentEngine:
    def get_llm(self):
        return ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=get_rotated_key()
        )

    def execute_client_project(self, project_scope: str, client_name: str) -> dict:
        print(f"⚙️ [FULFILLMENT ENGINE] Building & Executing Deliverables for '{client_name}'...")

        prompt = f"""
        You are Agent 13 & 14 (Automated Project Execution & Delivery Engine) of ZANKENE AI.
        Client: {client_name}
        Scope: {project_scope}

        Generate the production integration code snippet, automated test cases, and delivery verification summary for this client project.

        Return pure JSON without markdown or backticks in this exact format:
        {{
            "client_name": "{client_name}",
            "execution_status": "COMPLETED",
            "production_code_snippet": "python / integration code block",
            "automated_test_cases": ["Test 1: Webhook Payload Validation", "Test 2: CRM Rate Limit Retry"],
            "delivery_summary": "Summary of features deployed for the client"
        }}
        """
        response = self.get_llm().invoke([HumanMessage(content=prompt)])

        if isinstance(response.content, list):
            raw_text = "".join([item.get("text", "") if isinstance(item, dict) else str(item) for item in response.content])
        else:
            raw_text = str(response.content)

        clean_json = raw_text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(clean_json)
        except Exception:
            return {"parsed_fulfillment": clean_json}

if __name__ == "__main__":
    engine = ProjectFulfillmentEngine()
    result = engine.execute_client_project("Shopify-Klaviyo Dynamic Cart Recovery Webhook Engine", "Veloce Activewear")
    print(json.dumps(result, indent=2))