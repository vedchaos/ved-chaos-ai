import asyncio
import math
import main
from main import hybrid_search_memory, search_chat_history, save_chat_example, delete_chat_example

def test_memory_authentication_guard():
    # Configure 2FA in main
    main.SECURITY_PIN = "secret_pin"
    main.ACTIVATION_PHRASE = "secret phrase"
    main._failed_attempts = 0
    main._lockout_until = 0.0

    # Unauthenticated call to search_chat_history
    res = asyncio.run(search_chat_history(query="fastapi", limit=5, security_pin="wrong", activation_phrase="wrong"))
    assert len(res) == 1
    assert "error" in res[0]
    assert "Unauthorized" in res[0]["error"]

    # Unauthenticated call to save_chat_example
    save_res = asyncio.run(save_chat_example(role="user", content="sample text", security_pin="wrong"))
    assert save_res["ok"] is False
    assert "Unauthorized" in save_res["error"]

    # Unauthenticated call to delete_chat_example
    del_res = asyncio.run(delete_chat_example(example_id="123e4567-e89b-12d3-a456-426614174000", security_pin="wrong"))
    assert del_res["ok"] is False
    assert "Unauthorized" in del_res["error"]

def test_hybrid_vector_dimension_validation():
    # Pass 2FA
    main.SECURITY_PIN = "secret_pin"
    main.ACTIVATION_PHRASE = "secret phrase"
    main._failed_attempts = 0
    main._lockout_until = 0.0

    # 1. Non-list vector
    res_non_list = asyncio.run(hybrid_search_memory(
        query="test",
        embedding="not_a_list",  # type: ignore
        security_pin="secret_pin",
        activation_phrase="secret phrase",
    ))
    assert len(res_non_list) == 1
    assert "Invalid embedding: must be a list of floats" in res_non_list[0]["error"]

    # 2. Vector with wrong dimension (e.g. 512 instead of 1536)
    short_vec = [0.1] * 512
    res_dim = asyncio.run(hybrid_search_memory(
        query="test",
        embedding=short_vec,
        security_pin="secret_pin",
        activation_phrase="secret phrase",
    ))
    assert len(res_dim) == 1
    assert "Invalid embedding dimension: expected 1536, got 512" in res_dim[0]["error"]

    # 3. Vector containing NaN or Inf
    nan_vec = [0.1] * 1536
    nan_vec[42] = float("nan")
    res_nan = asyncio.run(hybrid_search_memory(
        query="test",
        embedding=nan_vec,
        security_pin="secret_pin",
        activation_phrase="secret phrase",
    ))
    assert len(res_nan) == 1
    assert "Invalid vector value at index 42" in res_nan[0]["error"]
