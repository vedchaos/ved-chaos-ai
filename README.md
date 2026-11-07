<div align="center">

# ⚡ VED CHAOS AI ⚡
### Stateful FastMCP Developer Suite, Hybrid Memory & Engineering Intelligence

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00F0FF&center=true&vCenter=true&width=750&lines=VED+CHAOS+AI+%E2%80%94+STATEFUL+FASTMCP+ECOSYSTEM;PERSISTENT+POSTGRESQL+%2B+SQLITE+MEMORY;LIVE+TECH+FEEDS+%7C+REMOTEOK+%2B+HACKER+NEWS;DEFENSIVE+PENTESTING+%7C+AST+VULNERABILITY+AUDIT;QUANT+PAPER+TRADING+%7C+1%25+EQUITY+RISK+MANAGEMENT;HARDENED+BI-FACTOR+GATE+%7C+RATE-LIMITED+AUTH)](https://git.io/typing-svg)

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-FastMCP%20%7C%20Agentic-00F0FF?style=for-the-badge&logo=fastapi&logoColor=black" alt="FastMCP" />
  <img src="https://img.shields.io/badge/Memory-PostgreSQL%20%2B%20SQLite-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Security-AST%20Auditing%20%2B%20Rate--Limit-FF0055?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="Security" />
  <img src="https://img.shields.io/badge/Tests-19%20Passed%20(100%25)-00FF66?style=for-the-badge&logo=pytest&logoColor=black" alt="Tests" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-FFE873?style=for-the-badge&logo=python&logoColor=black" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-999999?style=for-the-badge" alt="License" />
</p>

---

**A stateful, rigorously tested FastMCP developer server built for persistent AI agents (Antigravity IDE, Claude Desktop, Cursor, Windsurf).**  
Combines **hybrid long-term memory (Cloud PostgreSQL + SQLite state persistence)**, a **rate-limited bi-factor persona gate**, **live developer hiring scrapers (RemoteOK & Hacker News)**, **static AST vulnerability auditing**, **quantitative paper-trading**, and **real-time tech research**.

</div>

---

## 📖 About Ved Chaos AI

### 💡 The Vision & Architecture
Most standard AI assistant tools are stateless and passive—they forget context across chat sessions, return mock responses, and lack developer-centric domain execution tools.

**Ved Chaos AI** solves cognitive continuity and developer execution through a modular, hardened FastMCP server:

* 🧠 **Hybrid Persistence Architecture**: 
  - **Cloud PostgreSQL (`asyncpg`)**: Long-term conversational memory with native full-text search (FTS GIN indexing) and 1536-dimensional pgvector cosine retrieval.
  - **Local SQLite (`state.db`)**: Atomic persistence for daily earning targets, executed micro-tasks, and historical work logs that survive process restarts.
* 🛡️ **Hardened Bi-Factor Persona Gate**: Constant-time HMAC authentication with a sliding-window lockout counter (locks out after 5 consecutive failures for 300 seconds) preventing brute-force traversal.
* 💼 **Live Developer Hiring & Bounty Discovery**: Queries live RemoteOK API and Hacker News job feeds in real time for direct founder and freelance contracts with zero platform cuts, backed by verified curated fallbacks.
* ⚔️ **Static AST Code Auditing**: Real Python AST syntax tree parsing detecting SQL injection via f-strings in database execution calls, shell injection via `os.system` or `subprocess(shell=True)`, `pickle` deserialization, and `eval`/`exec`.
* 📈 **Quant Paper Trading Suite**: Algorithmic technical indicators (SMA crossovers, RSI 14 momentum) with mathematical 1% equity risk sizing and a virtual paper portfolio.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User["Client Interface<br/>(Antigravity / Claude / Cursor / CLI)"]
    Gate{"Persona Access Gate<br/>Constant-Time HMAC + Lockout Guard"}
    
    User -->|Queries & Commands| Gate
    
    Gate -->|Unauthenticated / Guest| GuestMode["Guest Mode<br/>Standard Assistant, Private Memory Locked"]
    Gate -->|Authenticated Operator| CoreEngine["VED CHAOS CORE ENGINE<br/>FastMCP Server (main.py)"]
    
    subgraph "Core Agentic Tooling"
        CoreEngine --> Memory["Persistent Memory Layer<br/>(PostgreSQL FTS + Vector 1536)"]
        CoreEngine --> Freelance["Freelance Workflow Engine<br/>(Proposal Generator, Live Jobs, Scope Defender)"]
        CoreEngine --> Security["AST Security Suite<br/>(CWE-89, CWE-78, CWE-95, OWASP Top 10)"]
        CoreEngine --> Trading["Quantitative Paper Suite<br/>(SMA, RSI 14, 1% Risk Sizer, Virtual Book)"]
        CoreEngine --> Intel["Live Tech Feeds<br/>(Hacker News Live API + Fallback)"]
    end

    subgraph "Persistence & Background Daemon"
        Freelance --> Worker["Background Daemon<br/>(worker.py - Windows / Termux)"]
        Freelance --> LocalDB[(Local SQLite<br/>state.db)]
        Memory --> CloudDB[(Cloud PostgreSQL<br/>Supabase / Neon)]
    end
```

---

## 🔥 Key Pillars & Capabilities

### 🧠 1. Hybrid Persistence & Memory Layer
* **PostgreSQL GIN Full-Text Search**: Native PostgreSQL GIN indexes on `to_tsvector('simple', content)` for high-velocity query recall across stored interactions.
* **Vector Input Validation**: Strict validation for pgvector inputs ensuring exact 1536-dimensional embeddings and finite numerical values (rejecting `NaN` / `Inf`).
* **SQLite Daily State Persistence**: Tracks daily targets, executed micro-tasks (regex validation, JSON linting, syntax analysis), and freelance revenue in local `state.db`.

---

### 🛡️ 2. Hardened Bi-Factor Gate & Rate-Limiting
* **Constant-Time Comparison**: Uses `hmac.compare_digest` to prevent timing attacks and substring extraction.
* **Brute-Force Lockout Defense**: 5 consecutive failed attempts trigger an automatic 300-second (5 minute) lockout, completely rejecting automated dictionary attacks.
* **Memory Protection**: `search_chat_history`, `hybrid_search_memory`, `save_chat_example`, and `delete_chat_example` enforce authorization, preventing guest callers from accessing private memory.

---

### 💼 3. Live Direct Hiring & Bounty Discovery
* **Real Live Feeds**: Connects to the **RemoteOK API** and **Hacker News Job Stories** to surface active engineering and freelance roles in real-time.
* **Keyword & Budget Filtering**: Filters live listings by tech stack (`python`, `fastapi`, `automation`) and minimum payout thresholds.
* **Graceful Degradation**: If network access is offline or rate-limited, safely returns verified curated leads with transparent `is_live=False` telemetry.

---

### ⚔️ 4. Static AST Defensive Auditing
* **AST Visitor (`SecurityASTVisitor`)**:
  * 💉 **SQL Injection (CWE-89)**: Detects f-strings and `%`/`+` string concatenation passed into `.execute()`, `.raw()`, and `.fetch()` calls.
  * 💻 **Command Injection (CWE-78)**: Identifies `os.system()`, `os.popen()`, and `subprocess` calls with `shell=True`.
  * 📦 **Insecure Deserialization (CWE-502)**: Flags untrusted `pickle.loads()` usage.
  * 🚨 **Arbitrary Code Execution (CWE-95)**: Flags dangerous `eval()` and `exec()` calls.
* **Regex Secret Defense**: Supplemental scans for exposed OpenAI keys (`sk-`), GitHub tokens (`ghp_`), and hardcoded passwords.

---

## 🛠️ Complete MCP Tool Matrix (26 Tools)

| Category | Tool Name | Description | Auth Required |
|---|---|---|:---:|
| **Security & Gate** | `verify_security_access` | Constant-time 2FA verification with 5-attempt brute-force lockout | No |
| | `get_user_profile` | Returns developer identity profile (guest fallback if unauthorized) | Yes |
| | `get_writing_style` | Returns custom writing guidelines | Yes |
| | `get_system_prompt` | Returns core developer prompt | Yes |
| **Memory Engine** | `search_chat_history` | PostgreSQL full-text search with GIN index ranking | Yes |
| | `hybrid_search_memory` | Hybrid FTS + 1536-dim pgvector cosine similarity | Yes |
| | `save_chat_example` | Upsert interaction with SHA-256 deduplication | Yes |
| | `delete_chat_example` | Delete stored example by UUID | Yes |
| | `analyze_word_frequency` | Vocabulary frequency analysis over stored interactions | Yes |
| **Freelance & Jobs** | `scan_direct_bounties` | **Live RemoteOK & Hacker News** job scraper with fallback | No |
| | `auto_generate_freelance_proposal` | Generates high-converting client pitches | No |
| | `defend_scope_and_upsell` | Converts client scope creep into billable milestones | No |
| | `generate_portfolio_case_study` | Generates production case study markdown | No |
| | `run_client_delivery_shield` | Pre-handover syntax and secret leak inspection | No |
| **State & Tasks** | `process_micro_task` | **Executes real tasks** (regex, JSON, AST syntax) & persists to SQLite | No |
| | `set_daily_earning_target` | Updates daily revenue target in SQLite | No |
| | `get_earning_dashboard` | Reads persistent daily revenue, completed tasks & mood telemetry | No |
| | `log_freelance_earning` | Records contract revenue into SQLite state | No |
| **Code & Pentesting** | `audit_code_vulnerabilities` | **Real Python AST analysis** for SQLi, CWE-78, CWE-95, CWE-502 | No |
| | `owasp_security_checklist` | Authoritative OWASP Top 10 hardening checklist | No |
| **Intelligence** | `fetch_latest_intelligence` | **Live Hacker News API** breaking tech feed with offline fallback | No |
| | `deep_research_dossier` | Dynamic multi-section technical research dossier | No |
| **Quantitative** | `analyze_trading_technical_setup` | SMA short/long crossovers, RSI 14 momentum, and support/resistance | No |
| | `calculate_position_risk_management` | Exact position sizing enforcing strict 1% equity risk rule | No |
| | `execute_paper_trade` | Simulated zero-risk paper portfolio execution | No |
| | `craft_brilliant_prompt` | Professional prompt engineering for coding and creative synthesis | No |

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
Populate your credentials:
```ini
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/postgres  # Optional (for cloud memory)
VED_USER_ID=ved-local
VED_SECURITY_PIN=your_custom_pin_here
VED_ACTIVATION_PHRASE=your_secret_phrase_here
MAX_SEARCH_RESULTS=10
MAX_TEXT_CHARS=12000
```

### 3. Run Automated Tests
```bash
pytest -v
```
All **19 tests** covering AST security, rate limiting, vector validation, SQLite state persistence, scrapers, and trading indicators run with **100% pass rate**.

### 4. Run Background Daemon
```bash
# Continuous loop (Windows CMD / Termux / Linux):
python worker.py

# Single diagnostic iteration:
python worker.py --once
```

---

## 🔒 Security & Privacy Notice
* **Zero PII**: This repository contains zero personal identifying information (no real addresses, birthdays, or family details).
* **Network Isolation**: All client credentials and database tokens remain strictly within your local `.env` and are never committed to version control.
* **Lockout Policy**: In-memory rate limiting rejects brute-force authentication attempts after 5 consecutive failures.

---

### 🛡️ License
Licensed under the [MIT License](LICENSE). Built for autonomous, persistent developer tooling.
