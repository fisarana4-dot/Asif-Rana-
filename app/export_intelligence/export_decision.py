from app.decision.decision_engine import decision_engine
class ExportDecision:
    def evaluate(self,data): return decision_engine.evaluate(data)
export_decider=ExportDecision()
