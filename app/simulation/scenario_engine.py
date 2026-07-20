class ScenarioEngine:
    def run(self, scenario, metadata=None):
        return {"scenario": scenario, "metadata": metadata or {}, "result": "completed"}
