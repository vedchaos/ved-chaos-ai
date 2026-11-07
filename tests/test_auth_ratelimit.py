import asyncio
import time
import main
from main import verify_security_access, check_2fa_authorization

def test_auth_rate_limiting_and_lockout():
    # Setup test credentials
    main.SECURITY_PIN = "test_pin_9876"
    main.ACTIVATION_PHRASE = "test activation phrase"
    main._failed_attempts = 0
    main._lockout_until = 0.0

    # 1. Successful authentication resets failures
    res_ok = asyncio.run(verify_security_access(pin="test_pin_9876", activation_phrase="test activation phrase"))
    assert res_ok["authenticated"] is True
    assert res_ok["access_level"] == "OWNER_UNLOCKED"
    assert res_ok["rate_limited"] is False

    # 2. Simulate 4 failed attempts
    for _ in range(4):
        res_fail = asyncio.run(verify_security_access(pin="wrong_pin", activation_phrase="wrong_phrase"))
        assert res_fail["authenticated"] is False
        assert res_fail["rate_limited"] is False

    assert main._failed_attempts == 4

    # 3. 5th failure triggers lockout
    res_lockout = asyncio.run(verify_security_access(pin="wrong_pin", activation_phrase="wrong_phrase"))
    assert res_lockout["authenticated"] is False
    assert res_lockout["rate_limited"] is True
    assert res_lockout["lockout_remaining_seconds"] > 0
    assert "Too many failed authentication attempts" in res_lockout["message"]

    # 4. While locked out, even valid credentials are rejected
    res_during_lockout = asyncio.run(verify_security_access(pin="test_pin_9876", activation_phrase="test activation phrase"))
    assert res_during_lockout["authenticated"] is False
    assert res_during_lockout["rate_limited"] is True

    # 5. Clean up lockout for subsequent tests
    main._failed_attempts = 0
    main._lockout_until = 0.0

