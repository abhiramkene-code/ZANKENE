import sys
import os

# Add root directory to sys.path so Python can find 'zankene'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import schedule
from zankene.pipeline import ZankeneAgentPipeline
from zankene.database import log_campaign
from zankene.mailer import send_outreach_email

def run_daily_campaign_job():
    print("[INFO] 🚀 Daily Autonomous Campaign Started by Background Scheduler...")
    topic_name = "Latest B2B AI Automation and Workflow Optimization trends 2026"
    
    # Configure your sender details here for automated dispatch
    SENDER_EMAIL = "your_email@gmail.com"
    APP_PASSWORD = "your_app_password"
    TARGET_EMAIL = "client@example.com"
    
    try:
        mega = ZankeneAgentPipeline(model_name="llama3")
        res = mega.run_pipeline(topic_name)
        
        result_str = str(res)
        preview_text = result_str[:150]
        
        # Log success to Database
        log_campaign(topic=topic_name, status="SUCCESS", preview=preview_text)
        
        # Optional: Uncomment below line once you configure your actual sender email & app password
        # send_outreach_email(SENDER_EMAIL, APP_PASSWORD, TARGET_EMAIL, "Take the Lead in AI-Powered Automation", result_str)
        
        print(f"-> Pipeline Executed Successfully. Result: {preview_text}...")
        print("[SUCCESS] ✅ Daily Campaign Executed & Logged to DB Successfully!")
    except Exception as e:
        error_msg = str(e)
        log_campaign(topic=topic_name, status="ERROR", preview=error_msg[:150])
        print(f"[ERROR] ❌ Error in Daily Campaign Job: {e}")

def start_scheduler():
    print("👑 ZANKENE V10 Background Scheduler is ONLINE and waiting for schedule...")
    schedule.every().day.at("05:00").do(run_daily_campaign_job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_daily_campaign_job() # Runs immediately on start for test
    start_scheduler()
    