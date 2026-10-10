import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

class DirectEmailSenderAgent:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.email_user = os.getenv("EMAIL_USER")
        self.email_pass = os.getenv("EMAIL_PASS")

    def send_email(self, recipient_email: str, subject: str, body: str) -> bool:
        if not self.email_user or not self.email_pass:
            print("❌ EMAIL_USER or EMAIL_PASS missing in .env")
            return False
        try:
            msg = MIMEMultipart()
            msg['From'] = f"Abhiram P. <{self.email_user}>"
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_user, self.email_pass)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"❌ SMTP Dispatch Error: {e}")
            return False