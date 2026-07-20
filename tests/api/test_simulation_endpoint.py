from app.api.v1.endpoints.simulation import run_simulation

def test_simulation_endpoint():
    result = run_simulation("test")
    assert result["scenario"] == "test"
