---
name: os-operator
description: Autonomous Windows system automation, PowerShell terminal command execution, active window telemetry, desktop screen vision, system health metrics, background job daemons, workspace file control, and browser automation.
---

# Autonomous OS Operator & Desktop Vision Skill

This skill equips the agent with authorized, defensive operating system automation, screen vision capture, system telemetry, file workspace control, background daemon management, and terminal control on Windows workstations.

## 1. Operating Principles & Safety Mandates
- **Sandboxed & Guarded:** Destructive commands (`format`, `diskpart`, recursive `del /s /q c:\`, root partition tampering) are strictly intercepted and blocked by the safety gate.
- **System Integrity:** Critical Windows system paths (`C:\Windows`, `System32`, `C:\Program Files`, `.git` internal structures) are protected from unauthorized writes or deletions.
- **Threat Shield Integrated:** All browser automation tasks run pre-flight URL safety analysis via `inspect_url_safety` to intercept phishing, typosquatting, and malicious executables before network transit.
- **Vision-Driven Execution:** Captures desktop snapshots to inspect open windows, active UI elements, and dialog prompts without blind execution.
- **Telemetry Transparency:** Emits exact return codes, execution time, and stdout/stderr outputs for every command executed.

## 2. Core OS Operator Tools
1. **`execute_system_command`**: Runs PowerShell / CMD commands with custom timeouts and destructive operation filters.
2. **`capture_screen_snapshot`**: Takes instantaneous primary monitor screenshots, saving to local PNG for multimodal AI inspection with headless fallbacks.
3. **`get_active_window_info`**: Inspects the foreground application title, window handle, and pixel coordinates.
4. **`inspect_system_telemetry`**: Retrieves real-time CPU %, logical/physical cores, RAM (total/used/free), disk storage metrics, and top processes by memory and CPU.
5. **`manage_background_job`**: Spawns detached background processes (e.g. `worker.py`), monitors live status via PID verification, lists active jobs, and gracefully terminates them with SQLite persistence.
6. **`manage_file_workspace`**: Safely lists directories, reads file contents, writes files, searches files via glob patterns, and removes single temporary files with path protection.
7. **`automate_browser_task`**: Performs automated web inspection, meta tag discovery, and structured text extraction with pre-flight Threat Shield verification.

## 3. Recommended Workflow
1. **Telemetry & Environment Check**: Inspect CPU/RAM headroom with `inspect_system_telemetry`.
2. **Pre-flight Inspection**: Check current active window via `get_active_window_info`.
3. **Visual Verification**: Take a screen snapshot via `capture_screen_snapshot` if UI state needs to be confirmed.
4. **Job & Task Execution**: Start long-running background workers with `manage_background_job` or execute commands with `execute_system_command`.
5. **Workspace Management**: Read/write code and project artifacts safely using `manage_file_workspace`.
6. **Post-execution Telemetry**: Verify output returncode and error output before continuing.
