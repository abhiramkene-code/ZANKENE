import asyncio
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 47 CONSENSUS] - %(levelname)s - %(message)s'
)

class Day47CircuitBreaker:
    def __init__(self, failure_threshold=2):
        self.threshold = failure_threshold
        self.failures = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.threshold:
            self.state = "OPEN"
            logging.warning(f"🚨 [CIRCUIT BREAKER TRIPPED] State changed to OPEN! Routing blocked for primary agent.")

    def record_success(self):
        self.failures = 0
        self.state = "CLOSED"

class Day47ConsensusEngine:
    def __init__(self):
        self.circuit_breaker = Day47CircuitBreaker()
        logging.info("ZANKENE Day 47 Consensus Voting & Dynamic Circuit Breaker Active.")

    async def execute_consensus_voting(self, task_name, votes):
        logging.info(f"🗳️ [CONSENSUS VOTING] Gathering agent votes for '{task_name}'...")
        await asyncio.sleep(0.5)

        # Count majority decision
        tally = {}
        for agent, decision in votes:
            tally[decision] = tally.get(decision, 0) + 1

        majority_decision = max(tally, key=tally.get)
        logging.info(f"✅ [CONSENSUS REACHED] Decision for '{task_name}': '{majority_decision}' (Votes Tally: {tally})")
        return majority_decision

    async def run_day47_pipeline(self):
        print("\n=======================================================")
        print("🗳️ ZANKENE DAY 47: CONSENSUS VOTING & CIRCUIT BREAKER 🗳️")
        print("=======================================================\n")

        # Step 1: Simulate Circuit Breaker Tripping
        logging.info("⚡ Testing Primary Agent Circuit Breaker Failure Limit...")
        self.circuit_breaker.record_failure()
        self.circuit_breaker.record_failure() # Tripped to OPEN

        if self.circuit_breaker.state == "OPEN":
            logging.info("🛡️ [FAILOVER ACTIVATED] Primary Agent Circuit OPEN. Bypassing directly to Consensus Pool.")

        await asyncio.sleep(0.4)

        # Step 2: Run Multi-Agent Consensus Voting
        votes_sample = [
            ("LeadHunterAgent", "APPROVE_DEAL"),
            ("SecurityAgent", "APPROVE_DEAL"),
            ("QAGuardAgent", "REJECT_DEAL")
        ]

        await self.execute_consensus_voting("Enterprise Lead Contract Approval", votes_sample)

        print("\n🎉 Day 47 Consensus Voting & Circuit Breaker Setup Complete!")

if __name__ == "__main__":
    engine = Day47ConsensusEngine()
    asyncio.run(engine.run_day47_pipeline())