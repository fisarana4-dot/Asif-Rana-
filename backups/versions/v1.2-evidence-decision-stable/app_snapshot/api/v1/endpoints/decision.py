from fastapi import APIRouter
from app.simulation.decision_twin import DecisionTwin

router = APIRouter(prefix="/decision", tags=["decision"])

@router.post("/simulate")
def simulate_decision(scenario: dict):
    twin = DecisionTwin()
    return twin.simulate(scenario)
