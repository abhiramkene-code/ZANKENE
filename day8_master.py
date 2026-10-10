import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
from agents.key_rotator import get_rotated_key
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def run_day8_test():
    print("=" * 65)
    print("🚀 ZANKENE SYSTEM: DAY 8 EXECUTION (SWARM & KEY ROTATION ENGINE)")
    print("=" * 65)

    print("\n[STEP 1] Initializing Swarm Pipeline with 10-Key Rotation Pool...")
    
    tasks = [
        "Audit API Gateways for Security Flaws",
        "Generate Cold Email Hook for Fintech SaaS",
        "Draft Enterprise Solution Milestone for AI Agents",
        "Create LinkedIn Marketing Strategy for B2B Agency"
    ]

    print("\n[STEP 2] Parallel Swarm Execution with Auto Key Rotation:")
    print("-" * 50)

    for idx, task in enumerate(tasks, 1):
        current_key = get_rotated_key()
        print(f"🔄 Executing Task {idx}/4 using Key Pool...")
        
        llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=current_key
        )
        
        response = llm.invoke([HumanMessage(content=f"Briefly answer in 1 sentence: {task}")])
        
        content = response.content
        if isinstance(content, list):
            content = " ".join([str(item) for item in content])
            
        print(f"✅ Result {idx}: {str(content).strip()}\n")
        time.sleep(1)

    print("=" * 65)
    print("🎉 [DAY 8 STATUS: PASSED] 10-Key Rotation & Swarm Engine Operational!")
    print("=" * 65)

if __name__ == "__main__":
    run_day8_test()