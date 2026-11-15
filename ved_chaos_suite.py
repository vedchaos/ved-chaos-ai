"""Ved Chaos AI — Upgraded Core Intelligence & GitHub-Integrated Tool Suite.

Branded modules engineered for Ved Chaos AI:
1. Offline-First Hybrid Memory Engine (SQLite FTS5 BM25 + Vector Cosine Similarity)
2. Ved Chaos Codebase Ingestor (Local & GitHub Repo Digest Packer + Token Estimator)
3. Ved Chaos Supply-Chain Shield (Live OSV.dev CVE Audit + Shannon Entropy Secret Scanner)
4. Ved Chaos Thought Chain (Persistent SQLite Sequential Reasoning & Branching Engine)
5. Ved Chaos GitHub Radar (Live GitHub Repo Discovery & Permissive License Fit Evaluator)
"""

from __future__ import annotations

import datetime
import fnmatch
import hashlib
import json
import math
import os
import re
import sqlite3
import tomllib
import uuid
from collections import Counter
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

import httpx

VED_BRAND = "Ved Chaos AI"
VED_SUITE_VERSION = "0.4.0"

DEFAULT_IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    "target",
    ".next",
    ".nuxt",
    "coverage",
}

DEFAULT_IGNORE_PATTERNS = {
    "*.pyc",
    "*.pyo",
    "*.pyd",
    "*.so",
    "*.dll",
    "*.exe",
    "*.bin",
    "*.db",
    "*.db-shm",
    "*.db-wal",
    "*.sqlite",
    "*.sqlite3",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.gif",
    "*.ico",
    "*.webp",
    "*.pdf",
    "*.zip",
    "*.tar",
    "*.gz",
    "*.7z",
    "*.lock",
}

