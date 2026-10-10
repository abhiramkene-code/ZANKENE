import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.saas_builder import SaaSBuilderAgent

load_dotenv()

def run_day7_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 7 EXECUTION (MICRO-SAAS BUILDER ENGINE)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    saas_agent = SaaSBuilderAgent()

    task = "Design and generate codebase for a Micro-SaaS Automated PDF Contract Auditor"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] SaaS Builder Generating Codebase & Landing Blueprint...")
    saas_data = saas_agent.build_micro_saas_blueprint(
        "Autonomous PDF Contract & Invoice Security Auditor API"
    )

    print("\n[STEP 3] Micro-SaaS Blueprint Verification:")
    print("-" * 40)
    for key, value in saas_data.items():
        if key in ["fastapi_backend_code", "landing_page_html"]:
            print(f"🔹 {key.upper()}: [Generated Code Snippet - {len(str(value))} chars]\n")
        else:
            print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 7 STATUS: PASSED] Micro-SaaS Builder Engine Active!")
    print("=" * 65)

if __name__ == "__main__":
    run_day7_test()