import os
import sys
import tempfile
import pytest
from pathlib import Path
from main import (
    inspect_system_telemetry,
    manage_background_job,
    manage_file_workspace,
    automate_browser_task,
)

@pytest.mark.anyio
async def test_inspect_system_telemetry():
    res = await inspect_system_telemetry()
    assert res["ok"] is True
    assert "cpu" in res
    assert res["cpu"]["logical_cores"] >= 1
    assert 0.0 <= res["cpu"]["usage_percent"] <= 100.0
    assert "memory" in res
    assert res["memory"]["total_gb"] > 0
    assert 0.0 <= res["memory"]["usage_percent"] <= 100.0
    assert "disk" in res
    assert res["disk"]["total_gb"] > 0
    assert "top_processes_by_memory" in res
    assert isinstance(res["top_processes_by_memory"], list)

@pytest.mark.anyio
async def test_manage_file_workspace_lifecycle_and_safety():
    with tempfile.TemporaryDirectory() as tmp_dir:
        test_file = Path(tmp_dir) / "test_artifact.txt"
        
        # 1. Write text
        write_res = await manage_file_workspace("write_text", str(test_file), content="Hello Autonomous World")
        assert write_res["ok"] is True
        assert test_file.exists()

        # 2. Read text
        read_res = await manage_file_workspace("read_text", str(test_file))
        assert read_res["ok"] is True
        assert "Hello Autonomous World" in read_res["content"]

        # 3. List dir
        list_res = await manage_file_workspace("list_dir", tmp_dir)
        assert list_res["ok"] is True
        assert list_res["items_count"] == 1
        assert list_res["items"][0]["name"] == "test_artifact.txt"

        # 4. Search files
        search_res = await manage_file_workspace("search_files", tmp_dir, query="*.txt")
        assert search_res["ok"] is True
        assert search_res["matches_count"] == 1

        # 5. Delete file
        del_res = await manage_file_workspace("delete_file", str(test_file))
        assert del_res["ok"] is True
        assert not test_file.exists()

        # 6. Safety Guardrail: Block write to system protected root
        system_path = "C:\\Windows\\System32\\test_exploit.txt"
        blocked_res = await manage_file_workspace("write_text", system_path, content="exploit")
        assert blocked_res["ok"] is False
        assert blocked_res.get("blocked_by_safety_policy") is True

@pytest.mark.anyio
async def test_manage_background_job_lifecycle():
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write("import time\ntime.sleep(20)\n")
        f.flush()
        dummy_script = f.name

    try:
        job_name = f"test_worker_{int(tempfile.tempdir is not None)}"
        
        # Start
        start_res = await manage_background_job("start", job_name, script_path=dummy_script)
        assert start_res["ok"] is True
        assert start_res["status"] == "RUNNING"
        pid = start_res["pid"]
        assert pid > 0

        # Status
        status_res = await manage_background_job("status", job_name)
        assert status_res["ok"] is True
        assert status_res["job"]["is_alive"] is True

        # List
        list_res = await manage_background_job("list", "")
        assert list_res["ok"] is True
        matched = [j for j in list_res["jobs"] if j["job_name"] == job_name]
        assert len(matched) >= 1

        # Stop
        stop_res = await manage_background_job("stop", job_name)
        assert stop_res["ok"] is True

        # Verify stopped
        status_after = await manage_background_job("status", job_name)
        assert status_after["ok"] is True
        assert status_after["job"]["status"] == "STOPPED"
    finally:
        if os.path.exists(dummy_script):
            os.remove(dummy_script)

@pytest.mark.anyio
async def test_automate_browser_task_threat_shield_intercept():
    # Threat check: Phishing domain with brand typosquatting
    phishing_url = "http://paypa1-update-auth.com/login"
    res = await automate_browser_task(phishing_url)
    assert res["ok"] is False
    assert res.get("blocked_by_threat_shield") is True
    assert "blocked by Threat Shield" in res["error"]

@pytest.mark.anyio
async def test_automate_browser_task_safe_fetch_headers():
    res = await automate_browser_task("https://example.com", action="inspect_headers")
    assert res["ok"] is True
    assert res["status_code"] in (200, 301, 302)
    assert "headers" in res

