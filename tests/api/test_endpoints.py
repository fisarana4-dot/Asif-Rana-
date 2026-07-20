from app.api.v1.endpoints.decision import simulate_decision

def test_decision_api():
    result = simulate_decision("test")
