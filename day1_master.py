import os
import sys

# Get absolute path of current directory and add to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv

# Direct module imports
try:
    from agents.supervisor import CentralSupervisor
    from agents.developer import AutonomousDeveloper
    from agents.qa_guard import QAIntegrityGuard
except ImportError as e:
    print(f"❌ [IMPORT ERROR]: {e}")
    print("Ensure supervisor.py, developer.py, and qa_guard.py exist inside 'agents/' folder.")
    sys.exit(1)

load_dotenv()

def run_day1_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 1 EXECUTION & VERIFICATION")
    print("=" * 65)

    if not os.getenv("GEMINI_API_KEY"):
        print("❌ [CRITICAL ERROR] GEMINI_API_KEY missing in .env file!")
        return

    print("\n[STEP 1] Initializing Core Agents...")
    supervisor = CentralSupervisor()
    developer = AutonomousDeveloper()
    qa_guard = QAIntegrityGuard()
    print("✅ All 3 Core Agents Loaded Successfully.")

    task_description = "Create a python script that logs system health, active agents, and API execution latency."
    target_filename = "system_health_logger.py"

    print(f"\n[STEP 2] Central Supervisor Routing Task: '{task_description}'")
    assigned_agent = supervisor.route_task(task_description)
    print(f"🎯 Assigned to: {assigned_agent}")

    print(f"\n[STEP 3] Autonomous Developer writing code into 'agents/{target_filename}'...")
    developer.write_and_execute_code(task_description, target_filename)

    print(f"\n[STEP 4] QA Integrity Guard Auditing Generated Code...")
    file_path = os.path.join("agents", target_filename)
    is_safe = qa_guard.audit_code(file_path)

    print("\n" + "=" * 65)
    if is_safe:
        print("🎉 [DAY 1 STATUS: PASSED] Core Foundation is 100% Operational!")
        print("👉 We are ready to proceed to Day 2 (Lead Acquisition & BD Agent).")
    else:
        print("⚠️ [DAY 1 STATUS: FLAGGED] QA Guard detected an issue in execution.")
    print("=" * 65)

if __name__ == "__main__":
    run_day1_test()