import logging
from zankene.email_agent import ZankeneEmailAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_email_agent():
    print("\n=================================================================")
    print("✉️ ZANKENE V10 AUTOMATED EMAIL DISPATCHER TEST ✉️")
    print("=================================================================\n")

    agent = ZankeneEmailAgent()
    
    # Test structure validation without sending live credentials
    print("📧 [SMTP INITIALIZED]: Agent ready for dispatch pipeline.")
    print("=================================================================")

if __name__ == "__main__":
    test_email_agent()