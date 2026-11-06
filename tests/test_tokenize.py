import asyncio
from main import tokenize, get_writing_style, PROFILE_MERGED, craft_brilliant_prompt

def test_tokenize_removes_common_stopwords():
    result = tokenize("Accha toh laptop compare karo performance aur battery")
    assert "laptop" in result
    assert "performance" in result
    assert "battery" in result
    assert "toh" not in result
    assert "aur" not in result

def test_tokenize_handles_hinglish_and_devanagari():
    result = tokenize("Maja nahi aya बहुत अच्छा")
    assert "maja" in result
    assert "aya" in result
    assert "बहुत" in result
    assert "अच्छा" in result

def test_profile_merged_content():
    assert PROFILE_MERGED["identity"]["name"] == "Ved Chaos"
    assert PROFILE_MERGED["communication_rules"]["phonetic_spelling_rules"]["woh"] == "bo"
    assert PROFILE_MERGED["communication_rules"]["phonetic_spelling_rules"]["maine"] == "mene"

def test_craft_brilliant_prompt():
    res = asyncio.run(craft_brilliant_prompt("Build an asynchronous Python scraper", domain="coding"))
    assert res["ok"] is True
    assert "Principal Software Architect" in res["prompt"]
    assert "CRITICAL NEGATIVE CONSTRAINTS" in res["prompt"]

    res_art = asyncio.run(craft_brilliant_prompt("Cyberpunk warrior in neon rain", domain="ai_art"))
    assert res_art["ok"] is True
    assert "cinematic composition" in res_art["prompt"]
    assert "Negative Prompt" in res_art["prompt"]

def test_security_pin_access():
    import os
    import main
    expected_pin = os.environ.get("VED_SECURITY_PIN") or "sample_pin_for_test"
    expected_phrase = os.environ.get("VED_ACTIVATION_PHRASE") or "sample_phrase_for_test"
    main.SECURITY_PIN = expected_pin
    main.ACTIVATION_PHRASE = expected_phrase

    from main import verify_security_access, get_system_prompt

    # Valid 2FA: phrase + pin
    auth_ok = asyncio.run(verify_security_access(pin=expected_pin, activation_phrase=expected_phrase))
    assert auth_ok["authenticated"] is True
    assert auth_ok["access_level"] == "OWNER_UNLOCKED"

    # Missing activation phrase (only PIN) -> must fail and stay guest mode
    auth_pin_only = asyncio.run(verify_security_access(pin=expected_pin, activation_phrase=""))
    assert auth_pin_only["authenticated"] is False
    assert auth_pin_only["access_level"] == "GUEST_NORMAL_MODE"

    # Wrong credentials
    auth_bad = asyncio.run(verify_security_access(pin="wrong_pin_9999", activation_phrase="wrong_phrase"))
    assert auth_bad["authenticated"] is False
    assert auth_bad["access_level"] == "GUEST_NORMAL_MODE"

    # Substring attack prevention (hmac.compare_digest exact match)
    auth_substring = asyncio.run(verify_security_access(pin="prefix" + expected_pin + "suffix", activation_phrase=expected_phrase))
    assert auth_substring["authenticated"] is False

    # System prompt owner unlock
    prompt_owner = asyncio.run(get_system_prompt(security_pin=expected_pin, activation_phrase=expected_phrase))
    assert "Ved Chaos" in prompt_owner

    # System prompt guest fallback
    prompt_guest = asyncio.run(get_system_prompt(security_pin=expected_pin, activation_phrase=""))
    assert "helpful, neutral AI assistant" in prompt_guest


