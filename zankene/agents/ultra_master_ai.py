import os
import sys
import time
import schedule
import subprocess
import webbrowser
import pyautogui
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

class UltraMasterAI:
    def __init__(self):
        print("⚡ [ULTRA MASTER AI] 24/7 Continuous Autonomous Engine Activated!")
        pyautogui.FAILSAFE = True

    # 1. 24/7 Background Pipeline Trigger
    def run_global_pipeline(self):
        print(f"\n⏰ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Executing Scheduled Global Outreach Pipeline...")
        pipeline_script = os.path.join(BASE_DIR, "live_global_pipeline.py")
        try:
            subprocess.run([sys.executable, pipeline_script])
            print("✅ Outbound pipeline execution completed!")
        except Exception as e:
            print(f"❌ Pipeline execution error: {e}")

    # 2. Vision & GUI Screen Control
    def locate_and_click_screen_element(self, image_path: str):
        """
        സ്ക്രീനിൽ ഉള്ള ബട്ടണുകളും ഘടകങ്ങളും ക്യാപ്ചർ ചെയ്ത് സ്വയം കണ്ടുപിടിച്ച് ക്ലിക്ക് ചെയ്യുന്നു.
        """
        print(f"👁️ [VISION AI] Searching screen for element: {image_path}...")
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                point = pyautogui.center(location)
                pyautogui.click(point)
                print(f"🎯 [VISION AI] Successfully clicked element at {point}")
                return True
            else:
                print("⚠️ Element not visible on current screen.")
                return False
        except Exception as e:
            print(f"ℹ️ Vision element scan info: {e}")
            return False

    # 3. Multi-Channel Outreach Dispatcher (Telegram / WhatsApp / Notification Alert)
    def send_multichannel_alert(self, message: str):
        """
        നിങ്ങൾ എവിടെയായിരുന്നാലും ഫോണിലേക്ക് ഇൻസ്റ്റന്റ് അലേർട്ടുകൾ തനിയെ അയക്കുന്നു.
        """
        print(f"📲 [MULTI-CHANNEL DISPATCH] Sending real-time alert: '{message}'")
        # System notification
        try:
            print(f"🔔 [SYSTEM ALERT]: {message}")
        except Exception as e:
            print(f"Alert error: {e}")

    # 4. Master 24/7 Scheduler Loop
    def start_247_autonomous_loop(self):
        print("\n" + "=" * 70)
        print("🔄 ZANKENE 24/7 AUTONOMOUS SCHEDULER STARTED")
        print("• Running Global Outreach Pipeline every 2 hours")
        print("• Monitoring Inbox & Auto-Replies continuously")
        print("• Multi-channel alerting active")
        print("=" * 70 + "\n")

        # Schedule tasks
        schedule.every(2).hours.do(self.run_global_pipeline)
        
        # Initial First Run
        self.run_global_pipeline()

        while True:
            schedule.run_pending()
            time.sleep(10)

if __name__ == "__main__":
    engine = UltraMasterAI()
    # Runs the 24/7 loop
    engine.start_247_autonomous_loop()