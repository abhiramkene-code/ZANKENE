import asyncio
import logging
import json
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 34 BUDGET] - %(levelname)s - %(message)s'
)

class Day34TokenBudgetController:
    def __init__(self, daily_budget_usd=10.0, storage_file="token_budget_tracker.json"):
        self.daily_budget = daily_budget_usd
        self.storage_file = Path(storage_file)
        self.total_cost = self._load_current_usage()
        logging.info(f"ZANKENE Day 34 Token Cost & Budget Controller Active (Daily Cap: ${self.daily_budget}).")

    def _load_current_usage(self):
        if self.storage_file.exists():
            with open(self.storage_file, "r") as f:
                try:
                    data = json.load(f)
                    return data.get("total_cost_usd", 0.0)
                except json.JSONDecodeError:
                    return 0.0
        return 0.0

    def _save_usage(self):
        with open(self.storage_file, "w") as f:
            json.dump({"total_cost_usd": round(self.total_cost, 4)}, f, indent=4)

    async def consume_tokens(self, agent_name, token_count, cost_per_1k=0.002):
        cost = (token_count / 1000.0) * cost_per_1k
        logging.info(f"💵 [{agent_name}] Consumed {token_count} tokens (~${cost:.4f})")
        await asyncio.sleep(0.4)

        if self.total_cost + cost > self.daily_budget:
            logging.warning(f"🚨 [BUDGET CAP REACHED] Over cap! Throttling request for [{agent_name}]...")
            return {"status": "THROTTLED", "cost": cost}

        self.total_cost += cost
        self._save_usage()
        logging.info(f"✅ Budget Approved. Cumulative Daily Usage: ${self.total_cost:.4f} / ${self.daily_budget:.2f}")
        return {"status": "APPROVED", "cost": cost}

    async def run_day34_pipeline(self):
        print("\n=======================================================")
        print("💰 ZANKENE DAY 34: TOKEN COST & BUDGET CONTROLLER 💰")
        print("=======================================================\n")

        requests = [
            ("LeadHunterAgent", 1500),
            ("ProposalAgent", 4500),
            ("SecurityAgent", 2000),
            ("AnalyticsAgent", 1200)
        ]

        tasks = [self.consume_tokens(agent, tokens) for agent, tokens in requests]
        await asyncio.gather(*tasks)

        print("\n🎉 Day 34 Token Cost & Budget Control Setup Complete!")

if __name__ == "__main__":
    controller = Day34TokenBudgetController()
    asyncio.run(controller.run_day34_pipeline())