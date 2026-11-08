import asyncio
import os
import sqlite3
import time
from pathlib import Path
import main
from main import (
    init_state_db,
    run_self_healing_diagnostics,
)

def test_self_healing_nominal(tmp_path):
    test_db = tmp_path / "test_heal_state.db"
    orig_path = main.STATE_DB_PATH
    main.STATE_DB_PATH = test_db
    try:
        init_state_db()
        report = asyncio.run(run_self_healing_diagnostics(auto_repair=True))
        assert report["ok"] is True
        assert report["healthy"] is True
        assert report["db_integrity"] == "ok"
        assert report["code_integrity"]["main.py"] == "valid_syntax"
        assert report["code_integrity"]["worker.py"] == "valid_syntax"
    finally:
        main.STATE_DB_PATH = orig_path

def test_self_healing_zombie_cleanup(tmp_path):
    test_db = tmp_path / "test_heal_state.db"
    orig_path = main.STATE_DB_PATH
    main.STATE_DB_PATH = test_db
    try:
        init_state_db()
        with sqlite3.connect(test_db) as conn:
            conn.execute(
                "INSERT INTO background_jobs (id, job_name, script_path, pid, status, started_at) VALUES (?, ?, ?, ?, ?, ?)",
                ("job-zombie-1", "fake_worker", "dummy.py", 999998, "RUNNING", "2026-11-08T12:00:00")
            )
            conn.commit()

        report = asyncio.run(run_self_healing_diagnostics(auto_repair=True))
        assert report["ok"] is True
        assert report["zombies_cleaned"] >= 1
        assert any("fake_worker" in act or "dead background job" in act for act in report["actions_taken"])

        with sqlite3.connect(test_db) as conn:
            status = conn.execute("SELECT status FROM background_jobs WHERE id = 'job-zombie-1'").fetchone()[0]
            assert status == "STOPPED"
    finally:
        main.STATE_DB_PATH = orig_path

def test_self_healing_contamination_purge(tmp_path):
    test_db = tmp_path / "test_heal_state.db"
    orig_path = main.STATE_DB_PATH
    main.STATE_DB_PATH = test_db
    try:
        init_state_db()
        today = "2026-11-08"
        with sqlite3.connect(test_db) as conn:
            conn.execute(
                "INSERT INTO task_log (id, date, tier, task_type, amount_usd, summary, execution_result, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                ("contam-1", today, "micro", "regex_test", 25.0, "Extracted email patterns", "dev@example.com", "2026-11-08T15:00:00")
            )
            conn.execute(
                "INSERT OR REPLACE INTO daily_state (date, target_usd, current_usd, micro_usd, freelance_usd, micro_tasks_count, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (today, 500.0, 25.0, 25.0, 0.0, 1, "2026-11-08T15:00:00")
            )
            conn.commit()

        report = asyncio.run(run_self_healing_diagnostics(auto_repair=True))
        assert report["ok"] is True
        assert any("Purged" in act and "test-polluted" in act for act in report["actions_taken"])

        with sqlite3.connect(test_db) as conn:
            cnt = conn.execute("SELECT COUNT(*) FROM task_log WHERE id = 'contam-1'").fetchone()[0]
            assert cnt == 0
            cur_usd = conn.execute("SELECT current_usd FROM daily_state WHERE date = ?", (today,)).fetchone()[0]
            assert cur_usd == 0.0
    finally:
        main.STATE_DB_PATH = orig_path

def test_self_healing_lockout_flush():
    main._lockout_until = time.time() - 5.0
    main._failed_attempts = 5

    report = asyncio.run(run_self_healing_diagnostics(auto_repair=True))
    assert report["ok"] is True
    assert report["lockout_recovered"] is True
    assert main._lockout_until == 0.0
    assert main._failed_attempts == 0
