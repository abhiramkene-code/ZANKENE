import asyncio
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 59 SYSTEM-GUARDIAN] - %(levelname)s - %(message)s'
)

class Day59SystemGuardianEngine:
    def __init__(self, high_load_threshold=80):
        self.high_load_threshold = high_load_threshold
        logging.info("🤖 ZANKENE Day 59 Autonomous System Guardian & Self-Healing Active.")

    async def monitor_and_process_task(self, task_id, task_name, priority, simulated_system_load):
        logging.info(f"🔍 [HEALTH CHECK] Task #{task_id} ('{task_name}') - Current System Load: {simulated_system_load}%")

        # Load Shedding Trigger for Low Priority Tasks under heavy system load
        if simulated_system_load > self.high_load_threshold and priority == "LOW":
            logging.warning(f"🛑 [LOAD SHEDDING TRIGGERED] High System Load ({simulated_system_load}%)! Deferring LOW Priority Task #{task_id}.")
            return {"status": "DEFERRED", "task_id": task_id}

        # Processing Task
        logging.info(f"⚡ [EXECUTING] Processing {priority} Priority Task #{task_id}...")
        await asyncio.sleep(0.3)
        logging.info(f"✅ [SUCCESS] Task #{task_id} Processed Cleanly.")
        return {"status": "SUCCESS", "task_id": task_id}

    async def run_day59_pipeline(self):
        print("\n=================================================================")
        print("🤖 ZANKENE DAY 59: AUTONOMOUS GUARDIAN & LOAD SHEDDING ENGINE 🤖")
        print("=================================================================\n")

        workloads = [
            (1101, "Critical Financial Settlement", "HIGH", 45),
            (1102, "Routine Analytics Dump", "LOW", 88),         # Should trigger Load Shedding
            (1103, "Enterprise Security Audit Log", "HIGH", 92), # HIGH Priority passes even under load
            (1104, "Background Cache Clean", "LOW", 85)          # Should trigger Load Shedding
        ]

        tasks = [self.monitor_and_process_task(tid, tname, prio, load) for tid, tname, prio, load in workloads]
        results = await asyncio.gather(*tasks)

        processed = sum(1 for r in results if r["status"] == "SUCCESS")
        shedded = sum(1 for r in results if r["status"] == "DEFERRED")

        print("\n-----------------------------------------------------------------")
        logging.info(f"📊 [GUARDIAN HEALTH REPORT] Processed: {processed} | Load-Shedded: {shedded}")
        print("-----------------------------------------------------------------")

        print("\n🎉 Day 59 Autonomous Guardian & System Self-Healing Complete!")

if __name__ == "__main__":
    guardian = Day59SystemGuardianEngine()
    asyncio.run(guardian.run_day59_pipeline())