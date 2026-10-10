import logging
import time

class ZankeneTelemetryEngine:
    def __init__(self):
        self.total_executed = 0
        self.total_latency_ms = 0.0
        logging.info("📊 [ZANKENE TELEMETRY] Metrics Collector Active.")

    def record_metric(self, start_time):
        latency = round((time.time() - start_time) * 1000, 2)
        self.total_executed += 1
        self.total_latency_ms += latency
        logging.info(f"⏱️ [TELEMETRY] Task Latency: {latency} ms")

    def get_summary(self):
        avg = round(self.total_latency_ms / self.total_executed, 2) if self.total_executed > 0 else 0
        return {"total_executed": self.total_executed, "avg_latency_ms": avg}