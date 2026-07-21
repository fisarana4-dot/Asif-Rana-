

from app.phase14.autonomy.autonomous_engine import AutonomousEngine

def test_autonomy():
    result = AutonomousEngine().execute("task")
    assert result["status"] == "completed"
