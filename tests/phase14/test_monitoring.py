from app.phase14.monitoring.system_observer import SystemObserver

def test_monitoring():
    result = SystemObserver().check()
    assert result["status"] == "healthy"
