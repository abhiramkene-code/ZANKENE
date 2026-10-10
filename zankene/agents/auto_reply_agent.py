class AutoReplyAgent:
    def __init__(self, booking_link="https://calendly.com/abhiramkene/30min"):
        self.booking_link = booking_link
        print("👔 [PRO AUTO-REPLY] Inbox Intent Monitor Online.")

    def analyze_intent(self, incoming_email_body: str) -> str:
        body_lower = incoming_email_body.lower()
        if any(w in body_lower for w in ["interested", "call", "meet", "discuss", "time", "demo", "yes", "sure"]):
            return "INTERESTED"
        elif any(w in body_lower for w in ["pricing", "cost", "details", "portfolio", "more info"]):
            return "INFO_REQUESTED"
        elif any(w in body_lower for w in ["not interested", "unsubscribe", "remove", "no thanks"]):
            return "NOT_INTERESTED"
        return "GENERAL_QUERY"

    def generate_reply(self, sender_name: str, incoming_email_body: str) -> dict:
        intent = self.analyze_intent(incoming_email_body)
        if intent == "INTERESTED":
            subject = "Re: Executive Briefing | ZANKENE AI Systems"
            body = (
                f"Dear {sender_name},\n\n"
                f"Thank you for your response. I would be glad to demonstrate our multi-agent architecture.\n\n"
                f"Please reserve a suitable time slot directly on my calendar:\n"
                f"👉 {self.booking_link}\n\n"
                f"Best regards,\n\n"
                f"Abhiram P.\n"
                f"Founder & Chief AI Architect | ZANKENE AI Systems"
            )
        elif intent == "NOT_INTERESTED":
            subject = "Re: Confirmation | ZANKENE AI Systems"
            body = f"Dear {sender_name},\n\nThank you for letting me know. I have updated our records accordingly.\n\nBest regards,\nAbhiram P."
        else:
            subject = "Re: ZANKENE AI Infrastructure Overview"
            body = (
                f"Dear {sender_name},\n\n"
                f"Thank you for reaching out. Feel free to book a slot here to discuss:\n"
                f"👉 {self.booking_link}\n\n"
                f"Best regards,\nAbhiram P."
            )
        return {"intent": intent, "subject": subject, "body": body}