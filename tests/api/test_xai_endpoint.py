from app.api.v1.endpoints.xai import explain_decision

def test_xai_endpoint():
    result = explain_decision("test")
    assert result["decision"] == "test"
