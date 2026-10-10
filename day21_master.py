import asyncio
import logging
from queue import PriorityQueue
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 21 ROUTER] - %(levelname)s - %(message)s'
)

class Day21TaskRouter:
    def __init__(self):
        logging.info("ZANKENE Day 21 Intelligent Priority Task Router Active.")

    async def execute_task(self, priority, task_name):
        logging.info(f"⚡ Processing Task [Priority {priority}]: {task_name}")
        await asyncio.sleep(1)
        logging.info(f"✅ Completed High-Priority Work: {task_name}")
        return task_name

    async def run_day21_pipeline(self):
        print("\n=======================================================")
        print("🧠 ZANKENE DAY 21: INTELLIGENT TASK ROUTER & QUEUE 🧠")
        print("=======================================================\n")
        
        # Priority mapping: 1 = CRITICAL, 2 = HIGH, 3 = NORMAL
        incoming_tasks = [
            (3, "Routine Database Cleanup"),
            (1, "Critical Security Patch Update"),
            (2, "High-Ticket Lead Discovery"),
            (1, "Payment Gateway Re-authentication"),
            (3, "Weekly Analytics Summary")
        ]

        # Sorting by priority first (Priority 1 executes before Priority 3)
        sorted_tasks = sorted(incoming_tasks, key=lambda x: x[0])

        for priority, task in sorted_tasks:
            await self.execute_task(priority, task)

        print("\n🎉 Day 21 Priority Queue Routing Completed Successfully!")

if __name__ == "__main__":
    router = Day21TaskRouter()
    asyncio.run(router.run_day21_pipeline())
    