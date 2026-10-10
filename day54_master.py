import asyncio
import logging
from collections import defaultdict

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 54 PUB-SUB] - %(levelname)s - %(message)s'
)

class Day54EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)
        logging.info("📡 ZANKENE Day 54 Cross-Agent Real-Time Event Bus Active.")

    def subscribe(self, event_type, subscriber_name, callback_fn):
        self.subscribers[event_type].append((subscriber_name, callback_fn))
        logging.info(f"🔗 [{subscriber_name}] Subscribed to Event Channel: '{event_type}'")

    async def publish(self, event_type, publisher_name, payload):
        logging.info(f"📢 [{publisher_name}] Published Event to Channel '{event_type}' -> Payload: {payload}")
        if event_type in self.subscribers:
            for sub_name, callback in self.subscribers[event_type]:
                logging.info(f"⚡ [EVENT BUS ROUTER] Broadcasting to Subscriber [{sub_name}]...")
                await callback(sub_name, payload)

class Day54PubSubEngine:
    def __init__(self):
        self.bus = Day54EventBus()

    async def on_lead_detected(self, subscriber_name, payload):
        await asyncio.sleep(0.2)
        logging.info(f"✅ [{subscriber_name}] Processed Broadcast Lead: '{payload['lead_name']}' (Score: {payload['score']})")

    async def on_security_alert(self, subscriber_name, payload):
        await asyncio.sleep(0.2)
        logging.warning(f"🚨 [{subscriber_name}] ACTION REQUIRED! Critical Threat Detected: '{payload['threat_type']}'")

    async def run_day54_pipeline(self):
        print("\n=================================================================")
        print("📡 ZANKENE DAY 54: CROSS-AGENT REAL-TIME PUB/SUB EVENT BUS 📡")
        print("=================================================================\n")

        # Setup Subscriptions
        self.bus.subscribe("NEW_HIGH_VALUE_LEAD", "ProposalAgent_V9", self.on_lead_detected)
        self.bus.subscribe("NEW_HIGH_VALUE_LEAD", "AnalyticsAgent_V9", self.on_lead_detected)
        self.bus.subscribe("SECURITY_ALERT", "QAGuardAgent_V9", self.on_security_alert)

        await asyncio.sleep(0.3)

        # Publish Events
        await self.bus.publish("NEW_HIGH_VALUE_LEAD", "LeadHunterAgent_V9", {
            "lead_name": "Acme Corp Enterprise",
            "score": 98
        })

        await self.bus.publish("SECURITY_ALERT", "SystemMonitorAgent_V9", {
            "threat_type": "Unauthorized API Token Use"
        })

        print("\n🎉 Day 54 Cross-Agent Event Bus & Pub/Sub Messaging Execution Complete!")

if __name__ == "__main__":
    engine = Day54PubSubEngine()
    asyncio.run(engine.run_day54_pipeline())