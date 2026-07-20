def test_xai_engine_module_exists():
    import os
    assert os.path.exists("app/analytics/xai_engine.py")
