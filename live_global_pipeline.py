import os
import sys
import json
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.lead_prospector import LeadProspectorAgent
from agents.outreach_engine import AutonomousOutreachEngine
from agents.solution_architect import SolutionArchitectAgent
from agents.security_guard import SecurityGuardAgent
from agents.onboarding_agent import ClientOnboardingAgent
from agents.email_sender import DirectEmailSenderAgent
from agents.auto_reply_agent import AutoReplyAgent

load_dotenv()

DATABASE_FILE = os.path.join(BASE_DIR, "global_campaign_db.json")

def load_database():
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {"campaigns": [], "total_projected_revenue_usd": 0}
    return {"campaigns": [], "total_projected_revenue_usd": 0}

def save_database(data):
    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def run_global_outreach_pipeline():
    print("=" * 75)
    print("🌍 ZANKENE GLOBAL B2B EXPORT PIPELINE: ULTRA-AUTONOMOUS SUPER ENGINE")
    print("=" * 75)

    prospector = LeadProspectorAgent()
    outreach = AutonomousOutreachEngine()
    architect = SolutionArchitectAgent()
    guard = SecurityGuardAgent()
    onboarding = ClientOnboardingAgent()
    email_sender = DirectEmailSenderAgent()
    auto_reply = AutoReplyAgent()

    db = load_database()
    global_niche = "US & UK High-Growth DTC E-commerce & B2B SaaS ($5M+ Revenue)"
    
    print(f"\n[STEP 1] Autonomous AI Prospecting Leads for: '{global_niche}'...")
    prospect_data = prospector.extract_and_enrich_leads(global_niche, count=2)
    leads = prospect_data.get("leads", [])

    for idx, lead in enumerate(leads, 1):
        company_name = lead.get("company_name", f"Global Client {idx}")
        role = lead.get("decision_maker_role", "Executive")
        target_email = lead.get("email", "abhiramkene@gmail.com")
        
        print(f"\n----------------------------------------------------------------------")
        print(f"🎯 [GLOBAL TARGET {idx}/{len(leads)}] Processing: {company_name} ({role})")
        print(f"----------------------------------------------------------------------")

        sequence = outreach.generate_outreach_sequence(lead)
        step1_email = sequence.get("step_1", {})
        email_subject = step1_email.get("subject", f"AI Automation Proposal for {company_name}")
        email_body = step1_email.get("body", "")

        print(f"🚀 [EMAIL DISPATCH] Dispatching Email to: {target_email}...")
        email_success = email_sender.send_email(target_email, email_subject, email_body)
        
        if email_success:
            print(f"✅ Email successfully dispatched to {target_email}")

        proposal = architect.generate_technical_proposal(
            f"Autonomous Agent Infrastructure for {company_name}",
            "Global Enterprise Tier ($6,500 USD)"
        )

        audit = guard.audit_security_and_compliance(proposal.get("proposed_architecture", "Multi-agent framework"))

        sow = onboarding.generate_sow_and_onboarding(
            company_name,
            "Autonomous AI Infrastructure & Workflow Engine",
            "$6,500 USD"
        )

        campaign_record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "company_name": company_name,
            "decision_maker_role": role,
            "target_email": target_email,
            "contract_value_usd": "$6,500",
            "outreach_status": "step_1_sent" if email_success else "step_1_pending"
        }

        db["campaigns"].append(campaign_record)
        db["total_projected_revenue_usd"] += 6500
        time.sleep(1)

    save_database(db)

    print("\n" + "=" * 75)
    print("🎉 ULTRA-AUTONOMOUS PIPELINE EXECUTION COMPLETE!")
    print("=" * 75)

if __name__ == "__main__":
    run_global_outreach_pipeline()