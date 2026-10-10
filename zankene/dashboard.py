import sys
import os

# Add root directory to sys.path so Python can find 'zankene'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import time
import requests
import pandas as pd
from zankene import load_all_agents, ZankeneWebSearchAgent, ZankeneEmailAgent, ZankeneMegaPipeline
from zankene.llm import ZankeneLLMEngine

st.set_page_config(page_title="ZANKENE V10 Mission Control", page_icon="👑", layout="wide")

# --- Password Protection Security Layer ---
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] == "abhiram"  # നിങ്ങളുടെ യൂസർനെയിം
            and st.session_state["password"] == "@#aknandu123abhikene123"  # നിങ്ങളുടെ രഹസ്യ പാസ്‌വേഡ്
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username and password.
        st.subheader("🔒 ZANKENE V10 - Secure Access")
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.button("Login", on_click=password_entered)
        return False
    elif not st.session_state["password_correct"]:
        # Password incorrect, show input + error.
        st.subheader("🔒 ZANKENE V10 - Secure Access")
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.button("Login", on_click=password_entered)
        st.error("😕 User ID or Password incorrect")
        return False
    else:
        # Password correct.
        return True

if not check_password():
    st.stop()  # Do not run the rest of the app if password is incorrect

# --- Main Dashboard Application ---
st.title("👑 ZANKENE V10 MISSION CONTROL DASHBOARD")
st.caption("Unified Package Engine • Multi-Model Mesh • Mega Autonomous Pipeline • REST Backend")

API_BASE_URL = "http://127.0.0.1:8000/api/v1"

# Initialize LLM Engine for model discovery
llm_mesh = ZankeneLLMEngine(model_name="llama3")
available_models = llm_mesh.list_local_models()

# Sidebar - Controls & Status
st.sidebar.header("🕹️ Control Panel")

# Model Switcher Dropdown in Sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("🧠 Active LLM Engine Mesh")
selected_model = st.sidebar.selectbox("Select Active Model:", available_models, index=0)
st.sidebar.info(f"Active Mesh Model: **{selected_model}**")
st.sidebar.markdown("---")

selected_tab = st.sidebar.radio("Navigation", [
    "📊 Engine Telemetry & Analytics", 
    "🔥 Mega Autonomous Campaign",
    "🌐 Live Web Search Agent",
    "📧 Automated Email Dispatcher",
    "🦙 LLM Single Agent (via REST API)", 
    "🔗 Multi-Agent Pipeline (via REST API)", 
    "💾 Audit DB Logs"
])

# Check FastAPI Backend Server Status
@st.cache_data(ttl=5)
def check_api_health():
    try:
        res = requests.get("http://127.0.0.1:8000/", timeout=2)
        if res.status_code == 200:
            return True, res.json()
    except Exception:
        pass
    return False, None

api_online, api_info = check_api_health()

# Load Agents
@st.cache_resource
def get_registered_agents():
    return load_all_agents()

agents = get_registered_agents()

# -------------------------------------------------------------------
# TAB 1: Engine Telemetry & Analytics
# -------------------------------------------------------------------
if selected_tab == "📊 Engine Telemetry & Analytics":
    st.subheader("⚡ Active Engine Worker Pool & Backend Health")
    
    col1, col2, col3, col4 = st.columns(4)
    if api_online:
        col1.metric("FastAPI Server", "ONLINE 🟢")
    else:
        col1.metric("FastAPI Server", "OFFLINE 🔴")
        
    col2.metric("Worker Pool", "4 Concurrent")
    col3.metric("Rate Limit Gateway", "Active 🛡️")
    col4.metric("LLM Model Mesh", f"{selected_model} 🧠")

    st.markdown("---")
    st.subheader("📈 Agent Performance & Execution Analytics")

    if api_online:
        try:
            res = requests.get(f"{API_BASE_URL}/logs", timeout=5)
            if res.status_code == 200:
                logs = res.json().get("logs", [])
                if logs:
                    df = pd.DataFrame(logs, columns=["ID", "Task ID", "Task Name", "Status", "Timestamp"])
                    
                    chart_col1, chart_col2 = st.columns(2)

                    with chart_col1:
                        st.markdown("#### 🟢 Execution Status Ratio")
                        status_counts = df["Status"].value_counts()
                        st.bar_chart(status_counts)

                    with chart_col2:
                        st.markdown("#### 🤖 Top Executed Task Types")
                        df["Task Group"] = df["Task Name"].apply(lambda x: str(x).split(":")[0] if ":" in str(x) else str(x))
                        task_counts = df["Task Group"].value_counts()
                        st.bar_chart(task_counts)

                    st.markdown("---")
                    st.markdown("#### ⏱️ Recent Task Activity Stream")
                    st.dataframe(df.head(10), width="stretch")
                else:
                    st.info("No log data available to build analytics charts yet.")
        except Exception as e:
            st.error(f"Error loading analytics data: {e}")
    else:
        st.warning("⚠️ FastAPI server is OFFLINE. Start server to fetch real-time analytics graphics!")

