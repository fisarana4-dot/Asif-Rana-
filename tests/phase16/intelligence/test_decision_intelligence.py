from app.phase16.intelligence.decision_intelligence import DecisionIntelligence


def test_decision_intelligence():
    result = DecisionIntelligence().analyze("decision")
    assert result["decision"] == "decision"
    assert result["intelligence"] == "evaluated"
