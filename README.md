<div align="center">

# ⚡ VED CHAOS AI ⚡
### Stateful FastMCP Memory Engine, Freelance Automation & Developer Intelligence

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00F0FF&center=true&vCenter=true&width=750&lines=VED+CHAOS+AI+%E2%80%94+STATEFUL+FASTMCP+ECOSYSTEM;PERSISTENT+POSTGRESQL+MEMORY+%7C+HYBRID+FTS+%2B+VECTOR;FREELANCE+WORKFLOW+AUTOMATION+%7C+ZERO-COMMISSION+BOUNTIES;DEFENSIVE+PENTESTING+%7C+OWASP+VULNERABILITY+AUDIT;QUANT+PAPER+TRADING+%7C+1%25+EQUITY+RISK+MANAGEMENT;BI-FACTOR+PERSONA+TOGGLE+%7C+OWNER+VS+GUEST+MODES)](https://git.io/typing-svg)

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-FastMCP%20%7C%20Agentic-00F0FF?style=for-the-badge&logo=fastapi&logoColor=black" alt="FastMCP" />
  <img src="https://img.shields.io/badge/Memory-PostgreSQL%20%2B%20pgvector-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Security-Persona%20Access%20Gate-FF0055?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="Persona Gate" />
  <img src="https://img.shields.io/badge/Workflow-Freelance%20Automation-00FF66?style=for-the-badge&logo=cashapp&logoColor=black" alt="Workflow Automation" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-FFE873?style=for-the-badge&logo=python&logoColor=black" alt="Python" />
  <img src="https://img.shields.io/badge/License-MIT-999999?style=for-the-badge" alt="License" />
</p>

---

**A stateful, production-ready FastMCP server built for persistent AI agents (Antigravity IDE, Claude Desktop, Cursor, Windsurf).**  
Combines **long-term cloud PostgreSQL memory with FTS indexing**, a **client-level bi-factor persona gate**, **freelance workflow automation & direct bounty scrapers**, **defensive code pentesting**, **quantitative paper-trading**, and **real-time tech research**.

</div>

---

## 📖 About Ved Chaos AI

### 💡 The Vision & Architecture
Most standard AI agents are stateless and passive—they forget architectural context across chat sessions, communicate in generic corporate platitudes, and lack developer-centric domain tools.

**Ved Chaos AI** solves cognitive continuity and developer execution through a modular FastMCP server:

* 🧠 **Persistent Cloud Memory (Core Hero)**: Backed by cloud PostgreSQL with full-text search (FTS GIN indexing) and extensible vector retrieval, preserving user profiles, historical architectural decisions, and chat memory across IDE reboots.
* 🛠️ **Freelance Workflow Automation**: Accelerates independent engineers with rapid client pitch drafting, zero-fee direct bounty discovery (Reddit / Twitter), AST delivery shields, and scope-creep defense.
* 🛡️ **Bi-Factor Persona Gate**: A client-level session gate separating public/guest interactions from unhinged developer tools and owner personas.
* ⚔️ **Defensive Code Auditing**: Static AST vulnerability scanner checking for SQL injection, command execution, pickle serialization, and OWASP Top 10 hardening.
* 📈 **Quant Paper Trading Suite**: Algorithmic technical indicators (SMA crossovers, RSI 14 momentum) with mathematical 1% equity risk sizing and a virtual paper portfolio.

---

## 🏛️ System Architecture

```mermaid
graph TD
    User["Client Interface<br/>(Antigravity / Claude / Cursor / CLI)"]
    Gate{"Persona Access Gate<br/>Secret Phrase + Private PIN"}
    
    User -->|Queries & Commands| Gate
    
    Gate -->|Unauthenticated / Guest| GuestMode["Guest Mode<br/>Neutral Assistant, Locked Persona & Tools"]
    Gate -->|Authenticated Operator| CoreEngine["VED CHAOS CORE ENGINE<br/>FastMCP Server (main.py)"]
    
    subgraph "Core Agentic Tooling"
        CoreEngine --> Memory["Persistent Memory Layer<br/>(PostgreSQL FTS + Asyncpg Pool)"]
        CoreEngine --> Freelance["Freelance Workflow Engine<br/>(Pitch Generator, Bounty Scraper, Scope Defender)"]
        CoreEngine --> Quality["Quality Shield<br/>(AST Syntax Audit, Secret Leaks, Stubs)"]
        CoreEngine --> Security["Defensive Pentesting Suite<br/>(SQLi, Command Injection, Pickle, OWASP Top 10)"]
        CoreEngine --> Trading["Quantitative Paper Suite<br/>(SMA, RSI 14, 1% Risk Sizer, Virtual Book)"]
        CoreEngine --> Intel["Live Tech Research<br/>(AI Models, CVE Advisories, Market Spikes)"]
    end

    subgraph "Execution & Persistence"
        Freelance --> Worker["Background Daemon<br/>(worker.py - Windows / Termux)"]
        Memory --> CloudDB[(Cloud PostgreSQL<br/>Supabase / Neon)]
    end
```

---

## 🔥 Key Pillars & Capabilities

### 🧠 1. Cloud PostgreSQL & Persistent Memory (Hero Engine)
* **Full-Text Search (FTS)**: Native PostgreSQL GIN indexes on `to_tsvector('simple', content)` for high-velocity query recall across stored interactions.
* **Connection Pooling**: Stateful `asyncpg.create_pool` with defensive retry routines for zero connection exhaustion under high concurrency.
* **Multi-User Isolation**: User-scoped queries (`user_id = $1`) with database schema prepared for Row-Level Security (RLS).

---

### 🛡️ 2. Bi-Factor Persona Gate & Access Toggle
* **Client-Level Persona Gate**: Separates owner tools and unhinged communication from generic guest interactions using environment-configured credentials (`VED_ACTIVATION_PHRASE` and `VED_SECURITY_PIN`).
* **Guest Neutral Mode**: Unauthorized requests gracefully drop back to a standard, neutral AI assistant without exposing private toolchains or custom prompts.
* *(Note: For network transport layer security, standard FastMCP Bearer token / reverse proxy authorization should be configured at the deployment boundary).*

---

### 💼 3. Freelance Workflow Automation & Bounty Discovery
* **Autonomous Pitch Generator**: Emits tailored, technical client proposals for job posts on Upwork, Fiverr, or Twitter dev boards.
* **Zero-Fee Bounty Scraper**: Aggregates direct client postings on Reddit (`r/forhire`, `r/freelance_forhire`) and Twitter dev bounties to eliminate marketplace platform commissions.
* **Scope Creep Defender**: Identifies client requests outside the agreed project scope and provides polite, assertive responses converting them into $50–$150 billable milestone add-ons.
* **Client Delivery Shield**: Pre-handover static AST scanner checking code for hardcoded secrets (`sk-`, `ghp_`), syntax flaws, and uncompleted `TODO` stubs.

---

### ⚔️ 4. Defensive Pentesting & OWASP Hardening
* **Static AST Code Auditor**:
  * 💉 **SQL Injection (CWE-89)**: Detects unsafe string formatting in SQL statements and proposes parameterized equivalents.
  * 💻 **Command Injection (CWE-78)**: Identifies insecure `os.system` and `eval`/`exec` calls with tokenized `subprocess.run` mitigations.
  * 📦 **Insecure Deserialization (CWE-502)**: Flags untrusted `pickle` usage with JSON/HMAC recommendations.
  * 🔐 **Weak Cryptography (CWE-328)**: Flags legacy MD5/SHA1 and enforces salted cryptographic hashing.
* **OWASP Top 10 Hardening**: Authoritative defensive checklists covering RBAC, SSRF defense, rate limiting, and secure headers.

---

### 📈 5. Quantitative Paper Trading & Risk Sizing
* **Algorithmic Technical Indicators**: Computes SMA crossovers (fast vs slow), RSI 14 momentum, and market expansion/reversal conditions.
* **1% Risk Rule Engine**: Sizes equity position limits based on account balance, entry price, and stop-loss targets to cap maximum downside risk.
* **Virtual Paper Trading Book**: Simulates trades against a virtual $10,000 USD portfolio to test win rates without real financial exposure.

---

### 📡 6. Real-Time Tech Intelligence & Deep Research
* **Real-Time Tech Monitor**: Aggregates breaking updates across foundational AI models, cybersecurity CVE bulletins, and developer tooling.
* **Structured Research Dossiers**: Produces 5-pillar technical briefings (Thesis, Mechanics, Breaking Changes, Security Audit, Action Steps).

---

### 🤖 7. Background Worker Daemon (`worker.py`)
* Lightweight background runner for **Windows**, **Linux VPS**, or **Android Termux**.
* Periodically refreshes bounty feeds, runs scheduled paper-trading checks, and logs health heartbeats.

---

## ⚠️ Disclaimers & Operational Compliance

> [!WARNING]
> **Trading & Financial Disclaimer**: The quantitative trading and risk sizing tools in this repository are for **educational and simulated paper-trading purposes only**. They do not constitute financial advice, trading signals, or investment recommendations. Never trade real capital without professional evaluation.

> [!NOTE]
> **Scraping & Platform Terms of Service**: Bounty scanners and external feeds are built to respect platform rate limits and terms of service. Operators should use their own authorized API credentials for production data retrieval.

> [!IMPORTANT]
> **Security Boundaries**: The bi-factor gate is an in-context LLM persona and prompt toggle. For mission-critical multi-tenant deployments, pair this with network-level authentication (Bearer tokens, TLS, and database Row Level Security).

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
| `search_chat_history` | `query`, `limit` | Full-text search across past conversations via PostgreSQL FTS (content_tsv) |
| `hybrid_search_memory` | `query`, `embedding`, `limit` | Hybrid search combining FTS keyword rank and pgvector HNSW cosine distance |
| `save_chat_example` | `role`, `content`, `source_label`, `embedding` | Stores snippet into cloud memory with SHA-256 deduplication & pgvector embeddings |
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
