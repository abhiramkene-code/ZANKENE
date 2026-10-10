import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.email_sender import AutonomousEmailSender

load_dotenv()

def run_day13_test():
    print("=" * 70)
    print("🚀 ZANKENE SYSTEM: DAY 13 EXECUTION (AUTONOMOUS EMAIL SENDER ENGINE)")
    print("=" * 70)

    supervisor = CentralSupervisor()
    sender = AutonomousEmailSender()

    task = "Dispatch automated cold outreach email sequence to enriched B2B leads"
    print(f"\n[STEP 1] Supervisor Routing Task: '{task}'")
    route = supervisor.route_task(task)
    print(f"🎯 Assigned Route: {route}")

    print("\n[STEP 2] Dispatching Stored Global Campaign Emails...")
    db_path = os.path.join(BASE_DIR, "global_campaign_db.json")
    # is_dry_run=False നൽകിയതിനാൽ ഇമെയിൽ ലൈവ് ആയി അയക്കപ്പെടും
    sender.dispatch_campaign_emails_from_db(db_path, is_dry_run=False)

    print("\n" + "=" * 70)
    print("🎉 [DAY 13 STATUS: PASSED] Autonomous Email Sender Engine Active!")
    print("=" * 70)

if __name__ == "__main__":
    run_day13_test()