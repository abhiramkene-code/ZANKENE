import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class AutonomousDeveloper:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

    def write_and_execute_code(self, task_description: str, file_name: str):
        print(f"💻 [DEVELOPER] Writing code for: '{task_description}'")
        
        prompt = f"""
        You are Agent 2 (Autonomous Developer) of ZANKENE.
        Write a complete, functional Python script for the following task:
        '{task_description}'
        
        Return ONLY valid Python code without any markdown formatting or code blocks.
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        content = response.content
        if isinstance(content, list):
            content = " ".join([str(item) for item in content])
            
        clean_code = str(content).replace("```python", "").replace("```", "").strip()
        
        output_path = os.path.join("agents", file_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(clean_code)
            
        print(f"✅ [DEVELOPER] Code written successfully to '{output_path}'")

if __name__ == "__main__":
    dev = AutonomousDeveloper()
    print("Developer Engine Operational.")