SENSITIVE_SECRET_RULES: list[tuple[str, str, str]] = [
    ("AWS Access Key ID", r"\bAKIA[0-9A-Z]{16}\b", "Critical"),
    ("GitHub Classic PAT", r"\bghp_[A-Za-z0-9]{36}\b", "Critical"),
    ("GitHub Fine-Grained PAT", r"\bgithub_pat_[A-Za-z0-9_]{22,}\b", "Critical"),
    ("OpenAI / Anthropic Secret Key", r"\bsk-(?:ant-api\d+-|proj-)?[A-Za-z0-9_\-]{20,}\b", "Critical"),
    ("Stripe Live Secret Key", r"\bsk_live_[A-Za-z0-9]{20,}\b", "Critical"),
    ("Slack Token", r"\bxox[baprs]-[A-Za-z0-9\-]{10,}\b", "Critical"),
    ("Private Cryptographic Key", r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----", "Critical"),
    (
        "Hardcoded Credential Assignment",
        r"(?i)\b(?:api[_-]?key|secret[_-]?key|password|passwd|auth[_-]?token|access[_-]?token)\s*[:=]\s*['\"]([A-Za-z0-9_\-./+=]{10,})['\"]",
        "High",
    ),
]

PERMISSIVE_LICENSES = {"MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "ISC", "Unlicense", "CC0-1.0"}


# ==============================================================================
# Shared SQLite Initialization & Security Helpers
# ==============================================================================


def ensure_upgrade_tables(conn: sqlite3.Connection) -> None:
    """Create Ved Chaos AI upgrade tables (local FTS5 memory + reasoning chains)."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS local_memory (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            content_hash TEXT NOT NULL,
            source_label TEXT NOT NULL DEFAULT 'manual',
            embedding_json TEXT,
            created_at TEXT NOT NULL,
            UNIQUE(user_id, content_hash)
        )
    """)
    conn.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS local_memory_fts USING fts5(
            id UNINDEXED,
            user_id UNINDEXED,
            role,
            content,
            source_label
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS reasoning_chains (
            chain_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'ACTIVE',
            final_decision TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS reasoning_steps (
            id TEXT PRIMARY KEY,
            chain_id TEXT NOT NULL,
            step_number INTEGER NOT NULL,
            total_thoughts INTEGER NOT NULL,
            thought TEXT NOT NULL,
            confidence REAL NOT NULL DEFAULT 0.8,
            is_revision INTEGER NOT NULL DEFAULT 0,
            revises_step INTEGER,
            branch_from_step INTEGER,
            created_at TEXT NOT NULL
        )
    """)


def _is_blocked_system_root(target: Path) -> bool:
    """Prevent scanning sensitive OS directories."""
    resolved = str(target.resolve()).lower()
    blocked_prefixes = (
        "c:\\windows",
        "c:\\program files",
        "c:\\program files (x86)",
        "/etc",
        "/usr/bin",
        "/sbin",
        "/bin",
    )
    return any(resolved == p or resolved.startswith(p + os.sep) for p in blocked_prefixes)


def _shannon_entropy(data: str) -> float:
    """Compute Shannon entropy (bits per character) for secret detection."""
    if not data:
        return 0.0
    counts = Counter(data)
    length = len(data)
    return -sum((cnt / length) * math.log2(cnt / length) for cnt in counts.values())


def _redact_secrets_in_text(text: str) -> tuple[str, int]:
    """Redact matched secret literals before sending repository digests to an LLM."""
    redactions = 0
    sanitized = text
    for _, pattern, _ in SENSITIVE_SECRET_RULES:
        sanitized, count = re.subn(pattern, "[REDACTED_BY_VED_CHAOS_SHIELD]", sanitized)
        redactions += count
    return sanitized, redactions


def _cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Compute cosine similarity between two equal-length vectors safely."""
    if len(vec_a) != len(vec_b) or not vec_a:
        return 0.0
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


def _build_safe_fts_query(raw_query: str) -> str:
    """Convert raw user query text into safe FTS5 OR-joined terms."""
    tokens = re.findall(r"[A-Za-z0-9_\u0900-\u097F]{2,}", raw_query or "")
    if not tokens:
        return ""
    unique_tokens = list(dict.fromkeys(tokens))[:12]
    return " OR ".join(f'"{tok}"' for tok in unique_tokens)


# ==============================================================================
# 1. Offline-First Local Hybrid Memory Engine (SQLite FTS5 + Vector Cosine)
# ==============================================================================


def local_save_memory(
    db_path: Path,
    user_id: str,
    role: str,
    content: str,
    content_hash: str,
    source_label: str,
    embedding: list[float] | None,
    is_truncated: bool,
) -> dict[str, Any]:
    """Upsert a memory entry into local SQLite + FTS5 index."""
    now_str = datetime.datetime.now(datetime.timezone.utc).isoformat()
    embedding_json = json.dumps(list(embedding)) if embedding is not None else None
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        ensure_upgrade_tables(conn)
        existing = conn.execute(
            "SELECT id, created_at FROM local_memory WHERE user_id = ? AND content_hash = ?",
            (user_id, content_hash),
        ).fetchone()
        if existing:
            mem_id = existing["id"]
            created_at = existing["created_at"]
            conn.execute(
                """
                UPDATE local_memory
                SET source_label = ?, embedding_json = COALESCE(?, embedding_json)
                WHERE id = ?
                """,
                (source_label, embedding_json, mem_id),
            )
            conn.execute("DELETE FROM local_memory_fts WHERE id = ?", (mem_id,))
            conn.execute(
                "INSERT INTO local_memory_fts (id, user_id, role, content, source_label) VALUES (?, ?, ?, ?, ?)",
                (mem_id, user_id, role, content, source_label),
            )
            conn.commit()
            return {
                "ok": True,
                "id": mem_id,
                "created_at": created_at,
                "deduplicated": True,
                "truncated": is_truncated,
                "backend": "local_sqlite_fts5",
            }

        mem_id = str(uuid.uuid4())
        conn.execute(
            """
            INSERT INTO local_memory (id, user_id, role, content, content_hash, source_label, embedding_json, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (mem_id, user_id, role, content, content_hash, source_label, embedding_json, now_str),
        )
        conn.execute(
            "INSERT INTO local_memory_fts (id, user_id, role, content, source_label) VALUES (?, ?, ?, ?, ?)",
            (mem_id, user_id, role, content, source_label),
        )
        conn.commit()
        return {
            "ok": True,
            "id": mem_id,
            "created_at": now_str,
            "deduplicated": False,
            "truncated": is_truncated,
            "backend": "local_sqlite_fts5",
        }


def local_search_memory(db_path: Path, user_id: str, query: str, limit: int) -> list[dict[str, Any]]:
    """Search local SQLite FTS5 memory with BM25 ranking."""
    fts_query = _build_safe_fts_query(query)
    if not fts_query:
        return []
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        ensure_upgrade_tables(conn)
        rows = conn.execute(
            """
            SELECT m.id, m.role, m.content, m.source_label, m.created_at,
                   (-bm25(local_memory_fts)) AS rank
            FROM local_memory_fts
            JOIN local_memory m ON m.id = local_memory_fts.id
            WHERE local_memory_fts MATCH ? AND m.user_id = ?
            ORDER BY rank DESC, m.created_at DESC
            LIMIT ?
            """,
            (fts_query, user_id, limit),
        ).fetchall()
        return [
            {
                "id": r["id"],
                "role": r["role"],
                "content": r["content"],
                "source_label": r["source_label"] or "",
                "created_at": r["created_at"],
                "fts_rank": round(float(r["rank"] or 0.0), 6),
                "backend": "local_sqlite_fts5",
            }
            for r in rows
        ]


def local_hybrid_search_memory(
    db_path: Path,
    user_id: str,
    query: str,
    embedding: list[float] | None,
    limit: int,
) -> list[dict[str, Any]]:
    """Combine FTS5 BM25 score and vector cosine similarity in local SQLite."""
    if embedding is None:
        return local_search_memory(db_path, user_id, query, limit)

    fts_scores: dict[str, float] = {}
    if query:
        for hit in local_search_memory(db_path, user_id, query, max(limit * 3, 20)):
            fts_scores[hit["id"]] = max(0.0, float(hit["fts_rank"]))

    max_fts = max(fts_scores.values(), default=1.0) or 1.0
    scored_rows: list[tuple[float, dict[str, Any]]] = []

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        ensure_upgrade_tables(conn)
        rows = conn.execute(
            "SELECT id, role, content, source_label, embedding_json, created_at FROM local_memory WHERE user_id = ?",
            (user_id,),
        ).fetchall()

    target_vec = list(embedding)
    for r in rows:
        vec_sim = 0.0
        if r["embedding_json"]:
            try:
                stored_vec = json.loads(r["embedding_json"])
                vec_sim = _cosine_similarity(target_vec, stored_vec)
            except Exception:
                vec_sim = 0.0
        norm_fts = (fts_scores.get(r["id"], 0.0) / max_fts) if query else 0.0
        if not query and r["embedding_json"] is None:
            continue
        combined = (norm_fts * 0.4 + vec_sim * 0.6) if query else vec_sim
        scored_rows.append(
            (
                combined,
                {
                    "id": r["id"],
                    "role": r["role"],
                    "content": r["content"],
                    "source_label": r["source_label"] or "",
                    "created_at": r["created_at"],
                    "vector_similarity": round(vec_sim, 6),
                    "fts_score": round(fts_scores.get(r["id"], 0.0), 6),
                    "backend": "local_sqlite_fts5",
                },
            )
        )

    scored_rows.sort(key=lambda item: item[0], reverse=True)
    return [item[1] for item in scored_rows[:limit]]


def local_delete_memory(db_path: Path, user_id: str, example_id: str) -> dict[str, Any]:
    """Delete a memory entry by UUID from local SQLite and FTS5 index."""
    with sqlite3.connect(db_path) as conn:
        ensure_upgrade_tables(conn)
        cur = conn.execute(
            "DELETE FROM local_memory WHERE id = ? AND user_id = ?",
            (example_id, user_id),
        )
        conn.execute("DELETE FROM local_memory_fts WHERE id = ?", (example_id,))
        conn.commit()
        deleted = cur.rowcount > 0
        return {
            "ok": deleted,
            "message": "Deleted from local SQLite memory." if deleted else "No matching example found.",
            "backend": "local_sqlite_fts5",
        }


def local_analyze_word_frequency(
    db_path: Path,
    user_id: str,
    limit: int,
    tokenizer: Callable[[str], list[str]],
) -> dict[str, Any]:
    """Compute vocabulary frequency over locally stored user messages."""
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        ensure_upgrade_tables(conn)
        rows = conn.execute(
            "SELECT content FROM local_memory WHERE user_id = ? AND role = 'user'",
            (user_id,),
        ).fetchall()

    counter: Counter[str] = Counter()
    for row in rows:
        counter.update(tokenizer(row["content"]))
    return {
        "ok": True,
        "messages_analyzed": len(rows),
        "top_terms": [{"word": word, "count": count} for word, count in counter.most_common(limit)],
        "backend": "local_sqlite_fts5",
    }


# ==============================================================================
# 2. Ved Chaos Codebase Digest & Context Packer (gitingest / repomix inspired)
# ==============================================================================


def _load_gitignore_patterns(root: Path) -> list[str]:
    """Load simple glob ignore patterns from .gitignore if present."""
    gitignore = root / ".gitignore"
    if not gitignore.is_file():
        return []
    patterns: list[str] = []
    for raw_line in gitignore.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        patterns.append(line.rstrip("/"))
    return patterns


def _should_ignore_path(rel_path: str, name: str, is_dir: bool, gitignore_patterns: list[str]) -> bool:
    """Decide whether a file or folder should be skipped during codebase ingestion."""
    if is_dir and name in DEFAULT_IGNORE_DIRS:
        return True
    if not is_dir and any(fnmatch.fnmatch(name, pat) for pat in DEFAULT_IGNORE_PATTERNS):
        return True
    norm_rel = rel_path.replace("\\", "/")
    for pat in gitignore_patterns:
        if fnmatch.fnmatch(name, pat) or fnmatch.fnmatch(norm_rel, pat):
            return True
    return False


def _render_ascii_tree(rel_paths: list[str]) -> str:
    """Build a compact ASCII tree from relative POSIX paths."""
    tree: dict[str, Any] = {}
    for p in sorted(rel_paths):
        node = tree
        for part in p.split("/"):
            node = node.setdefault(part, {})

    lines: list[str] = ["."]

    def _walk(subtree: dict[str, Any], prefix: str = "") -> None:
        items = list(subtree.items())
        for idx, (key, child) in enumerate(items):
            connector = "└── " if idx == len(items) - 1 else "├── "
            lines.append(f"{prefix}{connector}{key}{'/' if child else ''}")
            if child:
                ext = "    " if idx == len(items) - 1 else "│   "
                _walk(child, prefix + ext)

    _walk(tree)
    return "\n".join(lines)


def _format_digest_output(
    repo_label: str,
    tree_str: str,
    packed_files: list[dict[str, Any]],
    output_format: str,
) -> str:
    """Format packed repository tree and file contents in Markdown or XML."""
    if output_format == "xml":
        chunks = [f'<ved_chaos_digest repository="{repo_label}">', "<directory_tree>", tree_str, "</directory_tree>", "<files>"]
        for item in packed_files:
            chunks.append(f'<file path="{item["path"]}" lines="{item["lines"]}">\n{item["content"]}\n</file>')
        chunks.append("</files>\n</ved_chaos_digest>")
        return "\n".join(chunks)

    chunks = [f"# Ved Chaos Codebase Digest: `{repo_label}`", "", "## Directory Tree", "```text", tree_str, "```", "", "## Packed Files"]
    for item in packed_files:
        ext = Path(item["path"]).suffix.lstrip(".") or "text"
        chunks.append(f"\n### `{item['path']}` ({item['lines']} lines)\n```{ext}\n{item['content']}\n```")
    return "\n".join(chunks)


def _parse_github_target(target: str) -> tuple[str, str] | None:
    """Parse 'owner/repo' or 'https://github.com/owner/repo' into (owner, repo)."""
    cleaned = (target or "").strip().rstrip("/")
    if cleaned.startswith(("http://", "https://")):
        parsed = urlparse(cleaned)
        if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
            return None
        parts = [p for p in parsed.path.split("/") if p]
        if len(parts) >= 2:
            return parts[0], parts[1].removesuffix(".git")
        return None
    if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", cleaned):
        owner, repo = cleaned.split("/", 1)
        return owner, repo.removesuffix(".git")
    return None


async def _ingest_github_repo(
    owner: str,
    repo: str,
    max_files: int,
    max_total_chars: int,
    ext_filter: set[str],
    output_format: str,
    redact_secrets: bool,
) -> dict[str, Any]:
    """Fetch a public GitHub repository tree and pack top source files for LLM ingestion."""
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "VedChaosAI/0.4"}
    async with httpx.AsyncClient(timeout=10.0, follow_redirects=True, headers=headers) as client:
        meta_resp = await client.get(f"https://api.github.com/repos/{owner}/{repo}")
        if meta_resp.status_code != 200:
            return {"ok": False, "error": f"GitHub repository lookup failed (HTTP {meta_resp.status_code})."}
        meta = meta_resp.json()
        branch = meta.get("default_branch", "main")

        tree_resp = await client.get(f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1")
        if tree_resp.status_code != 200:
            return {"ok": False, "error": f"GitHub tree fetch failed (HTTP {tree_resp.status_code})."}
        tree_items = tree_resp.json().get("tree", [])

        candidate_paths: list[str] = []
        for entry in tree_items:
            if entry.get("type") != "blob":
                continue
            rel = entry.get("path", "")
            parts = rel.split("/")
            if any(p in DEFAULT_IGNORE_DIRS for p in parts[:-1]):
                continue
            fname = parts[-1]
            if any(fnmatch.fnmatch(fname, pat) for pat in DEFAULT_IGNORE_PATTERNS):
                continue
            if ext_filter and Path(fname).suffix.lower() not in ext_filter:
                continue
            if (entry.get("size") or 0) > 120_000:
                continue
            candidate_paths.append(rel)

        selected_paths = candidate_paths[:max_files]
        packed_files: list[dict[str, Any]] = []
        total_chars = 0
        total_redactions = 0

        for rel in selected_paths:
            if total_chars >= max_total_chars:
                break
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{rel}"
            file_resp = await client.get(raw_url)
            if file_resp.status_code != 200 or b"\x00" in file_resp.content[:1024]:
                continue
            text = file_resp.text
            if redact_secrets:
                text, redacted = _redact_secrets_in_text(text)
                total_redactions += redacted
            remaining = max_total_chars - total_chars
            if len(text) > remaining:
                text = text[:remaining] + "\n... [TRUNCATED BY VED CHAOS BUDGET]"
            packed_files.append({"path": rel, "lines": text.count("\n") + 1, "content": text})
            total_chars += len(text)

    tree_str = _render_ascii_tree([f["path"] for f in packed_files] or selected_paths[:max_files])
    digest = _format_digest_output(f"{owner}/{repo}@{branch}", tree_str, packed_files, output_format)
    return {
        "ok": True,
        "branded_by": f"{VED_BRAND} Codebase Ingestor",
        "source_type": "github_remote",
        "repository": f"{owner}/{repo}",
        "branch": branch,
        "stars": meta.get("stargazers_count", 0),
        "license": (meta.get("license") or {}).get("spdx_id", "Unknown"),
        "files_packed": len(packed_files),
        "total_chars": len(digest),
        "estimated_tokens": max(1, len(digest) // 4),
        "secrets_redacted": total_redactions,
        "output_format": output_format,
        "digest": digest,
    }


async def ingest_codebase_digest(
    target: str = ".",
    max_files: int = 60,
    max_total_chars: int = 80000,
    include_extensions: list[str] | None = None,
    output_format: str = "markdown",
    redact_secrets: bool = True,
) -> dict[str, Any]:
    """Pack a local directory or public GitHub repository into a clean LLM-ready digest."""
    max_files = max(1, min(int(max_files), 200))
    max_total_chars = max(1000, min(int(max_total_chars), 250000))
    fmt = (output_format or "markdown").strip().lower()
    if fmt not in {"markdown", "xml"}:
        fmt = "markdown"
    ext_filter = {
        (e if e.startswith(".") else f".{e}").lower()
        for e in (include_extensions or [])
        if e and e.strip()
    }

    gh_spec = _parse_github_target(target)
    local_candidate = Path(target)
    if gh_spec and not local_candidate.exists():
        try:
            return await _ingest_github_repo(
                gh_spec[0], gh_spec[1], max_files, max_total_chars, ext_filter, fmt, redact_secrets
            )
        except Exception as exc:
            return {"ok": False, "error": f"GitHub ingestion failed: {exc}"}

    root = local_candidate.resolve()
    if not root.exists() or not root.is_dir():
        return {"ok": False, "error": f"Target directory does not exist: {target}"}
    if _is_blocked_system_root(root):
        return {"ok": False, "error": "Safety policy blocked ingestion of OS system directory."}

    gitignore_patterns = _load_gitignore_patterns(root)
    packed_files: list[dict[str, Any]] = []
    rel_tree_paths: list[str] = []
    total_chars = 0
    total_redactions = 0

    for dirpath, dirnames, filenames in os.walk(root):
        cur_dir = Path(dirpath)
        dirnames[:] = sorted(
            d for d in dirnames
            if not _should_ignore_path(str((cur_dir / d).relative_to(root)), d, True, gitignore_patterns)
        )
        for fname in sorted(filenames):
            fpath = cur_dir / fname
            rel_posix = fpath.relative_to(root).as_posix()
            if _should_ignore_path(rel_posix, fname, False, gitignore_patterns):
                continue
            if ext_filter and fpath.suffix.lower() not in ext_filter:
                continue
            rel_tree_paths.append(rel_posix)
            if len(packed_files) >= max_files or total_chars >= max_total_chars:
                continue
            try:
                raw_bytes = fpath.read_bytes()
            except OSError:
                continue
            if b"\x00" in raw_bytes[:1024] or len(raw_bytes) > 250_000:
                continue
            text = raw_bytes.decode("utf-8", errors="replace")
            if redact_secrets:
                text, redacted = _redact_secrets_in_text(text)
                total_redactions += redacted
            remaining = max_total_chars - total_chars
            if len(text) > remaining:
                text = text[:remaining] + "\n... [TRUNCATED BY VED CHAOS BUDGET]"
            packed_files.append({"path": rel_posix, "lines": text.count("\n") + 1, "content": text})
            total_chars += len(text)

    tree_str = _render_ascii_tree(rel_tree_paths)
    digest = _format_digest_output(root.name, tree_str, packed_files, fmt)
    return {
        "ok": True,
        "branded_by": f"{VED_BRAND} Codebase Ingestor",
        "source_type": "local_filesystem",
        "root": str(root),
        "files_discovered": len(rel_tree_paths),
        "files_packed": len(packed_files),
        "total_chars": len(digest),
        "estimated_tokens": max(1, len(digest) // 4),
        "secrets_redacted": total_redactions,
        "output_format": fmt,
        "digest": digest,
    }


# ==============================================================================
# 3. Ved Chaos Supply-Chain & Entropy Secret Auditor (osv-scanner inspired)
# ==============================================================================


def _parse_dependencies_from_workspace(root: Path) -> list[dict[str, str]]:
    """Extract PyPI and npm package declarations from workspace manifests."""
    deps: list[dict[str, str]] = []

    req_file = root / "requirements.txt"
    if req_file.is_file():
        for raw in req_file.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.split("#", 1)[0].strip()
            if not line or line.startswith("-"):
                continue
            m = re.match(r"^([A-Za-z0-9_.\-]+)(?:\[[^\]]+\])?\s*(?:==\s*([A-Za-z0-9_.\-]+))?", line)
            if m:
                deps.append({"ecosystem": "PyPI", "name": m.group(1), "version": m.group(2) or "", "manifest": "requirements.txt"})

    pyproject_file = root / "pyproject.toml"
    if pyproject_file.is_file():
        try:
            data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))
            for spec in data.get("project", {}).get("dependencies", []):
                m = re.match(r"^([A-Za-z0-9_.\-]+)(?:\[[^\]]+\])?\s*(?:==\s*([A-Za-z0-9_.\-]+))?", str(spec).strip())
                if m and not any(d["name"].lower() == m.group(1).lower() and d["ecosystem"] == "PyPI" for d in deps):
                    deps.append({"ecosystem": "PyPI", "name": m.group(1), "version": m.group(2) or "", "manifest": "pyproject.toml"})
        except Exception:
            pass

    pkg_json = root / "package.json"
    if pkg_json.is_file():
        try:
            data = json.loads(pkg_json.read_text(encoding="utf-8"))
            for section in ("dependencies", "devDependencies"):
                for pkg_name, ver in (data.get(section) or {}).items():
                    clean_ver = re.sub(r"^[\^~>=< ]+", "", str(ver).strip())
                    deps.append({"ecosystem": "npm", "name": pkg_name, "version": clean_ver, "manifest": "package.json"})
        except Exception:
            pass

    return deps


async def _query_osv_batch(pinned_deps: list[dict[str, str]]) -> tuple[list[dict[str, Any]], bool]:
    """Query OSV.dev batch API for known CVEs across pinned dependencies."""
    if not pinned_deps:
        return [], False
    queries = [
        {"package": {"name": d["name"], "ecosystem": d["ecosystem"]}, "version": d["version"]}
        for d in pinned_deps
    ]
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.post("https://api.osv.dev/v1/querybatch", json={"queries": queries})
            if resp.status_code != 200:
                return [], False
            results = resp.json().get("results", [])
            vulns_found: list[dict[str, Any]] = []
            for dep, res in zip(pinned_deps, results):
                for v in res.get("vulns", [])[:5]:
                    vulns_found.append({
                        "package": dep["name"],
                        "version": dep["version"],
                        "ecosystem": dep["ecosystem"],
                        "advisory_id": v.get("id", "UNKNOWN"),
                        "summary": v.get("summary") or "Vulnerability reported in OSV.dev database",
                    })
            return vulns_found, True
    except Exception:
        return [], False


def _scan_workspace_secrets(root: Path, max_files: int = 120) -> list[dict[str, Any]]:
    """Scan workspace files for hardcoded secret patterns and high-entropy token literals."""
    findings: list[dict[str, Any]] = []
    scanned = 0
    for dirpath, dirnames, filenames in os.walk(root):
        cur_dir = Path(dirpath)
        dirnames[:] = [d for d in dirnames if d not in DEFAULT_IGNORE_DIRS and d != "tests"]
        for fname in filenames:
            if scanned >= max_files:
                return findings
            fpath = cur_dir / fname
            if any(fnmatch.fnmatch(fname, pat) for pat in DEFAULT_IGNORE_PATTERNS):
                continue
            if fname in {".env.example"}:
                continue
            try:
                raw = fpath.read_bytes()
            except OSError:
                continue
            if b"\x00" in raw[:512] or len(raw) > 150_000:
                continue
            scanned += 1
            rel = fpath.relative_to(root).as_posix()
            lines = raw.decode("utf-8", errors="ignore").splitlines()
            for lineno, line in enumerate(lines, start=1):
                for rule_name, pattern, severity in SENSITIVE_SECRET_RULES:
                    if re.search(pattern, line):
                        findings.append({
                            "file": rel,
                            "line": lineno,
                            "rule": rule_name,
                            "severity": severity,
                            "detection_method": "pattern_match",
                        })
                        break
                else:
                    for quoted in re.findall(r"['\"]([A-Za-z0-9+/=_\-]{24,80})['\"]", line):
                        if "/" in quoted or " " in quoted:
                            continue
                        entropy = _shannon_entropy(quoted)
                        if entropy >= 4.35:
                            findings.append({
                                "file": rel,
                                "line": lineno,
                                "rule": "High-Entropy Secret Candidate",
                                "severity": "Medium",
                                "entropy": round(entropy, 2),
                                "detection_method": "shannon_entropy",
                            })
                            break
    return findings


async def scan_supply_chain_security(
    workspace_path: str = ".",
    check_live_osv: bool = True,
) -> dict[str, Any]:
    """Audit workspace dependencies via OSV.dev and scan files for leaked/high-entropy secrets."""
    root = Path(workspace_path).resolve()
    if not root.exists() or not root.is_dir():
        return {"ok": False, "error": f"Workspace path does not exist: {workspace_path}"}
    if _is_blocked_system_root(root):
        return {"ok": False, "error": "Safety policy blocked scanning OS system directory."}

    deps = _parse_dependencies_from_workspace(root)
    pinned_deps = [d for d in deps if d["version"]]
    osv_vulns: list[dict[str, Any]] = []
    osv_live = False
    if check_live_osv and pinned_deps:
        osv_vulns, osv_live = await _query_osv_batch(pinned_deps)

    secret_findings = _scan_workspace_secrets(root)
    critical_or_high = any(s["severity"] in {"Critical", "High"} for s in secret_findings) or len(osv_vulns) > 0

    if not osv_vulns and not secret_findings:
        grade = "A+ (SECURE)"
    elif critical_or_high:
        grade = "F (ACTION REQUIRED)"
    else:
        grade = "B (HARDENING RECOMMENDED)"

    return {
        "ok": True,
        "branded_by": f"{VED_BRAND} Supply-Chain Shield",
        "workspace": str(root),
        "security_grade": grade,
        "dependencies_discovered": len(deps),
        "pinned_dependencies_checked": len(pinned_deps),
        "osv_live_checked": osv_live,
        "dependency_vulnerabilities_count": len(osv_vulns),
        "dependency_vulnerabilities": osv_vulns,
        "secret_findings_count": len(secret_findings),
        "secret_findings": secret_findings[:50],
        "dependencies": deps,
    }


# ==============================================================================
# 4. Ved Chaos Persistent Thought Chain (sequential-thinking inspired)
# ==============================================================================


def manage_reasoning_chain(
    db_path: Path,
    action: str = "add_step",
    chain_id: str = "",
    title: str = "",
    thought: str = "",
    thought_number: int = 1,
    total_thoughts: int = 3,
    confidence: float = 0.8,
    is_revision: bool = False,
    revises_step: int | None = None,
    branch_from_step: int | None = None,
    decision: str = "",
) -> dict[str, Any]:
    """Persistently record, revise, branch, and conclude multi-step reasoning chains in SQLite."""
    act = (action or "add_step").strip().lower()
    now_str = datetime.datetime.now(datetime.timezone.utc).isoformat()

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        ensure_upgrade_tables(conn)

        if act == "list_chains":
            rows = conn.execute(
                """
                SELECT c.chain_id, c.title, c.status, c.final_decision, c.created_at, c.updated_at,
                       COUNT(s.id) AS steps_count
                FROM reasoning_chains c
                LEFT JOIN reasoning_steps s ON s.chain_id = c.chain_id
                GROUP BY c.chain_id
                ORDER BY c.updated_at DESC
                LIMIT 25
                """
            ).fetchall()
            return {
                "ok": True,
                "branded_by": f"{VED_BRAND} Thought Chain",
                "chains": [dict(r) for r in rows],
            }

        if act == "get_chain":
            if not chain_id:
                return {"ok": False, "error": "chain_id is required for get_chain"}
            chain = conn.execute("SELECT * FROM reasoning_chains WHERE chain_id = ?", (chain_id,)).fetchone()
            if not chain:
                return {"ok": False, "error": f"Reasoning chain '{chain_id}' not found"}
            steps = conn.execute(
                "SELECT * FROM reasoning_steps WHERE chain_id = ? ORDER BY step_number ASC, created_at ASC",
                (chain_id,),
            ).fetchall()
            return {
                "ok": True,
                "branded_by": f"{VED_BRAND} Thought Chain",
                "chain": dict(chain),
                "steps": [dict(s) for s in steps],
            }

        if act == "conclude":
            if not chain_id:
                return {"ok": False, "error": "chain_id is required for conclude"}
            cur = conn.execute(
                "UPDATE reasoning_chains SET status = 'CONCLUDED', final_decision = ?, updated_at = ? WHERE chain_id = ?",
                ((decision or "").strip(), now_str, chain_id),
            )
            conn.commit()
            if cur.rowcount == 0:
                return {"ok": False, "error": f"Reasoning chain '{chain_id}' not found"}
            return {
                "ok": True,
                "branded_by": f"{VED_BRAND} Thought Chain",
                "chain_id": chain_id,
                "status": "CONCLUDED",
                "final_decision": (decision or "").strip(),
            }

        if act == "add_step":
            clean_thought = (thought or "").strip()
            if not clean_thought:
                return {"ok": False, "error": "thought cannot be empty"}
            cid = (chain_id or "").strip() or f"chain-{uuid.uuid4().hex[:8]}"
            clean_title = (title or "").strip() or f"Ved Chaos Reasoning ({cid})"
            clamped_conf = max(0.0, min(1.0, float(confidence)))

            conn.execute(
                """
                INSERT INTO reasoning_chains (chain_id, title, status, final_decision, created_at, updated_at)
                VALUES (?, ?, 'ACTIVE', '', ?, ?)
                ON CONFLICT(chain_id) DO UPDATE SET updated_at = excluded.updated_at
                """,
                (cid, clean_title, now_str, now_str),
            )
            step_id = f"step-{uuid.uuid4().hex[:8]}"
            conn.execute(
                """
                INSERT INTO reasoning_steps (
                    id, chain_id, step_number, total_thoughts, thought, confidence,
                    is_revision, revises_step, branch_from_step, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    step_id,
                    cid,
                    int(thought_number),
                    max(int(thought_number), int(total_thoughts)),
                    clean_thought,
                    clamped_conf,
                    1 if is_revision else 0,
                    revises_step,
                    branch_from_step,
                    now_str,
                ),
            )
            conn.commit()
            return {
                "ok": True,
                "branded_by": f"{VED_BRAND} Thought Chain",
                "chain_id": cid,
                "step_id": step_id,
                "step_number": int(thought_number),
                "total_thoughts": max(int(thought_number), int(total_thoughts)),
                "confidence": clamped_conf,
                "next_thought_needed": int(thought_number) < int(total_thoughts),
            }

        return {"ok": False, "error": f"Unknown action '{action}'. Use add_step, get_chain, list_chains, or conclude."}


# ==============================================================================
# 5. Ved Chaos GitHub Radar & Upgrade Scout (mcp-github-trending inspired)
# ==============================================================================


CURATED_GITHUB_FALLBACK = [
    {
        "full_name": "cyclotruc/gitingest",
        "stars": 9500,
        "language": "Python",
        "license": "MIT",
        "ved_compatibility": "permissive_safe",
        "description": "Turn any Git repository into a simple text digest of its codebase for LLMs.",
        "url": "https://github.com/cyclotruc/gitingest",
    },
    {
        "full_name": "google/osv-scanner",
        "stars": 7200,
        "language": "Go",
        "license": "Apache-2.0",
        "ved_compatibility": "permissive_safe",
        "description": "Vulnerability scanner written in Go which uses the data provided by https://osv.dev.",
        "url": "https://github.com/google/osv-scanner",
    },
    {
        "full_name": "tadata-org/fastapi_mcp",
        "stars": 6500,
        "language": "Python",
        "license": "MIT",
        "ved_compatibility": "permissive_safe",
        "description": "Expose your FastAPI endpoints as Model Context Protocol (MCP) tools with zero configuration.",
        "url": "https://github.com/tadata-org/fastapi_mcp",
    },
]


async def scout_github_upgrades(
    topic_or_query: str = "mcp server",
    language: str = "python",
    min_stars: int = 50,
    limit: int = 8,
) -> dict[str, Any]:
    """Search GitHub repositories and evaluate license + architecture fit for Ved Chaos AI."""
    limit = max(1, min(int(limit), 20))
    min_stars = max(0, int(min_stars))
    q_parts = [(topic_or_query or "mcp server").strip()]
    if language and language.strip():
        q_parts.append(f"language:{language.strip().lower()}")
    if min_stars > 0:
        q_parts.append(f"stars:>={min_stars}")
    query_str = " ".join(q_parts)

    headers = {"Accept": "application/vnd.github+json", "User-Agent": "VedChaosAI/0.4"}
    try:
        async with httpx.AsyncClient(timeout=8.0, headers=headers) as client:
            resp = await client.get(
                "https://api.github.com/search/repositories",
                params={"q": query_str, "sort": "stars", "order": "desc", "per_page": limit},
            )
            if resp.status_code == 200:
                items = resp.json().get("items", [])
                discovered: list[dict[str, Any]] = []
                for repo in items[:limit]:
                    spdx = (repo.get("license") or {}).get("spdx_id") or "Unknown"
                    compat = "permissive_safe" if spdx in PERMISSIVE_LICENSES else "review_license"
                    discovered.append({
                        "full_name": repo.get("full_name", ""),
                        "stars": repo.get("stargazers_count", 0),
                        "forks": repo.get("forks_count", 0),
                        "language": repo.get("language") or "Unknown",
                        "license": spdx,
                        "ved_compatibility": compat,
                        "topics": (repo.get("topics") or [])[:6],
                        "description": (repo.get("description") or "")[:240],
                        "url": repo.get("html_url", ""),
                        "updated_at": repo.get("updated_at", ""),
                    })
                return {
                    "ok": True,
                    "branded_by": f"{VED_BRAND} GitHub Radar",
                    "is_live": True,
                    "query": query_str,
                    "total_found": len(discovered),
                    "repositories": discovered,
                }
    except Exception:
        pass

    return {
        "ok": True,
        "branded_by": f"{VED_BRAND} GitHub Radar",
        "is_live": False,
        "query": query_str,
        "total_found": len(CURATED_GITHUB_FALLBACK[:limit]),
        "repositories": CURATED_GITHUB_FALLBACK[:limit],
        "note": "Offline or rate-limited fallback catalog returned.",
    }

