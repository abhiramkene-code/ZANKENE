import os
import importlib
import logging

def load_all_agents():
    agents_map = {}
    current_dir = os.path.dirname(__file__)
    
    if os.path.exists(current_dir):
        for file in os.listdir(current_dir):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]
                try:
                    module = importlib.import_module(f"zankene.agents.{module_name}")
                    agents_map[module_name] = module
                except Exception as e:
                    logging.debug(f"Skipped loading legacy agent '{module_name}': {e}")
                    
    logging.info(f"🤖 [ZANKENE AGENTS] Loaded {len(agents_map)} Active Agents.")
    return agents_map

# Pipeline ഇമ്പോർട്ട് മെയിൻ ഫോൾഡറിലേക്ക് മാറ്റിയത് കൊണ്ട് ഇവിടെ നിന്ന് ഒഴിവാക്കാം