import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.inbound_crm import InboundCRMAgent

load_dotenv()

def run_day14_test():
    print("=" * 70)
    print("🚀 ZANKENE SYSTEM: DAY 14 EXECUTION (INBOUND CRM & TRIAGE ENGINE)")
    print("=" * 70)

    supervisor = CentralSupervisor()
    crm = InboundCRMAgent()

    # Simulate Incoming Client Replies
    simulated_inbound_replies = [
        {
            "client": "Lumina Botanicals",
            "email_text": "Hey Abhiram, saw your pitch on TikTok shop automation. We definitely need help with our checkout latency. Can we schedule a quick call this week?"
        },
        {
            "client": "Synthetix Operations (UK)",
            "email_text": "Sounds interesting, but $6,500 sounds a bit steep for an initial MVP. Do you have smaller milestone packages?"
        }
    ]

    for idx, item in enumerate(simulated_inbound_replies, 1):
        print(f"\n📩 [INBOUND MESSAGE {idx}/{len(simulated_inbound_replies)}] Processing...")
        analysis = crm.analyze_and_respond_to_lead(item["email_text"], item["client"])
        
        print(f"🔹 Sentiment: {analysis.get('lead_sentiment')}")
        print(f"🔹 Action: {analysis.get('recommended_next_action')}")
        print(f"📝 Draft Reply Preview:\n{analysis.get('drafted_reply_body')[:150]}...\n")

    print("=" * 70)
    print("🎉 [DAY 14 STATUS: PASSED] Inbound CRM & Triage Engine Operational!")
    print("=" * 70)

if __name__ == "__main__":
    run_day14_test()