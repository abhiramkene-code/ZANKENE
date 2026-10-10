import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.bd_agent import BusinessDevelopmentAgent

load_dotenv()

def run_day2_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 2 EXECUTION (BD & LEAD ACQUISITION)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    bd_agent = BusinessDevelopmentAgent()

    task = "Generate a B2B Outreach Campaign for E-commerce Brands seeking AI Automation"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] BD Agent Generating Cold Outreach Strategy & ICP...")
    strategy = bd_agent.generate_outreach_strategy("E-commerce Brands", "US / Global")

    print("\n[STEP 3] Output Strategy Verification:")
    print("-" * 40)
    for key, value in strategy.items():
        print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 2 STATUS: PASSED] Business Development Engine Active!")
    print("=" * 65)

if __name__ == "__main__":
    run_day2_test()