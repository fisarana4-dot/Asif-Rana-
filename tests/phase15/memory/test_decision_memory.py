from app.phase15.memory.decision_memory import DecisionMemory


def test_decision_memory():
    result = DecisionMemory().store("decision")
    assert result["stored"] is True
