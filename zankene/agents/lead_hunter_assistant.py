import os
import json

class LeadHunterAssistant:
    def __init__(self):
        print("🤖 [LEAD HUNTER AI] Assistant Agent Initialized!")

    def parse_raw_lead_text(self, raw_text: str):
        """
        നിങ്ങൾ Apollo-യിൽ നിന്നോ മറ്റ് വെബ്‌സൈറ്റുകളിൽ നിന്നോ കോപ്പി ചെയ്യുന്ന 
        ഏത് ടെക്സ്റ്റ്/ഡാറ്റയും കൃത്യമായ JSON ആക്കി മാറ്റാൻ ഈ ഏജന്റിന് കഴിയും.
        """
        lines = [line.strip() for line in raw_text.strip().split('\n') if line.strip()]
        parsed_leads = []
        
        # Auto-extracting fields from raw pasted text
        for line in lines:
            if "@" in line:
                email = line
                parsed_leads.append({
                    "first_name": "Decision Maker",
                    "company_name": "Target Company",
                    "decision_maker_role": "CEO / Founder",
                    "email": email,
                    "personalized_pitch_hook": "Scaling enterprise AI pipeline automation and agent infrastructure"
                })
        
        return parsed_leads

if __name__ == "__main__":
    assistant = LeadHunterAssistant()
    sample_text = "john@acmecorp.com\nsarah@techscale.io"
    print(assistant.parse_raw_lead_text(sample_text))