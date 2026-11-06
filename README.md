<div align="center">

# ⚡ VED CHAOS AI ⚡
### Autonomous Agentic FastMCP Server, Cloud Memory & Freelance Intelligence Engine

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00F0FF&center=true&vCenter=true&width=750&lines=VED+CHAOS+AI+%E2%80%94+FULL-DUPLEX+AGENTIC+FASTMCP;AUTONOMOUS+FREELANCING+%7C+%24500%2FDAY+REVENUE+TARGET;2FA+SECURITY+GATE+%7C+PASSCODE+%2B+TRIGGER+PHRASE;DEFENSIVE+PENTESTING+%7C+OWASP+VULNERABILITY+AUDIT;QUANTITATIVE+TRADING+%7C+RISK-MANAGED+PAPER+SUITE;REAL-TIME+TECH+INTELLIGENCE+%26+RESEARCH+DOSSIERS)](https://git.io/typing-svg)

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-FastMCP%20%7C%20Agentic-00F0FF?style=for-the-badge&logo=fastapi&logoColor=black" alt="FastMCP" />
  <img src="https://img.shields.io/badge/Security-2FA%20Bi-Factor%20Gate-FF0055?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="2FA Gate" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL%20%2B%20pgvector-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Autonomous%20Goal-%24500%20USD%20%2F%20Day-00FF66?style=for-the-badge&logo=cashapp&logoColor=black" alt="Revenue Goal" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-FFE873?style=for-the-badge&logo=python&logoColor=black" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-999999?style=for-the-badge" alt="License" />
</p>

---

**A stateful, production-grade FastMCP ecosystem built for high-throughput AI agents (Antigravity IDE, Claude Desktop, Cursor, Windsurf).**  
Combines **long-term cloud PostgreSQL memory**, a **2-Factor Security Gate**, **autonomous $500/day freelancing & zero-fee bounty discovery**, **defensive code pentesting**, **quantitative trading**, and **real-time tech intelligence**.

</div>

---

## 🏛️ System Architecture

```mermaid
graph TD
    User["Client Interface<br/>(Antigravity / Claude / Cursor / CLI)"]
    Gate{"2FA Security Gate<br/>Secret Phrase + Private PIN"}
    
    User -->|Queries & Commands| Gate
    
    Gate -->|Unauthenticated / Guest| GuestMode["Guest Mode<br/>Neutral Assistant, Locked Persona & Tools"]
    Gate -->|Authenticated Owner| CoreEngine["VED CHAOS CORE ENGINE<br/>FastMCP Server (main.py)"]
    
    subgraph "Core Agentic Capabilities"
        CoreEngine --> Persona["Personality & Style Layer<br/>(Hinglish, Zero Punctuation, Core & Unhinged)"]
        CoreEngine --> Memory["Cloud Memory Layer<br/>(PostgreSQL FTS + pgvector Embeddings)"]
        CoreEngine --> Prompts["Prompt Engineering Engine<br/>(Production Coding, AI Art, System Prompts)"]
        CoreEngine --> Freelance["Autonomous Earning Pipeline<br/>($500/Day Target, Micro-Tasks, Celebration Mode)"]
        CoreEngine --> Bounties["Zero-Fee Bounty Scraper<br/>(Reddit r/forhire + Twitter/X Dev Bounties)"]
        CoreEngine --> Quality["Quality Shield & Scope Defender<br/>(AST Audit, Secret Leaks, $50-$150 Upsells)"]
        CoreEngine --> Intel["Live Tech Research & News<br/>(AI Models, CVE Advisories, Market Spikes)"]
        CoreEngine --> Security["Defensive Pentesting Suite<br/>(SQLi, Command Injection, Pickle, OWASP Top 10)"]
        CoreEngine --> Trading["Quantitative Trading Engine<br/>(SMA, RSI 14, 1% Risk Rule, Paper Trading)"]
    end

    subgraph "Execution & Persistence"
        Freelance --> Worker["24/7 Background Daemon<br/>(worker.py - Windows / Termux)"]
        Memory --> CloudDB[(Cloud PostgreSQL<br/>Supabase / Neon)]
    end
```

---

## 🔥 Key Pillars & Features

### 🛡️ 1. Two-Factor Security Gate (Custom Secret Phrase + Private PIN)
* **Layer 1: Activation Phrase** &rarr; Configurable via environment (`VED_ACTIVATION_PHRASE`)
* **Layer 2: Secret Passcode** &rarr; Configurable via environment (`VED_SECURITY_PIN`)
* **Guest Fallback**: If an unauthorized user accesses the server without both credentials, the server immediately drops into **Standard Guest Mode**—a polite, neutral AI assistant with all custom personas and developer tools strictly locked.

---

### 💰 2. Autonomous Freelance Engine & $500/Day Target
* **Daily Goal Tracker**: Targets **$500 USD/day** (configurable anytime via `set_daily_earning_target`).
* **Continuous Micro-Tasks ($10 - $50)**: Rapid turnaround execution (JSON parsing, regex data cleanup, small web scrapers, prompt tuning) for nonstop cash flow.
* **Autonomous Pitch Generator**: Reads client job postings on Upwork/Fiverr and emits tailored, high-converting proposals within seconds.
* **Happiness Milestone Trigger**: When cumulative daily revenue reaches $500, Ved AI triggers the **`super_happy_celebration`** state with full celebration feedback.

---

### 🎯 3. Direct Zero-Commission Bounty Hunter (Reddit & Twitter)
* Bypasses Upwork/Fiverr's 10%–20% commission cuts.
* Filters live direct client bounties on **Reddit (`r/forhire`, `r/freelance_forhire`)** and **Twitter/X Dev Bounties**.
* Secures 100% net payouts directly to Stripe, PayPal, or Crypto.

---

### 🛡️ 4. Client Delivery Quality Shield & Scope Defender
* **Pre-Handover AST Audit**: Validates syntax, detects hardcoded secrets/API keys (`ghp_`, `sk-`), catches placeholder `TODO` stubs, and verifies defensive exception boundaries.
* **Scope Creep Defender**: Politely blocks clients from requesting free scope expansions, converting extra requests into **$50–$150 paid milestone add-ons**.
* **Instant Portfolio Generator**: Emits polished, production-grade GitHub README case studies in 10 seconds to close hesitant clients.

---

### ⚔️ 5. Defensive Pentesting & OWASP Hardening
* **Static Vulnerability Scanner**:
  * 💉 **SQL Injection (CWE-89)**: Detects raw string formatting in SQL queries and provides parameterized fixes.
  * 💻 **Command Injection (CWE-78)**: Identifies insecure `os.system` and `eval`/`exec` calls with `subprocess.run` tokenization patches.
  * 📦 **Insecure Deserialization (CWE-502)**: Flags untrusted `pickle` usage with JSON/HMAC alternatives.
  * 🔐 **Weak Cryptography (CWE-328)**: Catches MD5/SHA1 and enforces salted hashing.
* **OWASP Top 10 Checklist**: Comprehensive defensive audit guide covering RBAC, SSRF defense, rate limiting, and secure HTTP headers.

---

### 📈 6. Quantitative Trading & Risk Management Suite
* **Technical Indicator Analysis**: Calculates Fast/Slow Moving Average crossovers (SMA), RSI 14 momentum, and market trend bias (Bullish Expansion, Overbought, Oversold).
* **The 1% Risk Rule Calculator**: Mathematically sizes positions based on entry, stop-loss, and capital to ensure maximum risk never exceeds 1% of equity.
* **Zero-Risk Paper Trading**: Simulates virtual trades on a virtual $10,000 USD portfolio to test win rates without risking real capital.

---

### 📡 7. Real-Time Tech Intelligence & Deep Research
* **Live Intelligence Wire**: Scans real-time developments across AI models (reasoning, SLMs), cybersecurity CVE bulletins, freelance hourly rate surges, and GPU hardware architectures.
* **5-Pillar Research Dossiers**: Generates deep-dive structured technical reports (Thesis, Mechanisms, Breaking Updates, Risk Audit, Action Steps) on any topic.

---

### 🤖 8. 24/7 Background Daemon (`worker.py`)
* Lightweight background worker script that runs silently on **Windows CMD**, a **Linux VPS**, or **Android Termux**.
* Continuously polls zero-fee bounties, checks the $500 target progress, and emits live status telemetry heartbeats.

---

## 🛠️ Complete MCP Tools Matrix

| Tool | Parameters | Description |
|---|---|---|
| `verify_security_access` | `pin`, `activation_phrase` | 2FA Gate: Verifies configured Secret Phrase + Private PIN to unlock owner mode |
| `get_system_prompt` | `security_pin`, `activation_phrase`, `mode` | Emits copy-ready system prompt (`core` / `unhinged`) or guest prompt |
| `get_user_profile` | `security_pin`, `activation_phrase` | Returns complete custom profile if authorized, otherwise guest profile |
| `get_writing_style` | `security_pin`, `activation_phrase` | Returns Hinglish zero-punctuation style guide if authenticated |
| `craft_brilliant_prompt` | `task`, `domain`, `output_format` | Generates battle-tested production prompts (Coding, AI Art, LLM Systems) |
| `process_micro_task` | `task_type`, `amount_usd`, `summary` | Executes and logs $10–$50 micro-gigs for continuous daily cash flow |
| `set_daily_earning_target` | `target_usd` | Configures the daily earning goal in USD (default: $500) |
| `get_earning_dashboard` | *None* | Returns live daily revenue progress, target status, and agent mood |
| `log_freelance_earning` | `amount_usd`, `client_or_platform`, `job_description` | Logs job revenue and triggers celebration mode upon hitting target |
| `auto_generate_freelance_proposal` | `job_post_title`, `client_budget`, `required_tech_stack` | Generates high-converting client pitches for Upwork, Fiverr, or Twitter |
| `scan_direct_bounties` | `platform`, `min_budget_usd`, `keyword` | Filters 0% commission direct bounties from Reddit (`r/forhire`) & Twitter |
| `defend_scope_and_upsell` | `client_message`, `original_agreement`, `extra_feature_cost_usd` | Converts scope creep into $50–$150 billable add-on milestones |
| `generate_portfolio_case_study` | `niche_topic`, `tech_stack` | Emits an instant GitHub README case study to close clients |
| `run_client_delivery_shield` | `code_content`, `language` | AST syntax check, secret leak scan, and placeholder audit for 5-star ratings |
| `fetch_latest_intelligence` | `category`, `query`, `limit` | Breaking news feed across AI tech, cybersecurity, freelance rates, and GPUs |
| `deep_research_dossier` | `topic`, `research_depth` | Generates a structured 5-pillar technical intelligence report |
| `audit_code_vulnerabilities` | `source_code`, `language` | Defensive pentesting: detects SQLi, command injection, pickle, and weak hashes |
| `owasp_security_checklist` | `component_type` | Authoritative OWASP Top 10 defensive hardening checklist |
| `analyze_trading_technical_setup` | `ticker`, `prices`, `timeframe` | Computes SMA crossovers, RSI 14 momentum, and trend bias |
| `calculate_position_risk_management` | `account_balance_usd`, `risk_percentage`, `entry_price`, `stop_loss_price`, `target_profit_price` | Calculates exact position sizing and 1% risk rule metrics |
| `execute_paper_trade` | `action`, `ticker`, `quantity`, `price` | Simulates virtual trades on a $10,000 USD portfolio with zero risk |
| `search_chat_history` | `query`, `limit` | Full-text search across past conversations via PostgreSQL FTS |
| `save_chat_example` | `role`, `content`, `source_label` | Saves selected messages to the cloud memory store |
| `analyze_word_frequency` | `limit` | Vocabulary frequency analysis across stored messages |
| `delete_chat_example` | `example_id` | Deletes a stored conversation example by UUID |

---

## 🚀 Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/vedchaos/ved-chaos-ai.git
cd ved-chaos-ai
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure `.env`
```bash
cp .env.example .env
```
Edit your `.env` file:
```env
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/postgres
VED_USER_ID=ved-local
VED_SECURITY_PIN=your_private_pin_here
VED_ACTIVATION_PHRASE=your_secret_phrase_here
MAX_SEARCH_RESULTS=10
```

### 4. Seed Cloud Database (Optional)
```bash
python seed.py
```

### 5. Launch FastMCP Server
```bash
python main.py
```

### 6. (Optional) Start 24/7 Background Daemon
```bash
python worker.py
```

---

## 🔌 Connecting to AI Clients (Antigravity, Claude, Cursor)

Add the following to your AI client's MCP configuration (`settings.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "ved-chaos-ai": {
      "command": "python",
      "args": ["/path/to/ved-chaos-ai/main.py"],
      "env": {
        "VED_SECURITY_PIN": "your_private_pin_here",
        "VED_ACTIVATION_PHRASE": "your_secret_phrase_here",
        "VED_USER_ID": "ved-local",
        "DATABASE_URL": "postgresql://..."
      }
    }
  }
}
```

---

<div align="center">

### 🔒 Built with precision by Ved Chaos. Engineered for autonomy.

[![GitHub Repo](https://img.shields.io/badge/GitHub-vedchaos%2Fved--chaos--ai-00F0FF?style=for-the-badge&logo=github)](https://github.com/vedchaos/ved-chaos-ai)

</div>
