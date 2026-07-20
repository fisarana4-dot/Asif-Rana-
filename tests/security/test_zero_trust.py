def test_zero_trust_module_exists():
    import os
    assert os.path.exists("app/security/zero_trust.py")
