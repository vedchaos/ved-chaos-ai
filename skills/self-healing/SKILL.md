---
name: self-healing
description: Autonomous system diagnostic and self-healing engine, repairing SQLite state corruption, purging test contamination, cleaning zombie processes, auto-recovering auth lockouts, verifying code AST syntax integrity, killing port collisions, garbage collecting old screenshots, and supervising crash resurrection.
---

# Autonomous Self-Healing & System Auto-Repair Skill

Equips the agent, FastMCP server, and background runner daemon with autonomous diagnostic and auto-repair capabilities to maintain continuous 24/7 reliability across SQLite persistence, port bindings, background daemons, auth gates, disk bloat, and core script AST syntax.

## 1. Core Self-Healing Capabilities
1. **SQLite Database & Schema Integrity (`PRAGMA integrity_check`)**: Detects corrupt database headers or missing schema tables, automatically re-initializing missing persistence structures.
2. **Test Contamination Purge**: Automatically detects and flushes test runner mock data that leaks into production task logs (e.g. from local pytest runs), recalculating accurate revenue metrics.
3. **Zombie Background Process Termination**: Scans active job logs against OS PID registries (`psutil.pid_exists`), auto-marking orphaned or dead process entries as `STOPPED`.
4. **Authentication Lockout Auto-Recovery**: Reconciles sliding window lockout timers, auto-evicting expired lockout locks and resetting failed attempt counters so operators never get permanently locked out.
5. **Python AST Code Integrity**: Validates the abstract syntax tree of core server scripts (`main.py`, `worker.py`) to intercept syntax errors before execution.
6. **Port Conflict & Zombie Server Killer**: Probes target server port (e.g. 8000), detects stale occupying processes using OS socket inspection and PID lookup, and terminates blocking processes to prevent `EADDRINUSE` errors.
7. **Temp Artifact & Screenshot Garbage Collection**: Cleans expired desktop screenshots (`screenshot_*.png`), temporary cache, and `.tmp` files older than retention hours (default 24h), freeing disk space.
8. **Cloud Memory Circuit Breaker**: Evaluates `DATABASE_URL` connectivity and placeholder states (`USER:PASSWORD@HOST`), automatically engaging offline local SQLite mode without crashing queries.
9. **Git Working Tree Conflict Marker Audit**: Scans code files for unmerged `<<<<<<< HEAD` merge conflict markers.
10. **Telemetry & Memory Exhaustion Safeguards**: Checks virtual memory pressures, raising proactive warnings if system RAM usage exceeds 95%.

## 2. Daemon Crash Resurrection Supervisor
The `worker.py` daemon is equipped with an autonomous supervisor loop:
- Catches unhandled runtime exceptions and network drops.
- Applies exponential backoff (`3s`, `6s`, `12s`...) up to 10 retry attempts.
- Triggers `run_self_healing_diagnostics(auto_repair=True)` during crash recovery to resolve underlying state anomalies before resurrection.

## 3. Self-Healing Tool
- **`run_self_healing_diagnostics(auto_repair=True, target_port=8000, artifact_retention_hours=24)`**: Executes the full diagnostic inspection suite and applies automated fixes.
