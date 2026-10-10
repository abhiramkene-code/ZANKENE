import logging
from zankene import ZankeneAgentPipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_pipeline():
    print("\n=================================================================")
    print("🔗 ZANKENE V10 MULTI-AGENT PIPELINE CHAINING TEST 🔗")
    print("=================================================================\n")

    pipeline = ZankeneAgentPipeline(model_name="llama3")

    # Defining a 3-Stage Agent Chain
    chain = [
        {
            "agent_name": "lead_hunter_assistant",
            "role": "You are LeadHunter, an expert in lead generation.",
            "instruction": "Identify 2 high-potential target segments for AI Workflow Automation software."
        },
        {
            "agent_name": "outreach_engine",
            "role": "You are OutreachEngine, a master B2B email copywriter.",
            "instruction": "Write a short 3-sentence cold email pitch targeting the segments identified in the previous step."
        },
        {
            "agent_name": "qa_guard",
            "role": "You are QA_Guard, a strict quality auditor.",
            "instruction": "Review the email pitch above. Give a score out of 10 and suggest 1 improvement."
        }
    ]

    result = pipeline.run_chain(initial_input="Initiate Lead Chaining Campaign", agent_chain=chain)

    print("\n🏁 [FINAL PIPELINE AUDIT RESULT]:")
    print(result["final_output"])
    print("\n=================================================================")

if __name__ == "__main__":
    test_pipeline()