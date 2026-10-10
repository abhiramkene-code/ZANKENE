import asyncio
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 52 AUTOSCALER] - %(levelname)s - %(message)s'
)

class Day52ParallelWorkerPool:
    def __init__(self, initial_workers=2, max_workers=5):
        self.current_workers = initial_workers
        self.max_workers = max_workers
        self.queue = asyncio.Queue()
        logging.info(f"⚡ ZANKENE Day 52 Parallel Worker Pool Active (Initial Workers: {initial_workers}, Max Limit: {max_workers}).")

    async def worker_node(self, worker_id):
        while True:
            task = await self.queue.get()
            if task is None:
                break
            
            task_id, task_name = task
            logging.info(f"🚀 [WORKER-{worker_id}] Executing Task #{task_id} ('{task_name}')...")
            await asyncio.sleep(random.uniform(0.3, 0.7))  # Concurrent processing simulation
            logging.info(f"✅ [WORKER-{worker_id}] Completed Task #{task_id} ('{task_name}')")
            self.queue.task_done()

    async def autoscale_pool(self, pending_tasks_count):
        if pending_tasks_count > 3 and self.current_workers < self.max_workers:
            needed = min(self.max_workers - self.current_workers, pending_tasks_count - 3)
            self.current_workers += needed
            logging.warning(f"📈 [AUTOSCALE TRIGGERED] High Workload Detected! Scaled up pool +{needed} workers -> Total Active: {self.current_workers}")

    async def run_day52_pipeline(self):
        print("\n=================================================================")
        print("📈 ZANKENE DAY 52: PARALLEL WORKER POOL & AUTOSCALING ENGINE 📈")
        print("=================================================================\n")

        workloads = [
            (951, "High-Speed Lead Scrape"),
            (952, "Parallel Fraud Detection Audit"),
            (953, "Async Proposal Dispatcher"),
            (954, "Real-time Telemetry Parsing"),
            (955, "Auto-Scaling Load Test Payload"),
            (956, "Database Connection Health Check")
        ]

        # Trigger autoscaling logic based on queue pressure
        await self.autoscale_pool(len(workloads))

        # Start dynamic worker tasks
        workers = [
            asyncio.create_task(self.worker_node(i + 1)) 
            for i in range(self.current_workers)
        ]

        for task in workloads:
            await self.queue.put(task)

        await self.queue.join()

        # Stop workers gracefully
        for _ in range(self.current_workers):
            await self.queue.put(None)

        await asyncio.gather(*workers)

        print("\n🎉 Day 52 Parallel Worker Pool & Autoscaling Execution Complete!")

if __name__ == "__main__":
    engine = Day52ParallelWorkerPool()
    asyncio.run(engine.run_day52_pipeline())