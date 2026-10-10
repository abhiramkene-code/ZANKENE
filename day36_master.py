import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DAY 36 REGISTRY] - %(levelname)s - %(message)s'
)

class Day36SkillRegistry:
    def __init__(self):
        self.registry = {}
        logging.info("ZANKENE Day 36 Agent Capability Discovery & Skill Registry Active.")

    def register_agent_capability(self, agent_name, capabilities):
        self.registry[agent_name] = capabilities
        logging.info(f"📝 [REGISTERED] [{agent_name}] -> Skills: {', '.join(capabilities)}")

    async def discover_best_agent_for_task(self, required_skill):
        logging.info(f"🔍 Discovery Engine searching for agent with skill: '{required_skill}'...")
        await asyncio.sleep(0.5)
        
        for agent, skills in self.registry.items():
            if required_skill in skills:
                logging.info(f"🎯 [MATCH FOUND] Assigning task to [{agent}] (Skill Match: {required_skill})")
                return agent
        
        logging.warning(f"⚠️ No dedicated agent found for skill '{required_skill}'. Routing to GeneralistAgent.")
        return "GeneralistAgent"

    async def run_day36_pipeline(self):
        print("\n=======================================================")
        print("🧩 ZANKENE DAY 36: CAPABILITY DISCOVERY & SKILL REGISTRY 🧩")
        print("=======================================================\n")
        
        # Register capabilities
        self.register_agent_capability("LeadHunterAgent", ["scraping", "lead_filtering", "enrichment"])
        self.register_agent_capability("ProposalAgent", ["copywriting", "pitch_deck", "pricing_model"])
        self.register_agent_capability("SecurityAgent", ["vulnerability_scan", "sanitization", "audit"])
        
        await asyncio.sleep(0.5)
        
        # Query tasks dynamically
        await self.discover_best_agent_for_task("pitch_deck")
        await self.discover_best_agent_for_task("vulnerability_scan")
        await self.discover_best_agent_for_task("blockchain_audit")

        print("\n🎉 Day 36 Dynamic Capability Discovery Setup Complete!")

if __name__ == "__main__":
    registry = Day36SkillRegistry()
    asyncio.run(registry.run_day36_pipeline())