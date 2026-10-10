import os
import json
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ZANKENE AI Global Empire Dashboard",
    page_icon="👑",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = os.path.join(BASE_DIR, "global_campaign_db.json")

def load_data():
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {"campaigns": [], "total_projected_revenue_usd": 0}
    return {"campaigns": [], "total_projected_revenue_usd": 0}

db_data = load_data()
campaigns = db_data.get("campaigns", [])

# Title Header
st.title("👑 ZANKENE AI B2B SWARM EMPIRE DASHBOARD")
st.subheader("24/7 Autonomous Global Export & Micro-SaaS Operating System")
st.markdown("---")

if not campaigns:
    st.info("No campaign data found in `global_campaign_db.json`. Run `live_global_pipeline.py` first!")
else:
    # Top Metrics Bar
    total_campaigns = len(campaigns)
    total_revenue_usd = sum([int(c.get("contract_value_usd", "$6,500").replace("$", "").replace(",", "")) for c in campaigns])
    total_deposit_usd = total_revenue_usd * 0.5
    total_revenue_inr = (total_revenue_usd * 83) / 100000  # Lakhs

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🎯 Total Targets Processed", f"{total_campaigns} Clients")
    col2.metric("💰 Pipeline Revenue (USD)", f"${total_revenue_usd:,} USD")
    col3.metric("🏦 Upfront Deposit Target (50%)", f"${total_deposit_usd:,.0f} USD")
    col4.metric("🇮🇳 Pipeline Revenue (INR)", f"₹{total_revenue_inr:.2f} Lakhs")

    st.markdown("---")

    # 📈 REVENUE GRAPH SECTION
    st.header("📊 Global Pipeline Revenue & Contract Analytics")

    # Prepare DataFrame for Visualization
    chart_data = []
    for idx, c in enumerate(campaigns, 1):
        c_val = int(c.get("contract_value_usd", "$6,500").replace("$", "").replace(",", ""))
        chart_data.append({
            "Company": f"{c.get('company_name', 'Client')} ({idx})",
            "Contract Value ($)": c_val,
            "50% Upfront Deposit ($)": c_val * 0.5,
            "Date": c.get("timestamp", "")[:10]
        })

    df = pd.DataFrame(chart_data)

    col_chart1, col_chart2 = st.columns([2, 1])

    with col_chart1:
        st.subheader("📈 Deal Value per Global Target ($ USD)")
        # Streamlit Bar Chart for Individual Target Revenue
        st.bar_chart(df.set_index("Company")[["Contract Value ($)", "50% Upfront Deposit ($)"]])

    with col_chart2:
        st.subheader("🗓️ Cumulative Pipeline Growth")
        # Cumulative Sum Revenue Line Chart
        df["Cumulative Revenue ($)"] = df["Contract Value ($)"].cumsum()
        st.line_chart(df.set_index("Company")["Cumulative Revenue ($)"])

    st.markdown("---")

    # Detailed Client Campaigns Table & Proposals
    st.header("📂 Stored Global Campaigns & Outreach Details")
    for idx, c in enumerate(campaigns, 1):
        with st.expander(f"🎯 Target {idx}: {c.get('company_name')} | Status: {c.get('outreach_status', 'Step 1 Sent')} | Date: {c.get('timestamp')}"):
            st.write(f"**Target Role:** {c.get('decision_maker_role')}")
            st.write(f"**Target Email:** {c.get('target_email')}")
            st.write(f"**Contract Value:** {c.get('contract_value_usd')} | **Payment Rail:** {c.get('payment_rail', 'Wise / SWIFT Wire')}")
            
            st.subheader("📧 3-Step Outreach Sequence")
            st.json(c.get("outreach_sequence", {}))
            
            st.subheader("📄 SOW & Agreement Details")
            st.write(c.get("sow_details", {}))