# -------------------------------------------------------------------
# TAB 2: Mega Autonomous Campaign
# -------------------------------------------------------------------
elif selected_tab == "🔥 Mega Autonomous Campaign":
    st.subheader("🚀 End-to-End Autonomous Intelligence & Outreach Campaign")
    st.info(f"Executes Web Scraping -> Lead Strategy -> Pitch Generation -> SMTP Dispatch using **{selected_model}**.")

    col_mega1, col_mega2 = st.columns(2)
    with col_mega1:
        campaign_topic = st.text_input("Campaign Search Topic:", value="Latest B2B AI Automation trends 2026")
    with col_mega2:
        target_audience = st.text_input("Target Audience / Segment:", value="SaaS Enterprise Founders")

    st.markdown("##### 📧 Optional Live Mail Dispatch Settings")
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        mega_sender = st.text_input("Sender Gmail:", placeholder="your_email@gmail.com")
    with col_m2:
        mega_pass = st.text_input("App Password:", type="password")
    with col_m3:
        mega_recipient = st.text_input("Target Email:", placeholder="client@example.com")

    if st.button("🔥 Run End-to-End Mega Campaign", type="primary"):
        with st.spinner("Executing multi-stage autonomous pipeline..."):
            start_time = time.time()
            mega = ZankeneMegaPipeline(model_name=selected_model)
            res = mega.run_autonomous_campaign(
                topic=campaign_topic,
                target_segment=target_audience,
                sender_email=mega_sender if mega_sender else None,
                sender_password=mega_pass if mega_pass else None,
                recipient_email=mega_recipient if mega_recipient else None
            )
            elapsed = round(time.time() - start_time, 2)

            st.success(f"Campaign Successfully Executed in {elapsed}s!")

            with st.expander("🌐 Stage 1: Web Intelligence Summary"):
                st.write(res["search_summary"])

            with st.expander("🎯 Stage 2: Lead Hunter Strategy"):
                st.write(res["strategy"])

            st.markdown("### ✉️ Stage 3: Auto-Generated Outreach Pitch")
            st.markdown(f"> {res['pitch']}")

            if res["mail_sent"]:
                st.success(f"✅ Outbound email successfully dispatched to {mega_recipient}!")

# -------------------------------------------------------------------
# TAB 3: Live Web Search Agent
# -------------------------------------------------------------------
elif selected_tab == "🌐 Live Web Search Agent":
    st.subheader("🌐 Autonomous Real-Time Web Search & Intelligence Agent")
    st.info(f"Fetches live search context from DuckDuckGo and analyzes real-time insights using **{selected_model}**.")

    search_query = st.text_input("Enter Search Topic / Query:", value="Latest B2B AI Automation trends 2026")

    if st.button("🔍 Search Web & Analyze", type="primary"):
        with st.spinner(f"Searching live web & gathering intelligence via {selected_model}..."):
            start_time = time.time()
            search_agent = ZankeneWebSearchAgent(model_name=selected_model)
            response = search_agent.run_live_search_task(search_query)
            elapsed = round(time.time() - start_time, 2)

            st.success(f"Intelligence Gathering Completed in {elapsed}s using {selected_model}!")
            st.markdown("### 📋 Web Intelligence Summary:")
            st.markdown(f"> {response}")

# -------------------------------------------------------------------
# TAB 4: Automated Email Dispatcher
# -------------------------------------------------------------------
elif selected_tab == "📧 Automated Email Dispatcher":
    st.subheader("📧 Outbound B2B Mail Delivery Gateway")
    st.info("Dispatch AI-generated cold pitches directly to clients via SMTP authentication.")

    col_mail1, col_mail2 = st.columns(2)

    with col_mail1:
        sender_email = st.text_input("Sender Email (Gmail):", placeholder="your_email@gmail.com")
        sender_password = st.text_input("App Password:", type="password", help="Use Gmail App Password")

    with col_mail2:
        recipient_email = st.text_input("Recipient Email:", placeholder="client@example.com")
        email_subject = st.text_input("Email Subject:", value="Transforming Enterprise Workflows with AI")

    email_body = st.text_area("Email Body / Pitch:", value="Hello Team,\n\nOur autonomous AI agents can automate 80% of your operational workflows.\n\nBest,\nZANKENE Ecosystem Engine", height=150)

    if st.button("🚀 Send Outbound Mail", type="primary"):
        if not sender_email or not sender_password or not recipient_email:
            st.error("Please fill in Sender Email, App Password, and Recipient Email!")
        else:
            with st.spinner("Connecting to SMTP server and delivering email..."):
                dispatcher = ZankeneEmailAgent()
                success = dispatcher.send_email(
                    sender_email=sender_email,
                    sender_password=sender_password,
                    recipient_email=recipient_email,
                    subject=email_subject,
                    body=email_body
                )
                if success:
                    st.success(f"✅ Email successfully dispatched to {recipient_email}!")
                else:
                    st.error("❌ Failed to send email. Check credentials and SMTP connection.")

