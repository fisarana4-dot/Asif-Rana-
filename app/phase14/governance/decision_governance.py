from dataclasses import dataclass

@dataclass
class DecisionRecord:
    decision_id: str
    approved: bool


class DecisionGovernance:

    def validate(self, decision_id, confidence):
        return DecisionRecord(decision_id, confidence >= 0.80)
