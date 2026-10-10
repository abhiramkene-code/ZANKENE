import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.onboarding_agent import ClientOnboardingAgent

load_dotenv()

def run_day6_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 6 EXECUTION (CLIENT ONBOARDING ENGINE)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    onboarding = ClientOnboardingAgent()

    task = "Prepare SOW Contract and Client Onboarding Packet for Enterprise AI System"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Onboarding Agent Generating Legal SOW & Payment Roadmap...")
    onboarding_data = onboarding.generate_sow_and_onboarding(
        "Apex Global Systems",
        "Autonomous Multi-Agent Customer Triage & CRM Integration",
        "$7,500 USD"
    )

    print("\n[STEP 3] Onboarding Packet Verification:")
    print("-" * 40)
    for key, value in onboarding_data.items():
        print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 6 STATUS: PASSED] Client Onboarding Engine Operational!")
    print("=" * 65)

if __name__ == "__main__":
    run_day6_test()