import os
import sys
import time
import subprocess
import webbrowser
import pyautogui

class MasterWorkstationAI:
    def __init__(self):
        print("🤖 [MASTER CONTROLLER AI] Autonomous Workstation Controller Online!")
        # Safety Fail-Safe: മൗസ് സ്ക്രീനിന്റെ മൂലയിലേക്ക് മാറ്റിയാൽ ഓട്ടോമേഷൻ നിർത്താൻ
        pyautogui.FAILSAFE = True

    def open_workspace_apps(self):
        """
        ലാപ്‌ടോപ്പിലെ പ്രധാന വെബ്‌സൈറ്റുകളും ആപ്പുകളും സ്വയം ഓപ്പൺ ചെയ്യുന്നു.
        """
        print("⚙️ [MASTER AI] Opening Workstation Apps & Dashboards...")
        
        # Open Browsers & Web Apps
        webbrowser.open("https://www.upwork.com")
        time.sleep(1)
        webbrowser.open("https://app.apollo.io")
        time.sleep(1)
        
        print("✅ Upwork & Apollo Dashboards Launched!")

    def auto_run_zankene_pipeline(self):
        """
        നിങ്ങളുടെ ZANKENE Global Pipeline തനിയെ റൺ ചെയ്യുന്നു.
        """
        print("🚀 [MASTER AI] Triggering ZANKENE Global Pipeline...")
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pipeline_script = os.path.join(base_dir, "live_global_pipeline.py")
        
        try:
            # Executes pipeline in system terminal
            subprocess.Popen([sys.executable, pipeline_script])
            print("✅ ZANKENE Pipeline initiated autonomously in background!")
        except Exception as e:
            print(f"❌ Failed to trigger pipeline: {e}")

    def execute_mouse_keyboard_action(self, action_type: str, details: str = ""):
        """
        ലാപ്‌ടോപ്പ് മൗസും കീബോർഡും മനുഷ്യനെപ്പോലെ ക്ലിക്ക് ചെയ്യാനും ടൈപ്പ് ചെയ്യാനും കൺട്രോൾ ചെയ്യുന്നു.
        """
        print(f"🖱️️ [SYSTEM AI CONTROLLER] Executing {action_type} action...")
        
        if action_type == "type_text":
            pyautogui.write(details, interval=0.05)
        elif action_type == "press_enter":
            pyautogui.press('enter')
        elif action_type == "scroll_down":
            pyautogui.scroll(-500)
        else:
            print("⚠️ Action mapped successfully.")

if __name__ == "__main__":
    ai_master = MasterWorkstationAI()
    print("\n--- MASTER AI TESTING ---")
    ai_master.open_workspace_apps()
    ai_master.auto_run_zankene_pipeline()