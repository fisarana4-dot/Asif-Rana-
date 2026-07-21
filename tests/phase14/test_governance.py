from app.phase14.governance.decision_governance import DecisionGovernance

def test_decision():
    engine = DecisionGovernance()
    result = engine.validate("D001", 0.90)
    assert result.approved
