<div align="center">

# ⚡ VED CHAOS AI ⚡
### Stateful FastMCP Developer Suite, Hybrid Memory & Engineering Intelligence

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00F0FF&center=true&vCenter=true&width=750&lines=VED+CHAOS+AI+%E2%80%94+STATEFUL+FASTMCP+ECOSYSTEM;PERSISTENT+POSTGRESQL+%2B+SQLITE+FTS5+MEMORY;OFFLINE-FIRST+HYBRID+RECALL+%7C+ZERO-PASSWORD+OPEN+ACCESS;LIVE+TECH+FEEDS+%7C+REMOTEOK+%2B+HACKER+NEWS;DEFENSIVE+PENTESTING+%7C+AST+VULNERABILITY+AUDIT;AUTONOMOUS+SELF-HEALING+%7C+CODEBASE+INGESTOR)](https://git.io/typing-svg)

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-FastMCP%20%7C%20Agentic-00F0FF?style=for-the-badge&logo=fastapi&logoColor=black" alt="FastMCP" />
  <img src="https://img.shields.io/badge/Version-v0.4.0-00E5FF?style=for-the-badge&logo=semver&logoColor=black" alt="Version" />
  <img src="https://img.shields.io/badge/Memory-PostgreSQL%20%2B%20SQLite%20FTS5-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Security-AST%20Auditing%20%2B%20Threat%20Shield-FF0055?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="Security" />
  <img src="https://img.shields.io/badge/Tests-43%20Passed%20(100%25)-00FF66?style=for-the-badge&logo=pytest&logoColor=black" alt="Tests" />
  <img src="https://img.shields.io/badge/Python-3.11%2B-FFE873?style=for-the-badge&logo=python&logoColor=black" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-999999?style=for-the-badge" alt="License" />
</p>

[![M8ven Score](https://m8ven.ai/badge/mcp/vedchaos-ved-chaos-ai-7ut3zs?v=de429bf8dd623c497bc56f27125dfc17)](https://m8ven.ai/mcp/vedchaos-ved-chaos-ai-7ut3zs?s=readme)

---

**A stateful, production-hardened FastMCP developer suite built for autonomous AI agents (Antigravity IDE, Claude Desktop, Cursor, Windsurf).**  
Equips your AI agent with **zero-friction open owner access**, **offline-first hybrid memory (Cloud PostgreSQL + Local SQLite FTS5 vector similarity)**, **codebase ingestion & AST security**, **live hiring scrapers (RemoteOK & Hacker News)**, **autonomous OS & desktop vision control**, **self-healing auto-repair**, and **quantitative trading**.

</div>

---

## 📖 About Ved Chaos AI

### 💡 The Vision & Architecture
Most standard AI assistant tools are stateless, passive, and disconnected from the host machine—they forget context across chat sessions, return mock responses, lack vision awareness, and cannot safely interact with the local operating system.

**Ved Chaos AI** solves cognitive continuity, safe local automation, and developer execution through a modular, hardened FastMCP server:

* 🧠 **Offline-First Hybrid Persistence**: 
  - **Cloud PostgreSQL (`asyncpg`)**: Long-term conversational memory with native full-text search (FTS GIN indexing) and 1536-dimensional pgvector cosine retrieval.
  - **Local SQLite (`state.db`) with FTS5 BM25**: Seamless offline fallback when `DATABASE_URL` is unset, supporting keyword search, vector similarity, daily revenue targets, executed micro-tasks, and historical work logs.
* 🔓 **Zero-Friction Open Owner Access (Optional 2FA Gate)**: By default, developer tools, custom personas, and memory operations are unlocked without requiring passwords. For public or shared environments, an optional rate-limited constant-time HMAC 2FA gate locks out after 5 consecutive failures for 300 seconds.
* 📦 **Ved Chaos Codebase & Supply-Chain Intelligence (v0.4.0)**:
  - **Codebase Ingestor (`ved_ingest_codebase`)**: Packs local directory trees or remote GitHub repositories into LLM-ready digests with token estimators and Shannon-entropy secret redaction.
  - **Supply-Chain Shield (`ved_scan_supply_chain`)**: Real-time dependency manifest auditing via the live OSV.dev vulnerability database.
  - **Durable Reasoning Chains (`ved_manage_reasoning_chain`)**: Sequential thinking and hypothesis branching persisted to SQLite.
  - **GitHub Radar (`ved_scout_github_upgrades`)**: Discovers trending open-source tools with permissive license scoring.
* 🖥️ **Autonomous OS Operator & Desktop Vision**: Instantaneous desktop screenshot capture (`Pillow`/`MSS`) for Vision AI models, active foreground window telemetry, and sandboxed PowerShell command execution with destructive command guards.
* 🛡️ **Defensive Threat & Malware / Phishing Link Shield**: Pre-flight URL safety inspection, typosquatting & leetspeak detection (`paypa1`), executable double-extension detection (`invoice.pdf.exe`), and binary masquerading defense (`MZ` header checks).
* 🔧 **Autonomous Self-Healing Diagnostics**: One-click health check detecting database corruption, zombie worker processes, port conflicts, and test suite state contamination.
* 💼 **Live Developer Hiring & Bounty Discovery**: Queries live RemoteOK API and Hacker News job feeds in real time for direct founder and freelance contracts with zero platform cuts, backed by verified curated fallbacks.
* ⚔️ **Static AST Code Auditing**: Real Python AST syntax tree parsing detecting SQL injection via f-strings in database execution calls, shell injection via `os.system` or `subprocess(shell=True)`, `pickle` deserialization, and `eval`/`exec`.
* 📈 **Quant Paper Trading Suite**: Algorithmic technical indicators (SMA crossovers, RSI 14 momentum) with mathematical 1% equity risk sizing and a virtual paper portfolio.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User["Client Interface<br/>(Antigravity / Claude / Cursor / Windsurf)"]
    Gate{"Persona Access Gate<br/>Open by Default | Optional Constant-Time 2FA"}
    
    User -->|Queries & Commands| Gate
    
    Gate -->|Direct Access / Valid 2FA| CoreEngine["VED CHAOS CORE ENGINE<br/>FastMCP Server (main.py)"]
    Gate -->|Explicitly Locked / Invalid 2FA| GuestMode["Guest Mode<br/>Standard Assistant, Private Memory Locked"]
    
    subgraph "Core Agentic Tooling"
        CoreEngine --> Memory["Hybrid Memory Layer<br/>(PostgreSQL pgvector / SQLite FTS5)"]
        CoreEngine --> Codebase["Codebase & Intelligence<br/>(Repo Ingestion, OSV Scanner, Thought Chains)"]
        CoreEngine --> OSOperator["OS Operator & Desktop Vision<br/>(Screenshots, Window Info, PowerShell)"]
        CoreEngine --> ThreatGuard["Threat & Malware Shield<br/>(URL Phishing, Double-Ext, MZ Header)"]
        CoreEngine --> Security["AST Security Suite<br/>(CWE-89, CWE-78, CWE-95, OWASP Top 10)"]
        CoreEngine --> Healing["Self-Healing Diagnostics<br/>(DB Repair, Zombie GC, Port Killer)"]
        CoreEngine --> Freelance["Freelance & Hiring Feeds<br/>(RemoteOK, Hacker News, Scope Defender)"]
        CoreEngine --> Trading["Quantitative Paper Suite<br/>(SMA, RSI 14, 1% Risk Sizer, Virtual Book)"]
    end

    subgraph "Persistence & Background Daemon"
        Freelance --> Worker["Background Daemon<br/>(worker.py - Windows / Termux / Linux)"]
        Freelance --> LocalDB[(Local SQLite<br/>state.db)]
        Memory --> CloudDB[(Cloud PostgreSQL<br/>Supabase / Neon)]
    end
```

---

## 🔥 Key Pillars & Capabilities

### 🧠 1. Offline-First Hybrid Persistence & Memory Layer
* **PostgreSQL GIN Full-Text Search**: Native PostgreSQL GIN indexes on `to_tsvector('simple', content)` for high-velocity query recall across stored interactions.
* **SQLite FTS5 Local Vector Fallback**: Zero-configuration local database storing conversations, embeddings, and task history with sub-millisecond retrieval.
* **Vector Input Validation**: Strict validation for pgvector inputs ensuring exact 1536-dimensional embeddings and finite numerical values (rejecting `NaN` / `Inf`).
* **SQLite Daily State Persistence**: Tracks daily targets, executed micro-tasks (regex validation, JSON linting, syntax analysis), and freelance revenue in local `state.db`.

---

### 🔓 2. Zero-Password Open Access & Optional Hardened Gate
* **Password-Free by Default**: Directly access Ved's custom developer profile, writing style, system prompt, and memories without entering PINs or secret phrases.
* **Optional Bi-Factor Gate**: When `VED_SECURITY_PIN` and `VED_ACTIVATION_PHRASE` are set in `.env`, the server enables constant-time HMAC authentication with a sliding-window lockout counter (locks out after 5 consecutive failures for 300 seconds).

---

### 📦 3. Codebase Intelligence & Supply-Chain Shield
* **Codebase Digest Ingestion (`ved_ingest_codebase`)**: Traverses workspaces or GitHub repositories, respects `.gitignore`, redacts detected API secrets, and outputs structured, token-budgeted markdown digests.
* **OSV Supply-Chain Auditing (`ved_scan_supply_chain`)**: Parses dependencies (`requirements.txt`, `pyproject.toml`, `package.json`) and queries live OSV.dev APIs for known CVEs.
* **Durable Sequential Reasoning (`ved_manage_reasoning_chain`)**: Maintains tree-of-thought steps, revisions, and branching across multi-turn complex tasks.
* **GitHub Radar (`ved_scout_github_upgrades`)**: Discovers relevant GitHub repositories with star tracking and license compatibility ratings.

---

### 🖥️ 4. Autonomous OS Operator & Desktop Vision
* **Vision Screen Capture (`capture_screen_snapshot`)**: Takes instantaneous primary monitor screenshots (Pillow/MSS) with automated fallback for headless environments, allowing multimodal Vision AI models to visually inspect screen coordinates and UI elements.
* **Foreground Window Telemetry (`get_active_window_info`)**: Queries Windows User32 APIs for the active application title, process handle, and bounding rectangle geometry.
* **Sandboxed System Execution (`execute_system_command`)**: Runs PowerShell and CMD commands with configurable timeouts and strict security filters intercepting destructive commands (`format`, `diskpart`, recursive `del /s /q`).
* **Live System Telemetry (`inspect_system_telemetry`)**: Monitors real-time CPU %, core counts, RAM availability/utilization, system disk storage, and top memory/CPU-intensive processes via `psutil`.
* **Detached Daemon Manager (`manage_background_job`)**: Launches, tracks, and stops background worker processes (e.g. `worker.py`) with PID verification and SQLite state persistence.

---

### 🛡️ 5. Defensive Threat & Malware / Phishing Link Shield
* **Pre-Flight URL Inspector (`inspect_url_safety`)**: Computes a dynamic risk score (0–100) evaluating brand typosquatting (including leetspeak visual substitutions like `1->l`, `0->o`), direct IP hosts, dangerous TLDs, and URL shorteners.
* **Malware & Payload Scanner (`inspect_file_threat`)**: Detects double-extension attacks (`.pdf.exe`), standalone executable extensions, and inspects binary headers for Windows Portable Executable (`MZ`) signatures masquerading as non-executable documents.

---

### ⚔️ 6. Static AST Defensive Auditing
* **AST Visitor (`SecurityASTVisitor`)**:
  * 💉 **SQL Injection (CWE-89)**: Detects f-strings and `%`/`+` string concatenation passed into `.execute()`, `.raw()`, and `.fetch()` calls.
  * 💻 **Command Injection (CWE-78)**: Identifies `os.system()`, `os.popen()`, and `subprocess` calls with `shell=True`.
  * 📦 **Insecure Deserialization (CWE-502)**: Flags untrusted `pickle.loads()` usage.
  * 🚨 **Arbitrary Code Execution (CWE-95)**: Flags dangerous `eval()` and `exec()` calls.
* **Regex Secret Defense**: Supplemental scans for exposed OpenAI keys (`sk-`), GitHub tokens (`ghp_`), and hardcoded passwords.

---

### 💼 7. Live Direct Hiring & Bounty Discovery
* **Real Live Feeds**: Connects to the **RemoteOK API** and **Hacker News Job Stories** to surface active engineering and freelance roles in real-time.
* **Keyword & Budget Filtering**: Filters live listings by tech stack (`python`, `fastapi`, `automation`) and minimum payout thresholds.
* **Graceful Degradation**: If network access is offline or rate-limited, safely returns verified curated leads with transparent `is_live=False` telemetry.

---

### 📈 8. Quantitative Paper Trading Suite
* **Algorithmic Technical Indicators**: Computes SMA short/long crossovers, RSI 14 momentum, and support/resistance boundaries via `analyze_trading_technical_setup`.
* **Mathematical Risk Sizing**: Enforces strict 1% equity risk rules and calculates exact position units via `calculate_position_risk_management`.
* **Zero-Risk Virtual Book**: Simulates trade execution and tracks live portfolio balances via `execute_paper_trade`.

---

## 🛠️ Complete MCP Tool Matrix (41 Tools)

| Category | Tool Name | Description | Auth Mode |
|---|---|---|:---:|
| **Security & Gate** | `verify_security_access` | Verifies security credentials; returns `OWNER_UNLOCKED` directly when password is not set | Open / Optional PIN |
| | `get_user_profile` | Returns Ved's developer identity profile (guest fallback if locked) | Open by Default |
| | `get_writing_style` | Returns authentic Hinglish writing guidelines | Open by Default |
| | `get_system_prompt` | Returns core or unhinged developer persona prompt | Open by Default |
| **OS Operator & Vision** | `capture_screen_snapshot` | Instantaneous desktop screenshot capture with vision fallback | Open |
| | `get_active_window_info` | Foreground window title, process ID, and coordinate bounds | Open |
| | `execute_system_command` | Sandboxed PowerShell/terminal execution with destructive command guards | Open |
| | `inspect_system_telemetry` | Real-time CPU, RAM, Disk, and top process telemetry | Open |
| | `manage_background_job` | Start, stop, monitor, and list detached background workers in SQLite | Open |
| | `manage_file_workspace` | Safe file read, write, search, and delete with root protection | Open |
| | `automate_browser_task` | Automated web scraping and header inspection with Threat Shield pre-flight | Open |
| **Threat & Malware Shield** | `inspect_url_safety` | Phishing, typosquatting, and executable trap URL pre-flight analyzer | Open |
| | `inspect_file_threat` | Double extension, PE header masquerading, and SHA-256 fingerprinting | Open |
| **Memory Engine** | `search_chat_history` | PostgreSQL full-text search with SQLite FTS5 fallback | Open by Default |
| | `hybrid_search_memory` | Hybrid FTS + 1536-dim pgvector / cosine similarity | Open by Default |
| | `save_chat_example` | Upsert interaction with SHA-256 deduplication into persistent memory | Open by Default |
| | `delete_chat_example` | Delete stored example by UUID | Open by Default |
| | `analyze_word_frequency` | Vocabulary frequency analysis over stored interactions | Open by Default |
| **Codebase & Intel (v0.4.0)** | `ved_ingest_codebase` | **Codebase Ingestor**: Local & GitHub repo digest packer + secret redaction | Open |
| | `ved_scan_supply_chain` | **Supply-Chain Shield**: Live OSV.dev CVEs + Shannon entropy secrets | Open |
| | `ved_manage_reasoning_chain` | **Thought Chain**: Persistent SQLite sequential reasoning & branching | Open |
| | `ved_scout_github_upgrades` | **GitHub Radar**: Live repo discovery & permissive license fit | Open |
| | `ved_get_capabilities_manifest` | Live version, active memory backend, and tool manifest | Open |
| **Self-Healing** | `run_self_healing_diagnostics` | Autonomous SQLite integrity, zombie cleanup, port killer, AST check & GC | Open |
| **Freelance & Jobs** | `scan_direct_bounties` | **Live RemoteOK & Hacker News** job scraper with fallback | Open |
| | `auto_generate_freelance_proposal` | Generates high-converting client pitches | Open |
| | `defend_scope_and_upsell` | Converts client scope creep into billable milestones | Open |
| | `generate_portfolio_case_study` | Generates production case study markdown | Open |
| | `run_client_delivery_shield` | Pre-handover syntax and secret leak inspection | Open |
| **State & Tasks** | `process_micro_task` | **Executes real tasks** (regex, JSON, AST syntax) & persists to SQLite | Open |
| | `set_daily_earning_target` | Updates daily revenue target in SQLite | Open |
| | `get_earning_dashboard` | Reads persistent daily revenue, completed tasks & mood telemetry | Open |
| | `log_freelance_earning` | Records contract revenue into SQLite state | Open |
| **Code & Pentesting** | `audit_code_vulnerabilities` | **Real Python AST analysis** for SQLi, CWE-78, CWE-95, CWE-502 | Open |
| | `owasp_security_checklist` | Authoritative OWASP Top 10 hardening checklist | Open |
| **Intelligence** | `fetch_latest_intelligence` | **Live Hacker News API** breaking tech feed with offline fallback | Open |
| | `deep_research_dossier` | Dynamic multi-section technical research dossier | Open |
| **Quantitative** | `analyze_trading_technical_setup` | SMA short/long crossovers, RSI 14 momentum, and support/resistance | Open |
| | `calculate_position_risk_management` | Exact position sizing enforcing strict 1% equity risk rule | Open |
| | `execute_paper_trade` | Simulated zero-risk paper portfolio execution | Open |
| | `craft_brilliant_prompt` | Professional prompt engineering for coding and creative synthesis | Open |

---

## 🚀 Quickstart & Installation

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/vedchaos/ved-chaos-ai.git
cd ved-chaos-ai
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Populate your credentials (leave `VED_SECURITY_PIN` blank for open owner access):
```ini
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/postgres  # Optional (SQLite FTS5 used if unset)
VED_USER_ID=ved-local
VED_SECURITY_PIN=                     # Optional (leave blank to disable password)
VED_ACTIVATION_PHRASE=                # Optional (leave blank to disable password)
MAX_SEARCH_RESULTS=10
MAX_TEXT_CHARS=12000
```

### 3. Run Automated Tests
```bash
pytest -v
```
All **43 tests** covering AST security, rate limiting, vector validation, SQLite FTS5 hybrid memory, state persistence, scrapers, OS automation & telemetry, background job management, self-healing, codebase ingestion, supply-chain OSV auditing, reasoning chains, GitHub radar, threat shields, and trading indicators run with **100% pass rate**.

### 4. Run Background Daemon
```bash
# Continuous loop (Windows CMD / Termux / Linux):
python worker.py

# Single diagnostic iteration:
python worker.py --once
```

### 5. Client MCP Configuration
To connect Ved Chaos AI to **Antigravity IDE**, **Claude Desktop**, or **Cursor**, add the following entry to your `mcp_config.json` or `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ved-chaos-ai": {
      "command": "python",
      "args": [
        "path/to/ved-chaos-ai/main.py"
      ],
      "env": {
        "VED_USER_ID": "ved-local",
        "DATABASE_URL": ""
      }
    }
  }
}
```

---

## 🔒 Security & Privacy Notice
* **Zero PII**: This repository contains zero personal identifying information (no real addresses, birthdays, or family details).
* **Network Isolation**: All client credentials and database tokens remain strictly within your local `.env` and are never committed to version control.
* **Optional Lockout Policy**: When configured, in-memory rate limiting rejects brute-force authentication attempts after 5 consecutive failures.

---

### 🛡️ License
Licensed under the [MIT License](LICENSE). Built for autonomous, persistent developer tooling.
