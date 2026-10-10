import os
import subprocess
import webbrowser
import platform

class SystemControllerAgent:
    def __init__(self):
        print(f"🤖 [SUPER AI - OS CONTROLLER] Workstation Controller Online on {platform.system()}!")

    def open_application(self, app_name: str):
        """
        ലാപ്‌ടോപ്പിലെ പ്രധാന ആപ്പുകളും സോഫ്റ്റ്‌വെയറുകളും തനിയെ ഓപ്പൺ ചെയ്യുന്നു.
        """
        app_name_lower = app_name.lower()
        print(f"⚙️ [SYSTEM AI] Launching Application: {app_name}...")

        if "browser" in app_name_lower or "chrome" in app_name_lower:
            webbrowser.open("https://www.google.com")
        elif "upwork" in app_name_lower:
            webbrowser.open("https://www.upwork.com")
        elif "apollo" in app_name_lower:
            webbrowser.open("https://app.apollo.io")
        elif "vscode" in app_name_lower:
            subprocess.Popen(["code", "."])
        else:
            print(f"⚠️ App {app_name} command triggered!")

    def execute_terminal_command(self, command: str):
        """
        നിന്റെ ടെർമിനലിൽ വരുന്ന കമാൻഡുകൾ തനിയെ റൺ ചെയ്യുന്നു.
        """
        print(f"💻 [SYSTEM AI] Executing Command: '{command}'")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Error executing command: {e}"

if __name__ == "__main__":
    controller = SystemControllerAgent()
    # Test System Automation
    print("🤖 Testing Autonomous System Trigger...")
    controller.open_application("upwork")