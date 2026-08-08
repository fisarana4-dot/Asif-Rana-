from fastapi import FastAPI

app = FastAPI(title="NEXRA V16000 Governance Kernel")

@app.get("/health")
def health():
    return {
        "system":"NEXRA V16000",
      
        "module":"Governance Kernel",
        "status":"active"
    }

from pydantic import BaseModel

class DecisionRequest(BaseModel):
    decision_id:str
    request:str
    risk_category:int
    confidence:float

@app.post("/decision")
def create_decision(data:DecisionRequest):
    return {
        "decision_id":data.decision_id,
        "status":"recorded",
        "risk_category":data.risk_category,
        "confidence":data.confidence
    }
