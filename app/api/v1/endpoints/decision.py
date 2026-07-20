from app.simulation.decision_twin import DecisionTwin

def simulate_decision(scenario):
    twin = DecisionTwin()
    return twin.simulate(scenario)
