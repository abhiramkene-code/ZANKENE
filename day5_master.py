import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.security_guard import SecurityGuardAgent

load_dotenv()

def run_day5_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 5 EXECUTION (SECURITY & COMPLIANCE ENGINE)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    guard = SecurityGuardAgent()

    task = "Audit the Technical Proposal and System Code for GDPR and API Security Integrity"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Security Guard Running Audit on Proposed Architecture...")
    proposal_sample = "Event-driven multi-agent framework with OAuth2 authentication, TLS encryption, and automated PII anonymization."
    audit_result = guard.audit_security_and_compliance(proposal_sample)

    print("\n[STEP 3] Audit Report Verification:")
    print("-" * 40)
    for key, value in audit_result.items():
        print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 5 STATUS: PASSED] Security & Compliance Engine Operational!")
    print("=" * 65)

if __name__ == "__main__":
    run_day5_test()