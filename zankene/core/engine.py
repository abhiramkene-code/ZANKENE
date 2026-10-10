import asyncio
import logging

class ZankeneCoreEngine:
    def __init__(self, worker_count=5):
        self.worker_count = worker_count
        self.queue = asyncio.Queue()
        logging.info(f"👑 [ZANKENE CORE] Engine Active with {worker_count} Workers.")

    async def dispatch_task(self, task_id, task_name):
        await self.queue.put((task_id, task_name))
        logging.info(f"📩 [ZANKENE CORE] Task #{task_id} ('{task_name}') Queued.")

    async def start_workers(self):
        async def worker(wid):
            while True:
                task = await self.queue.get()
                if task is None:
                    break
                tid, tname = task
                logging.info(f"🚀 [WORKER-{wid}] Processing #{tid} ('{tname}')...")
                await asyncio.sleep(0.3)
                logging.info(f"✅ [WORKER-{wid}] Finished #{tid}.")
                self.queue.task_done()

        return [asyncio.create_task(worker(i + 1)) for i in range(self.worker_count)]