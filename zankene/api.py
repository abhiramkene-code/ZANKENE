from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
import logging

from zankene import (
    ZankeneSecurityGateway,
    ZankeneDatabase,
    ZankeneLLMEngine,
    ZankeneAgentPipeline,
    ZankeneMemoryVault
)

app = FastAPI(
    title="ZANKENE V10 Production API",
    description="Unified REST API Engine for Multi-Agent Orchestration & Local Ollama Reasoning",
    version="10.0.0"
)

# Core System Instances
db = ZankeneDatabase()
llm = ZankeneLLMEngine(model_name="llama3")
pipeline = ZankeneAgentPipeline(model_name="llama3")
vault = ZankeneMemoryVault()

class TaskDispatchReq(BaseModel):
    task_id: int
    task_name: str
    agent_name: Optional[str] = "autonomous_job_executor"
    prompt: str

class PipelineChainReq(BaseModel):
    campaign_goal: str
    chain: List[Dict[str, str]]

@app.get("/")
def read_root():
    return {"status": "ONLINE", "system": "ZANKENE V10 Unified Architecture"}

@app.get("/api/v1/logs")
def get_audit_logs():
    return {"logs": db.fetch_all_logs()}

@app.post("/api/v1/dispatch")
def dispatch_single_agent_task(req: TaskDispatchReq):
    try:
        # Security Gateway Verification
        security = ZankeneSecurityGateway()
        
        # Check if attribute exists safely, otherwise pass
        if hasattr(security, "check_rate_limit"):
            if not security.check_rate_limit(req.agent_name):
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
        elif hasattr(security, "is_allowed"):
            if not security.is_allowed(req.agent_name):
                raise HTTPException(status_code=429, detail="Rate limit exceeded")

        system_prompt = f"You are {req.agent_name}, an autonomous AI specialist in ZANKENE."
        response = llm.generate_agent_response(system_prompt, req.prompt)

        # Log task to DB
        db.log_task(req.task_id, f"API Task: {req.task_name} ({req.agent_name})", "COMPLETED")
        
        # Save output to memory vault
        vault.save_agent_memory(req.agent_name, f"last_task_{req.task_id}", response)

        return {
            "status": "SUCCESS",
            "task_id": req.task_id,
            "agent_name": req.agent_name,
            "response": response
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        db.log_task(req.task_id, f"API Task: {req.task_name}", "FAILED")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/pipeline")
def dispatch_pipeline_chain(req: PipelineChainReq):
    try:
        result = pipeline.run_chain(initial_input=req.campaign_goal, agent_chain=req.chain)
        return {
            "status": "SUCCESS",
            "campaign_goal": req.campaign_goal,
            "final_output": result["final_output"],
            "history": result["history"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))