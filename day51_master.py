import asyncio
import logging
import random
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 51 EVENT-DISPATCHER] - %(levelname)s - %(message)s'
)

class Day51EventDrivenDispatcher:
    def __init__(self):
        self.event_queue = asyncio.Queue()
        self.active_workers = {
            "LeadAgent": "Worker_Lead_V9",
            "SecurityAgent": "Worker_Sec_V9",
            "AnalyticsAgent": "Worker_Analytics_V9"
        }
        logging.info("⚡ ZANKENE Day 51 Dynamic Event-Driven Dispatcher Active.")

    async def produce_events(self):
        sample_events = [
            {"event_id": "EVT-901", "type": "LeadAgent", "payload": "Incoming High-Value Webhook Lead"},
            {"event_id": "EVT-902", "type": "SecurityAgent", "payload": "Unauthorized Access Attempt Alert"},
            {"event_id": "EVT-903", "type": "AnalyticsAgent", "payload": "Daily System Health Telemetry Dump"},
            {"event_id": "EVT-904", "type": "LeadAgent", "payload": "Auto-Prospecting Batch Request"}
        ]
        
        for event in sample_events:
            await asyncio.sleep(0.3)
            await self.event_queue.put(event)
            logging.info(f"📩 [EVENT PRODUCED] Emitted Event '{event['event_id']}' ({event['type']})")

    async def consume_and_dispatch(self):
        while not self.event_queue.empty() or self.producing:
            try:
                event = await asyncio.wait_for(self.event_queue.get(), timeout=1.5)
                assigned_worker = self.active_workers.get(event['type'], "Worker_Generic_V9")
                
                logging.info(f"⚡ [EVENT DISPATCHED] Event '{event['event_id']}' -> Assigned to [{assigned_worker}]")
                await asyncio.sleep(0.5)  # Simulate processing
                logging.info(f"✅ [EVENT PROCESSED] '{event['event_id']}' successfully handled by [{assigned_worker}]")
                
                self.event_queue.task_done()
            except asyncio.TimeoutError:
                break

    async def run_day51_pipeline(self):
        print("\n=================================================================")
        print("⚡ ZANKENE DAY 51: DYNAMIC EVENT-DRIVEN DISPATCHER ⚡")
        print("=================================================================\n")

        self.producing = True
        producer_task = asyncio.create_task(self.produce_events())
        
        await producer_task
        self.producing = False

        await self.consume_and_dispatch()

        print("\n🎉 Day 51 Event-Driven Micro-Agent Dispatcher Execution Complete!")

if __name__ == "__main__":
    dispatcher = Day51EventDrivenDispatcher()
    asyncio.run(dispatcher.run_day51_pipeline())