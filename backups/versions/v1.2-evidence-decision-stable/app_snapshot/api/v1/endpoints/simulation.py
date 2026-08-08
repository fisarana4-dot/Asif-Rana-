from app.simulation.scenario_engine import ScenarioEngine

def run_simulation(scenario):
    engine = ScenarioEngine()
    return engine.run(scenario)
