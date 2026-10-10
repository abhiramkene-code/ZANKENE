import asyncio
import logging
import time
from zankene import (
    ZankeneCoreEngine,
    ZankeneSecurityGateway,
    ZankeneSystemGuardian,
    ZankeneTelemetryEngine
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

async def main():
    print("\n=================================================================")
    print("👑 ZANKENE V10 FULL UNIFIED PACKAGE EMPIRE EXECUTIVE 👑")
    print("=================================================================\n")

    gateway = ZankeneSecurityGateway(rate_limit_max=5)
    guardian = ZankeneSystemGuardian(high_load_threshold=80)
    telemetry = ZankeneTelemetryEngine()
    engine = ZankeneCoreEngine(worker_count=3)

    workers = await engine.start_workers()

    # Test Security Check
    auth = await gateway.authenticate_and_route("Client_Alpha", "ZANKENE_SECRET_TOKEN_999", "/api/v1/leads")

    if auth["status"] == 200:
        start_time = time.time()
        
        # Test Guardian Admission
        if guardian.evaluate_task_admission(201, "HIGH", system_load=85):
            await engine.dispatch_task(201, "Production Enterprise Lead Pipeline")
            telemetry.record_metric(start_time)

    await engine.queue.join()

    for _ in workers:
        await engine.queue.put(None)
    await asyncio.gather(*workers)

    print("\n-----------------------------------------------------------------")
    logging.info(f"📋 [FINAL SYSTEM REPORT] {telemetry.get_summary()}")
    print("-----------------------------------------------------------------")
    print("\n🎉 ZANKENE All Subsystems Unified Execution Complete!")

if __name__ == "__main__":
    asyncio.run(main())