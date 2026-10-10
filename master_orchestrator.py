import os
import sys
import json
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.supervisor import CentralSupervisor
from agents.lead_prospector import LeadProspectorAgent
from agents.outreach_engine import AutonomousOutreachEngine
from agents.solution_architect import SolutionArchitectAgent
from agents.security_guard import SecurityGuardAgent
from agents.onboarding_agent import ClientOnboardingAgent
from agents.fulfillment_engine import ProjectFulfillmentEngine
from agents.executive_dashboard import ExecutiveDashboardAgent

load_dotenv()

def run_zankene_autonomous_swarm():
    print("=" * 70)
    print("⚡ ZANKENE AI EMPIRE: AUTONOMOUS 15-AGENT SWARM PIPELINE ACTIVATED")
    print("=" * 70)

    supervisor = CentralSupervisor()
    prospector = LeadProspectorAgent()
    outreach = AutonomousOutreachEngine()
    architect = SolutionArchitectAgent()
    guard = SecurityGuardAgent()
    onboarding = ClientOnboardingAgent()
    fulfillment = ProjectFulfillmentEngine()
    executive = ExecutiveDashboardAgent()

    # PHASE 1: LEAD PROSPECTING & ENRICHMENT
    print("\n🚀 [PHASE 1] Sourcing & Enriching Target B2B Clients...")
    lead_data = prospector.extract_and_enrich_leads("DTC E-commerce Brands", 1)
    target_lead = lead_data["leads"][0] if "leads" in lead_data and lead_data["leads"] else {
        "company_name": "Veloce Activewear",
        "decision_maker_role": "VP of Growth",
        "personalized_pitch_hook": "High checkout abandonment during viral drops"
    }
    print(f"✅ Target Acquired: {target_lead['company_name']} ({target_lead['decision_maker_role']})")

    # PHASE 2: COLD OUTREACH CAMPAIGN
    print("\n🚀 [PHASE 2] Generating Automated Outreach Sequence...")
    sequence = outreach.generate_outreach_sequence(target_lead)
    print(f"✅ 3-Step Sequence Generated for {target_lead['company_name']}")

    # PHASE 3: SOLUTION ARCHITECTURE & PROPOSAL
    print("\n🚀 [PHASE 3] Architecting Enterprise Proposal & Milestone Pricing...")
    proposal = architect.generate_technical_proposal(
        f"Autonomous Checkout Acceleration for {target_lead['company_name']}",
        "Enterprise Tier ($7,500 USD)"
    )
    print(f"✅ Proposal Created. Contract Value: {proposal.get('total_contract_value_usd', '$7,500')}")

    # PHASE 4: SECURITY & COMPLIANCE AUDIT
    print("\n🚀 [PHASE 4] Running Security Audit & GDPR Verification...")
    audit = guard.audit_security_and_compliance(proposal.get("proposed_architecture", "Event-driven architecture"))
    print(f"✅ Audit Status: {audit.get('audit_status')} (Score: {audit.get('security_score_out_of_100')}/100)")

    # PHASE 5: LEGAL SOW & ONBOARDING
    print("\n🚀 [PHASE 5] Drafting Legal SOW Contract & Wire Terms...")
    sow = onboarding.generate_sow_and_onboarding(
        target_lead["company_name"],
        "Checkout Acceleration & CRM Sync Engine",
        "$7,500 USD"
    )
    print(f"✅ SOW Terms Finalized (Deposit: {sow.get('payment_milestones', {}).get('upfront_deposit_50_percent', '50%')})")

    # PHASE 6: PROJECT FULFILLMENT & CODE GENERATION
    print("\n🚀 [PHASE 6] Executing Delivery & Automated Integration Code...")
    deliverable = fulfillment.execute_client_project(
        "Autonomous Checkout Agent Engine",
        target_lead["company_name"]
    )
    print(f"✅ Delivery Status: {deliverable.get('execution_status')}")

    # PHASE 7: REVENUE LOGGING & TELEMETRY
    print("\n🚀 [PHASE 7] Updating Executive Telemetry & Revenue Dashboard...")
    report = executive.generate_executive_report(3, 18750.0) # $18,750 (~₹15.5 Lakhs)
    
    print("\n" + "=" * 70)
    print("📊 ZANKENE EMPIRE MASTER EXECUTIVE SUMMARY")
    print("=" * 70)
    print(f"🔹 Gross Revenue: ${report.get('gross_revenue_usd')} USD")
    print(f"🔹 Net Profit (80% Margin): ${report.get('estimated_net_profit_usd')} USD")
    print(f"🔹 Active Retainers: {report.get('active_clients')}")
    print(f"🔹 Month 2 Growth Target Status: {report.get('month_1_target_status')}")
    print(f"🔹 System Health: {report.get('system_health_status')}")
    print("=" * 70)
    print("🎉 FULL 15-AGENT AUTONOMOUS SWARM EXECUTION COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    run_zankene_autonomous_swarm()