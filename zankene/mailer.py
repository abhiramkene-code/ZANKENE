import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_outreach_email(sender_email, app_password, target_email, subject, body):
    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login using Gmail and App Password
        server.login(sender_email, app_password)
        
        # Construct email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = target_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server.sendmail(sender_email, target_email, msg.as_string())
        server.quit()
        
        print(f"[SUCCESS] 📧 Email successfully dispatched to {target_email}!")
        return True
    except Exception as e:
        print(f"[ERROR] ❌ Failed to send email: {e}")
        return False