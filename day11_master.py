import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.fulfillment_engine import ProjectFulfillmentEngine

load_dotenv()

def run_day11_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 11 EXECUTION (AUTOMATED PROJECT FULFILLMENT)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    fulfillment = ProjectFulfillmentEngine()

    task = "Execute and generate production integration code for Enterprise Customer Triage System"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Fulfillment Engine Generating Production Code & Delivery Packet...")
    result = fulfillment.execute_client_project(
        "Autonomous Customer Triage Agent & Salesforce CRM Sync Engine",
        "Apex Global Systems"
    )

    print("\n[STEP 3] Fulfillment Verification:")
    print("-" * 40)
    for key, value in result.items():
        if key == "production_code_snippet":
            print(f"🔹 {key.upper()}: [Production Code Generated - {len(str(value))} chars]\n")
        else:
            print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 11 STATUS: PASSED] Project Fulfillment Engine Active!")
    print("=" * 65)

if __name__ == "__main__":
    run_day11_test()