from app.decision.evidence.evidence_score import score_engine
class EvidenceEngine:
    def analyze(self,data):
        score=score_engine.calculate(30,30,20,20)
        return {'decision':data,'confidence':score['confidence'],'evidence':['Market','Buyer','Product','Memory']}
evidence_engine=EvidenceEngine()
