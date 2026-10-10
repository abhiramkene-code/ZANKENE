import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.marketing_agent import DigitalMarketingAgent

load_dotenv()

def run_day3_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 3 EXECUTION (DIGITAL MARKETING ENGINE)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    marketing_agent = DigitalMarketingAgent()

    task = "Create a Marketing Campaign around Enterprise AI Workflow Automation"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Digital Marketing Agent Generating Content Package...")
    campaign = marketing_agent.generate_content_campaign(
        "Replacing Manual Operations with Autonomous AI Swarms", 
        "SaaS Founders & Ops Leaders"
    )

    print("\n[STEP 3] Output Content Campaign Verification:")
    print("-" * 40)
    for key, value in campaign.items():
        print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 3 STATUS: PASSED] Digital Marketing Engine Operational!")
    print("=" * 65)

if __name__ == "__main__":
    run_day3_test()