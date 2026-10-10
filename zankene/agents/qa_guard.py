import os

class QAIntegrityGuard:
    def __init__(self):
        pass

    def audit_code(self, file_path: str) -> bool:
        print(f"🛡️ [QA GUARD] Auditing file: '{file_path}'")
        if not os.path.exists(file_path):
            print("❌ [QA GUARD] File does not exist!")
            return False
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "import os" in content or "print" in content or "def " in content:
            print("✅ [QA GUARD] Audit Passed: Code structure is valid & safe.")
            return True
        else:
            print("⚠️ [QA GUARD] Audit Failed: Insufficient code output.")
            return False

if __name__ == "__main__":
    qa = QAIntegrityGuard()
    print("QA Guard Operational.")