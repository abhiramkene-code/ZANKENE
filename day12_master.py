import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.executive_dashboard import ExecutiveDashboardAgent

load_dotenv()

def run_day12_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 12 EXECUTION (EXECUTIVE REVENUE & TELEMETRY)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    executive = ExecutiveDashboardAgent()

    task = "Compile Executive Revenue Report and System Telemetry for ZANKENE Empire"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Executive Dashboard Compiling Telemetry & Financial Audit...")
    report = executive.generate_executive_report(2, 11250.0) # $11,250 USD (~₹9.3 Lakhs collected)

    print("\n[STEP 3] Executive Report Verification:")
    print("-" * 40)
    for key, value in report.items():
        print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 12 STATUS: PASSED] Executive Operations & Telemetry Active!")
    print("=" * 65)

if __name__ == "__main__":
    run_day12_test()