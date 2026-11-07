---
name: os-operator
description: Autonomous Windows system automation, PowerShell terminal command execution, active window telemetry, and screen snapshot capture for vision AI.
---

# Autonomous OS Operator & Desktop Vision Skill

This skill equips the agent with authorized, defensive operating system automation, screen vision capture, and terminal control on Windows workstations.

## 1. Operating Principles & Safety Mandates
- **Sandboxed & Guarded:** Dangerous destructive commands (`format`, `diskpart`, recursive `del /s /q c:\`) are strictly intercepted and blocked by the safety gate.
- **Vision-Driven Execution:** Captures desktop snapshots to inspect open windows, active UI elements, and dialog prompts without blind execution.
- **Telemetry Transparency:** Emits exact return codes, execution time, and stdout/stderr outputs for every command executed.

## 2. Core OS Operator Tools
1. **`execute_system_command`**: Runs PowerShell / CMD commands with custom timeouts and destructive operation filters.
2. **`capture_screen_snapshot`**: Takes instantaneous primary monitor screenshots, saving to local PNG for multimodal AI inspection with headless fallbacks.
3. **`get_active_window_info`**: Inspects the foreground application title, window handle, and pixel coordinates.

## 3. Recommended Workflow
1. **Pre-flight Inspection**: Check current active window via `get_active_window_info`.
2. **Visual Verification**: Take a screen snapshot via `capture_screen_snapshot` if UI state needs to be confirmed.
3. **Command Execution**: Execute required build/test/run commands using `execute_system_command`.
4. **Post-execution Telemetry**: Verify output returncode and error output before continuing.
