from app.decision.evidence.evidence_engine import evidence_engine
class DecisionEngine:
    def evaluate(self,data):
        evidence=evidence_engine.analyze(data)
        return {'decision':'ANALYZE','evidence':evidence,'input':data}
decision_engine=DecisionEngine()
