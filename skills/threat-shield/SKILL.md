---
name: threat-shield
description: Pre-flight link safety inspection, phishing domain detection, masquerading payload defense, and malware file verification to protect the host PC.
---

# Defensive Threat & URL / Virus Shield Skill

This skill equips the agent with automated defensive inspection tools to analyze suspicious links, detect phishing lookalikes, inspect files for disguised executables, and block malware payloads before execution.

## 1. Operating Principles & The Zero-Trust Gate
- **Never Blindly Click:** Any untrusted URL received from clients, job listings, or web pages must first be validated through `inspect_url_safety`.
- **Pre-flight HEAD Inspection:** Follows redirect chains and inspects response `Content-Type` headers without downloading executable payloads to disk.
- **Masquerade Detection:** Checks file magic bytes (`MZ` header) against file extensions to catch executables disguised as PDFs, JPGs, or documents (`invoice.pdf.exe`).

## 2. Core Security Tools
1. **`inspect_url_safety`**:
   - Scores URLs from 0 to 100 based on risk factors.
   - Detects brand typosquatting (e.g. `paypa1`, `steam-comunitty`).
   - Flags direct IP loggers, high-abuse TLDs (`.top`, `.xyz`, `.zip`), and URL shorteners.
   - Traces redirect chains via asynchronous HEAD requests.
2. **`inspect_file_threat`**:
   - Detects double extensions (`.pdf.exe`, `.docx.scr`).
   - Flags standalone dangerous file types (`.exe`, `.bat`, `.vbs`, `.ps1`, `.msi`).
   - Validates PE binary headers vs declared extensions.
   - Generates SHA-256 cryptographic fingerprints.

## 3. Threat Action Policy
- **Risk Score < 30 (SAFE):** Proceed with normal processing.
- **Risk Score 30 - 59 (SUSPICIOUS):** Caution user and require explicit confirmation.
- **Risk Score >= 60 (MALICIOUS):** **ABORT ACTION IMMEDIATELY.** Do not click, do not download, and alert operator.