# -------------------------------------------------------------------
# TAB 5: LLM Single Agent via REST API
# -------------------------------------------------------------------
elif selected_tab == "🦙 LLM Single Agent (via REST API)":
    st.subheader("🦙 Dispatch Single Agent Task via FastAPI REST Endpoint")
    
    agent_names = list(agents.keys()) if agents else ["lead_hunter_assistant", "developer", "security_guard"]
    
    selected_agent = st.selectbox("Select Active Agent Module:", agent_names)
    prompt_text = st.text_area("Task Instructions / Prompt:", value="Analyze current B2B SaaS market trends and give 3 key takeaways.", height=120)

    if st.button("🚀 Dispatch via FastAPI Endpoint", type="primary"):
        if not api_online:
            st.error("FastAPI backend is offline! Start server first.")
        else:
            with st.spinner(f"Dispatching task to FastAPI backend for {selected_agent}..."):
                start_time = time.time()
                payload = {
                    "task_id": int(time.time()),
                    "task_name": f"Dashboard Task: {selected_agent}",
                    "agent_name": selected_agent,
                    "prompt": prompt_text
                }
                
                try:
                    res = requests.post(f"{API_BASE_URL}/dispatch", json=payload, timeout=60)
                    elapsed = round(time.time() - start_time, 2)
                    
                    if res.status_code == 200:
                        data = res.json()
                        st.success(f"Task Executed via REST API in {elapsed}s! Logged to SQLite DB & Memory Vault.")
                        st.markdown("### 📋 Agent Response:")
                        st.markdown(f"> {data.get('response')}")
                    else:
                        st.error(f"API Error ({res.status_code}): {res.text}")
                except Exception as e:
                    st.error(f"Failed to connect to API: {e}")

# -------------------------------------------------------------------
# TAB 6: Multi-Agent Pipeline via REST API
# -------------------------------------------------------------------
elif selected_tab == "🔗 Multi-Agent Pipeline (via REST API)":
    st.subheader("🔗 3-Stage Pipeline Chain via FastAPI Endpoint")
    st.info("Dispatches sequential multi-agent orchestration request to `/api/v1/pipeline`.")

    pipeline_input = st.text_input("Pipeline Campaign Goal:", value="Enterprise AI Automation Outreach Campaign")

    if st.button("⛓️ Dispatch Pipeline Chain via API", type="primary"):
        if not api_online:
            st.error("FastAPI backend is offline! Start server first.")
        else:
            with st.spinner("Dispatching multi-agent pipeline chain request to FastAPI..."):
                chain_payload = {
                    "campaign_goal": pipeline_input,
                    "chain": [
                        {
                            "agent_name": "lead_hunter_assistant",
                            "role": "You are LeadHunter, an expert in lead generation.",
                            "instruction": f"Identify 2 target segments for {pipeline_input}."
                        },
                        {
                            "agent_name": "outreach_engine",
                            "role": "You are OutreachEngine, a master B2B email copywriter.",
                            "instruction": "Write a 3-sentence cold email pitch targeting those segments."
                        },
                        {
                            "agent_name": "qa_guard",
                            "role": "You are QA_Guard, a strict quality auditor.",
                            "instruction": "Review the email pitch. Give a score out of 10 and 1 improvement."
                        }
                    ]
                }

                try:
                    res = requests.post(f"{API_BASE_URL}/pipeline", json=chain_payload, timeout=90)
                    if res.status_code == 200:
                        data = res.json()
                        st.success("Pipeline Chain Successfully Dispatched & Executed via REST API!")
                        
                        st.markdown("### 📜 Stage-by-Stage History:")
                        for item in data.get("history", []):
                            with st.expander(f"Stage {item['stage']}: {item['agent_name']}"):
                                st.write(item["output"])

                        st.markdown("### 🏁 Final Audit Score & Feedback:")
                        st.markdown(f"> {data.get('final_output')}")
                    else:
                        st.error(f"API Error ({res.status_code}): {res.text}")
                except Exception as e:
                    st.error(f"Failed to connect to API: {e}")

# -------------------------------------------------------------------
# TAB 7: Audit DB Logs
# -------------------------------------------------------------------
elif selected_tab == "💾 Audit DB Logs":
    st.subheader("💾 Real-Time SQLite Audit Logs (Fetched via `/api/v1/logs`)")
    
    if st.button("🔄 Refresh Logs"):
        st.rerun()

    if api_online:
        try:
            res = requests.get(f"{API_BASE_URL}/logs", timeout=5)
            if res.status_code == 200:
                logs = res.json().get("logs", [])
                if logs:
                    log_df = pd.DataFrame(logs, columns=["ID", "Task ID", "Task Name", "Status", "Timestamp"])
                    st.dataframe(log_df, width="stretch")
                else:
                    st.warning("No execution logs found in database.")
        except Exception as e:
            st.error(f"Error fetching logs via API: {e}")
    else:
        st.error("FastAPI server is offline. Cannot fetch logs via REST endpoint.")