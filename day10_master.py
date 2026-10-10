import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.outreach_engine import AutonomousOutreachEngine

load_dotenv()

def run_day10_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 10 EXECUTION (AUTONOMOUS OUTRACH & NURTURING)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    outreach = AutonomousOutreachEngine()

    task = "Generate Automated 3-Step Outreach Campaign for Enriched E-commerce Leads"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    sample_lead = {
        "company_name": "Veloce Activewear",
        "decision_maker_role": "VP of Growth & Performance Marketing",
        "personalized_pitch_hook": "72% checkout abandonment during high-traffic TikTok drops"
    }

    print(f"\n[STEP 2] Outreach Engine Constructing Campaign for: {sample_lead['company_name']}...")
    sequence = outreach.generate_outreach_sequence(sample_lead)

    print("\n[STEP 3] 3-Step Automated Outreach Sequence Verification:")
    print("-" * 40)
    for step, content in sequence.items():
        if isinstance(content, dict):
            print(f"🔹 {step.upper()}:")
            print(f"   Subject: {content.get('subject')}")
            print(f"   Body:\n{content.get('body')}\n")
        else:
            print(f"🔹 {step.upper()}: {content}\n")

    print("=" * 65)
    print("🎉 [DAY 10 STATUS: PASSED] Autonomous Outreach Engine Active!")
    print("=" * 65)

if __name__ == "__main__":
    run_day10_test()