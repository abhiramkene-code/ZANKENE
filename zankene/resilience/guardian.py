import logging

class ZankeneSystemGuardian:
    def __init__(self, high_load_threshold=80):
        self.high_load_threshold = high_load_threshold
        logging.info("🤖 [ZANKENE RESILIENCE] Guardian & Load Shedder Active.")

    def evaluate_task_admission(self, task_id, priority, system_load):
        if system_load > self.high_load_threshold and priority == "LOW":
            logging.warning(f"🛑 [LOAD SHEDDING] Deferring LOW priority Task #{task_id} (Load: {system_load}%)")
            return False
        return True