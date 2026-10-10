import logging
import time
from zankene.search_agent import ZankeneWebSearchAgent
from zankene.email_agent import ZankeneEmailAgent
from zankene.llm import ZankeneLLMEngine

class ZankeneMegaPipeline:
    def __init__(self, model_name: str = "llama3"):
        self.search_agent = ZankeneWebSearchAgent(model_name=model_name)
        self.email_agent = ZankeneEmailAgent()
        self.llm = ZankeneLLMEngine(model_name=model_name)

    def run_autonomous_campaign(self, topic: str, target_segment: str, sender_email: str = None, sender_password: str = None, recipient_email: str = None) -> dict:
        logging.info(f"🚀 [MEGA PIPELINE] Starting autonomous campaign for topic: '{topic}'")
        
        # Stage 1: Live Web Search Intelligence
        search_summary = self.search_agent.run_live_search_task(topic)
        
        # Stage 2: Lead Hunter Strategy
        strategy_prompt = f"Target Segment: {target_segment}\nMarket Insights:\n{search_summary}\n\nTask: Create 2 outreach positioning points."
        strategy = self.llm.generate_agent_response("You are LeadHunter, an expert lead strategist.", strategy_prompt)
        
        # Stage 3: Email Pitch Drafting
        pitch_prompt = f"Strategy:\n{strategy}\n\nTask: Write a short, highly persuasive 3-sentence B2B cold email pitch."
        pitch = self.llm.generate_agent_response("You are OutreachEngine, a master email copywriter.", pitch_prompt)
        
        # Stage 4: Email Dispatch (If credentials provided)
        mail_sent = False
        if sender_email and sender_password and recipient_email:
            mail_sent = self.email_agent.send_email(
                sender_email=sender_email,
                sender_password=sender_password,
                recipient_email=recipient_email,
                subject=f"AI Automation Insights for {target_segment}",
                body=pitch
            )
            
        return {
            "topic": topic,
            "search_summary": search_summary,
            "strategy": strategy,
            "pitch": pitch,
            "mail_sent": mail_sent
        }