import sys
import os

# Add root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from zankene.llm import ZankeneLLMEngine
from zankene.pipeline import ZankeneAgentPipeline as ZankeneMultiAgentPipeline

st.set_page_config(page_title="ZANKENE Mobile Engine", page_icon="⚡", layout="wide")

st.title("⚡ ZANKENE Mobile Controller")
st.caption("Autonomous AI Ecosystem & Multi-Agent Execution Panel")

st.sidebar.header("⚙️ Agent Engine Mode")
mode = st.sidebar.radio("Select Mode", ["Single Assistant", "Multi-Agent Pipeline"])

if mode == "Single Assistant":
    st.subheader("💬 Direct LLM Interface")
    user_input = st.text_area("Enter your prompt / task:", height=120)
    
    if st.button("🚀 Run Assistant", type="primary"):
        if user_input.strip():
            with st.spinner("ZANKENE Engine Processing..."):
                engine = ZankeneLLMEngine()
                response = engine.generate_agent_response(
                    system_prompt="You are ZANKENE Assistant. Provide clear and precise response.",
                    user_prompt=user_input
                )
                st.success("Response Received:")
                st.write(response)
        else:
            st.warning("Please enter a valid task!")

elif mode == "Multi-Agent Pipeline":
    st.subheader("🤖 Multi-Agent Autonomous Execution")
    st.info("Pipeline Workflow: Researcher Agent ➔ Coder Agent ➔ Executor Agent")
    
    agent_task = st.text_area("Enter complex autonomous task:", height=120, placeholder="e.g. Generate a python script to calculate fibonacci series and save output to a file.")
    
    if st.button("⚡ Execute Multi-Agent Workflow", type="primary"):
        if agent_task.strip():
            pipeline = ZankeneMultiAgentPipeline()
            
            with st.status("🤖 Executing Multi-Agent Pipeline...", expanded=True) as status:
                st.write("🔍 **Step 1: Researcher Agent** analyzing requirements...")
                res = pipeline.researcher_agent(agent_task)
                st.text_area("Researcher Output:", res, height=100)
                
                st.write("💻 **Step 2: Coder Agent** generating executable python script...")
                code = pipeline.coder_agent(res)
                st.code(code, language="python")
                
                st.write("⚡ **Step 3: Executor Agent** running code on host machine...")
                exec_result = pipeline.executor_agent(code)
                
                status.update(label="✅ Pipeline Execution Completed!", state="complete")
            
            st.subheader("🎯 Final Execution Result")
            st.code(exec_result)
        else:
            st.warning("Please enter a task for the Multi-Agent Pipeline!")