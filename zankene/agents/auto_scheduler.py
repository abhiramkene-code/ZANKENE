import os
import json
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from agents.email_sender import EmailSenderAgent

DATABASE_FILE = os.path.join(BASE_DIR, "global_campaign_db.json")

def process_automated_followups():
    if not os.path.exists(DATABASE_FILE):
        print("No campaign database found.")
        return

    with open(DATABASE_FILE, "r") as f:
        db = json.load(f)

    today_str = datetime.now().strftime("%Y-%m-%d")
    email_sender = EmailSenderAgent()
    updated = False

    print(f"\n🔄 Running Automated Follow-up Check for: {today_str}")

    for campaign in db.get("campaigns", []):
        status = campaign.get("outreach_status")
        followup_date = campaign.get("next_followup_date")
        target_email = campaign.get("target_email")
        sequence = campaign.get("outreach_sequence", {})

        # Trigger Step 2 Follow-up if scheduled date is due
        if status == "Step 1 Sent" and followup_date <= today_str:
            step2 = sequence.get("sequence_step_2_day_3", {})
            subject = step2.get("subject", "Following up on my previous note")
            body = step2.get("body", "")

            if body:
                print(f"📧 Dispatching Step 2 Follow-up Email to {target_email}...")
                sent = email_sender.send_email(target_email, subject, body)
                if sent:
                    campaign["outreach_status"] = "Step 2 Sent"
                    updated = True

    if updated:
        with open(DATABASE_FILE, "w") as f:
            json.dump(db, f, indent=4)
        print("✅ Database updated with new follow-up statuses.")
    else:
        print("ℹ️ No pending follow-ups due today.")

if __name__ == "__main__":
    process_automated_followups()