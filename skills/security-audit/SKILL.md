---
name: security-audit
description: Defensive security auditing, vulnerability assessment, OWASP Top 10 hardening, and static code security analysis to identify and remediate security risks.
---

# Defensive Security Auditing & Vulnerability Hardening Skill

This skill provides an automated defensive security auditing toolkit designed to analyze source code, identify common vulnerabilities (OWASP Top 10), and provide concrete hardening remediations.

## Scope & Operating Directives
- **Focus:** Defensive code review, static analysis, threat modeling, and secure architecture.
- **Principles:**
  - Detect high-risk vulnerability patterns (SQLi, command injection, insecure deserialization, weak hashing, hardcoded credentials).
  - Provide actionable, secure patches and remediations.
  - Follow OWASP Top 10 defensive standards.
- **Prohibited:** Generating functional exploits, attack payloads, or weaponized intrusion scripts.

## Core Security Tools
1. **`audit_code_vulnerabilities`**: Performs static analysis on scripts, scoring them from A+ to F and providing CWE-mapped security remediations.
2. **`owasp_security_checklist`**: Delivers a comprehensive defensive hardening checklist for Web APIs, cloud microservices, and authentication flows.

