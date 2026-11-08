---
name: self-healing
description: Autonomous system diagnostic and self-healing engine, repairing SQLite state corruption, purging test contamination, cleaning zombie processes, auto-recovering auth lockouts, and verifying code AST syntax integrity.
---

# Autonomous Self-Healing & System Auto-Repair Skill

Equips the agent and background runner daemon with autonomous diagnostic and auto-repair capabilities to maintain continuous 24/7 reliability across SQLite persistence, background daemons, auth gates, and core script AST syntax.

## 1. Core Self-Healing Capabilities
1. **SQLite Database & Schema Integrity (`PRAGMA integrity_check`)**: Detects corrupt database headers or missing schema tables, automatically re-initializing missing persistence structures.
2. **Test Contamination Purge**: Automatically detects and flushes test runner mock data that leaks into production task logs (e.g. from local pytest runs), recalculating accurate revenue metrics.
3. **Zombie Background Process Termination**: Scans active job logs against OS PID registries (`psutil.pid_exists`), auto-marking orphaned or dead process entries as `STOPPED`.
4. **Authentication Lockout Auto-Recovery**: Reconciles sliding window lockout timers, auto-evicting expired lockout locks and resetting failed attempt counters so operators never get permanently locked out.
5. **Python AST Code Integrity**: Validates the abstract syntax tree of core server scripts (`main.py`, `worker.py`) to intercept syntax errors before execution.
6. **Telemetry & Memory Exhaustion Safeguards**: Checks virtual memory pressures, raising proactive warnings if system RAM usage exceeds 95%.

## 2. Self-Healing Tool
- **`run_self_healing_diagnostics(auto_repair=True)`**: Executes the full diagnostic inspection suite and applies automated fixes.

## 3. Background Runner Watchdog
The `worker.py` daemon runs a self-healing health check on every cycle, logging resolved anomalies automatically without human intervention.
