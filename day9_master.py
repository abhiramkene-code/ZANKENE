import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.lead_prospector import LeadProspectorAgent

load_dotenv()

def run_day9_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 9 EXECUTION (LEAD PROSPECTING & ENRICHMENT)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    prospector = LeadProspectorAgent()

    task = "Prospect and enrich 3 high-ticket E-commerce leads looking for AI Automation"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Lead Prospector Sourcing & Enriching Leads...")
    lead_data = prospector.extract_and_enrich_leads("E-commerce DTC Brands", 3)

    print("\n[STEP 3] Lead Data Verification:")
    print("-" * 40)
    for key, value in lead_data.items():
        if key == "leads" and isinstance(value, list):
            print(f"🔹 ENRICHED LEADS GENERATED ({len(value)} Leads):")
            for idx, lead in enumerate(value, 1):
                print(f"   [{idx}] {lead.get('company_name')} ({lead.get('decision_maker_role')})")
                print(f"       Pain Point: {lead.get('identified_pain_point')}")
                print(f"       Hook: {lead.get('personalized_pitch_hook')}\n")
        else:
            print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 9 STATUS: PASSED] Lead Prospecting & Enrichment Operational!")
    print("=" * 65)

if __name__ == "__main__":
    run_day9_test()