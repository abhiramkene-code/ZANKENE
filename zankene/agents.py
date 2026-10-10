import os
import subprocess
from zankene.llm import ZankeneLLMEngine

class ZankeneMultiAgentPipeline:
    def __init__(self):
        self.engine = ZankeneLLMEngine()

    def researcher_agent(self, task):
        prompt = f"Act as Researcher Agent. Gather core technical requirements and strategy for: {task}"
        return self.engine.generate_agent_response("You are an expert AI Researcher.", prompt)

    def coder_agent(self, research_data):
        prompt = f"Act as Coder Agent. Write executable Python code based on this research:\n{research_data}\nReturn ONLY executable python code blocks."
        return self.engine.generate_agent_response("You are a Senior Python Engineer.", prompt)

    def executor_agent(self, code_snippet):
        code = code_snippet.replace("```python", "").replace("```", "").strip()
        file_path = os.path.join("zankene", "temp_task.py")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

        try:
            result = subprocess.run(["python", file_path], capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return f"✅ Execution Success:\n{result.stdout}"
            else:
                return f"❌ Execution Error:\n{result.stderr}"
        except Exception as e:
            return f"⚠️ System Exception: {e}"

    def run_pipeline(self, user_prompt):
        research = self.researcher_agent(user_prompt)
        code = self.coder_agent(research)
        execution = self.executor_agent(code)
        
        return {
            "research": research,
            "code": code,
            "execution": execution
        }