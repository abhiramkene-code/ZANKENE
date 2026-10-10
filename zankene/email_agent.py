import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

class ZankeneEmailAgent:
    def __init__(self, smtp_server: str = "smtp.gmail.com", port: int = 587):
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, sender_email: str, sender_password: str, recipient_email: str, subject: str, body: str) -> bool:
        """Sends an outbound email using SMTP authentication."""
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            logging.info(f"📧 [EMAIL AGENT] Connecting to {self.smtp_server}:{self.port}...")
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(sender_email, sender_password)
            
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            
            logging.info(f"✅ [EMAIL SENT] Successfully dispatched email to {recipient_email}")
            return True
        except Exception as e:
            logging.error(f"❌ [EMAIL ERROR] Failed to send email: {e}")
            return False