import logging
from zankene import ZankeneMegaPipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_mega_pipeline():
    print("\n=================================================================")
    print("🔥 ZANKENE V10 MEGA AUTONOMOUS PIPELINE TEST 🔥")
    print("=================================================================\n")

    pipeline = ZankeneMegaPipeline(model_name="llama3")
    
    result = pipeline.run_autonomous_campaign(
        topic="Latest B2B AI Automation trends 2026",
        target_segment="SaaS Enterprise Founders"
    )

    print("\n🌐 [STAGE 1: WEB INTELLIGENCE]:")
    print(result["search_summary"][:200] + "...")
    
    print("\n🎯 [STAGE 2: LEAD STRATEGY]:")
    print(result["strategy"])
    
    print("\n✉️ [STAGE 3: GENERATED EMAIL PITCH]:")
    print(result["pitch"])
    print("\n=================================================================")

if __name__ == "__main__":
    test_mega_pipeline()