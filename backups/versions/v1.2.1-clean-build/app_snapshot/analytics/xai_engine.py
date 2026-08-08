class XAIEngine:
    def explain(self, decision, confidence=0.0, evidence=None):
        return {"decision": decision, "confidence": confidence, "evidence": evidence or {}}
