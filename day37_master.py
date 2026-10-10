import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 37 TRANSACTION] - %(levelname)s - %(message)s'
)

class Day37TransactionManager:
    def __init__(self):
        self.execution_history = []
        logging.info("ZANKENE Day 37 Workflow Transaction & Rollback Manager Active.")

    async def execute_step(self, step_name, action_func, rollback_func):
        logging.info(f"⚙️ Executing Step: '{step_name}'...")
        await asyncio.sleep(0.5)
        success = await action_func()

        if success:
            self.execution_history.append((step_name, rollback_func))
            logging.info(f"✅ Step '{step_name}' committed to transaction log.")
            return True
        else:
            logging.error(f"❌ Step '{step_name}' FAILED! Triggering Transaction Rollback...")
            await self.rollback_all()
            return False

    async def rollback_all(self):
        logging.warning("⚠️ INITIATING WORKFLOW ROLLBACK PROCEDURE...")
        for step_name, rollback_func in reversed(self.execution_history):
            await asyncio.sleep(0.4)
            await rollback_func()
            logging.info(f"🔄 Rollback completed for: '{step_name}'")
        self.execution_history.clear()

    async def run_day37_pipeline(self):
        print("\n=======================================================")
        print("🔄 ZANKENE DAY 37: WORKFLOW TRANSACTION & ROLLBACK 🔄")
        print("=======================================================\n")

        # Dummy action and rollback steps
        async def step1_act(): return True
        async def step1_rb(): logging.info("Reverting Step 1: Cleared temp lead files")

        async def step2_act(): return True
        async def step2_rb(): logging.info("Reverting Step 2: Deleted draft proposal")

        async def step3_act(): return False  # Simulating failure on Step 3
        async def step3_rb(): logging.info("Reverting Step 3: Voided API allocation")

        s1 = await self.execute_step("Fetch Lead Data", step1_act, step1_rb)
        s2 = await self.execute_step("Generate Proposal Draft", step2_act, step2_rb)
        s3 = await self.execute_step("Charge Client Account", step3_act, step3_rb)

        if not s3:
            print("\n🎉 Day 37 Safe Rollback Execution Completed Successfully!")

if __name__ == "__main__":
    tx = Day37TransactionManager()
    asyncio.run(tx.run_day37_pipeline())