import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.solution_architect import SolutionArchitectAgent

load_dotenv()

def safe_api_call(func, *args, **kwargs):
    """Rate limit 429 വന്നാൽ തനിയെ കാത്തിരുന്ന് വീണ്ടും ട്രൈ ചെയ്യുന്ന ഹെൽപ്പർ"""
    max_retries = 5
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                wait_time = (attempt + 1) * 10
                print(f"⚠️ [RATE LIMIT DETECTED] Quota Cooldown... Waiting {wait_time}s (Attempt {attempt+1}/{max_retries})...")
                time.sleep(wait_time)
            else:
                raise e
    raise Exception("Max retries exceeded due to persistent rate limiting.")

def run_day4_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 4 EXECUTION (SOLUTION ARCHITECT & PROPOSAL ENGINE)")
    print("=" * 65)

    supervisor = CentralSupervisor()
    architect = SolutionArchitectAgent()

    task = "Design a Technical Proposal for Automating Customer Support with AI Agents"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = safe_api_call(supervisor.route_task, task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Solution Architect Drafting Proposal & Architecture Plan...")
    proposal = safe_api_call(
        architect.generate_technical_proposal,
        "Autonomous Multi-Agent Customer Triage & CRM Sync System", 
        "Tier 1 Enterprise ($7,500)"
    )

    print("\n[STEP 3] Proposal Verification:")
    print("-" * 40)
    for key, value in proposal.items():
        print(f"🔹 {key.upper()}: {value}\n")

    print("=" * 65)
    print("🎉 [DAY 4 STATUS: PASSED] Solution Architect Engine Active!")
    print("=" * 65)

if __name__ == "__main__":
    run_day4_test()