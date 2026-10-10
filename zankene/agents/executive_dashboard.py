import os
import json
from dotenv import load_dotenv
from agents.key_rotator import get_rotated_key
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class ExecutiveDashboardAgent:
    def get_llm(self):
        return ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=get_rotated_key()
        )

    def generate_executive_report(self, Active_clients: int, gross_revenue_usd: float) -> dict:
        print("📊 [EXECUTIVE AGENT] Compiling System Telemetry & Empire Revenue Report...")

        prompt = f"""
        You are Agent 15 (Executive Operations & Revenue Dashboard Engine) of ZANKENE AI.
        Active Retainer Clients: {Active_clients}
        Gross Revenue Collected (USD): ${gross_revenue_usd}

        Calculate estimated net profit margins (targeting 75-85%), operational health status across all 15 agents, and strategic recommendations for scaling to ₹15 Lakhs+ ($18,000+) in Month 2.

        Return pure JSON without markdown or backticks in this exact format:
        {{
            "gross_revenue_usd": "{gross_revenue_usd}",
            "estimated_net_profit_usd": "Amount calculated based on 80% margin",
            "active_clients": {Active_clients},
            "system_health_status": "OPERATIONAL / 100% HEALTHY",
            "month_1_target_status": "ON_TRACK_OR_ACHIEVED",
            "executive_summary": "Brief founder summary on agent swarm performance",
            "scaling_action_items": ["Action 1 for Month 2", "Action 2 for Month 2"]
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
            return {"parsed_report": clean_json}

if __name__ == "__main__":
    dashboard = ExecutiveDashboardAgent()
    result = dashboard.generate_executive_report(2, 11250.0)
    print(json.dumps(result, indent=2))