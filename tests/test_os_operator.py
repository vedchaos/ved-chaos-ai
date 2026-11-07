import asyncio
from main import (
    execute_system_command,
    get_active_window_info,
    capture_screen_snapshot,
)

def test_execute_system_command_safe_execution():
    # Run safe calculation in PowerShell
    res = asyncio.run(execute_system_command("Write-Output (100 + 45)"))
    assert res["ok"] is True
    assert res["exit_code"] == 0
    assert "145" in res["stdout"]
    assert res["elapsed_seconds"] >= 0

def test_execute_system_command_blocks_destructive_operations():
    # Attempt dangerous format command
    res_format = asyncio.run(execute_system_command("format C: /q"))
    assert res_format["ok"] is False
    assert res_format.get("blocked_by_safety_policy") is True
    assert "destructive" in res_format["error"].lower()

    # Attempt dangerous diskpart command
    res_diskpart = asyncio.run(execute_system_command("diskpart /s script.txt"))
    assert res_diskpart["ok"] is False
    assert res_diskpart.get("blocked_by_safety_policy") is True

def test_get_active_window_info_structure():
    res = asyncio.run(get_active_window_info())
    assert res["ok"] is True
    assert "window_title" in res
    assert "bounds" in res
    assert "left" in res["bounds"]
    assert "top" in res["bounds"]

def test_capture_screen_snapshot_fallback():
    res = asyncio.run(capture_screen_snapshot())
    assert res["ok"] is True
    assert "resolution" in res
    assert "width" in res
    assert "height" in res
    assert res["width"] > 0
    assert res["height"] > 0

