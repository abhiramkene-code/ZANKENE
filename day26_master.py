import asyncio
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 26 LOAD BALANCER] - %(levelname)s - %(message)s'
)

class Day26DynamicLoadBalancer:
    def __init__(self):
        self.nodes = ["Node-Alpha", "Node-Beta", "Node-Gamma"]
        logging.info("ZANKENE Day 26 Dynamic Load Balancer & Task Offloader Active.")

    async def dispatch_task(self, task_id, workload_name):
        selected_node = random.choice(self.nodes)
        logging.info(f"⚖️ Offloading Task #{task_id} ('{workload_name}') -> Distributed to [{selected_node}]")
        await asyncio.sleep(0.8)
        logging.info(f"✅ [{selected_node}] Finished processing Task #{task_id}")
        return {"task_id": task_id, "node": selected_node, "status": "COMPLETED"}

    async def run_day26_pipeline(self):
        print("\n=======================================================")
        print("⚖️ ZANKENE DAY 26: DYNAMIC LOAD BALANCER & OFFLOADER ⚖️")
        print("=======================================================\n")
        
        heavy_tasks = [
            (501, "Deep Web Data Mining"),
            (502, "LLM Fine-Tuning Batch Processing"),
            (503, "High-Resolution Image Processing"),
            (504, "Bulk Email Campaign Dispatch"),
            (505, "Automated Code Vulnerability Audit")
        ]

        tasks = [self.dispatch_task(tid, name) for tid, name in heavy_tasks]
        await asyncio.gather(*tasks)

        print("\n🎉 Day 26 Load Balancer & Offloader Setup Complete!")

if __name__ == "__main__":
    balancer = Day26DynamicLoadBalancer()
    asyncio.run(balancer.run_day26_pipeline())