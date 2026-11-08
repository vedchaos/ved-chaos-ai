import asyncio
import os
import sqlite3
from pathlib import Path
import main
from main import (
    init_state_db,
    set_daily_earning_target,
    get_earning_dashboard,
    process_micro_task,
    log_freelance_earning,
)

def test_sqlite_state_persistence_and_micro_tasks(tmp_path):
    test_db = tmp_path / "test_state.db"
    orig_path = main.STATE_DB_PATH
    main.STATE_DB_PATH = test_db
    try:
        # Ensure state db is initialized
        init_state_db()
        assert test_db.exists()

        # 1. Update target
        target_res = asyncio.run(set_daily_earning_target(650.0))
        assert target_res["ok"] is True
        assert target_res["daily_target_usd"] == 650.0

        # 2. Execute real regex micro-task
        regex_payload = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b|||Contact us at dev@example.com or support@ved.dev"
        task_res = asyncio.run(process_micro_task(
            task_type="regex_test",
            amount_usd=25.0,
            summary="Extracted email patterns from text",
            task_payload=regex_payload,
        ))
        assert task_res["ok"] is True
        assert task_res["execution_result"]["status"] == "success"
        assert task_res["execution_result"]["matches_found"] == 2
        assert "dev@example.com" in task_res["execution_result"]["matches"]
        assert task_res["persisted"] is True

        # 3. Execute real JSON validation micro-task
        json_payload = '{"service": "fastmcp", "port": 8000, "status": "active"}'
        json_res = asyncio.run(process_micro_task(
            task_type="json_validate",
            amount_usd=15.0,
            summary="Validated config JSON",
            task_payload=json_payload,
        ))
        assert json_res["ok"] is True
        assert json_res["execution_result"]["status"] == "valid_json"
        assert json_res["execution_result"]["keys_count"] == 3

        # 4. Log contract milestone
        freelance_res = asyncio.run(log_freelance_earning(
            amount_usd=200.0,
            client_or_platform="RemoteOK Client",
            job_description="Deployed async FastAPI data ingestion pipeline",
        ))
        assert freelance_res["ok"] is True
        assert freelance_res["added_amount_usd"] == 200.0
        assert freelance_res["persisted"] is True

        # 5. Verify SQLite persistence via dashboard
        dash = asyncio.run(get_earning_dashboard())
        assert dash["daily_target_usd"] == 650.0
        assert dash["current_earnings_usd"] >= 240.0
        assert len(dash["completed_jobs"]) >= 3
    finally:
        main.STATE_DB_PATH = orig_path
