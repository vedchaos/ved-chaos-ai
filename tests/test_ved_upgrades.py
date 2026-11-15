import asyncio
import main
from main import (
    analyze_word_frequency,
    delete_chat_example,
    hybrid_search_memory,
    save_chat_example,
    search_chat_history,
    ved_get_capabilities_manifest,
    ved_ingest_codebase,
    ved_manage_reasoning_chain,
    ved_scan_supply_chain,
    ved_scout_github_upgrades,
)


def test_local_sqlite_fts5_hybrid_memory_lifecycle(tmp_path):
    orig_db = main.STATE_DB_PATH
    orig_url = main.DATABASE_URL
    orig_pin = main.SECURITY_PIN
    orig_phrase = main.ACTIVATION_PHRASE
    main.STATE_DB_PATH = tmp_path / "test_memory.db"
    main.DATABASE_URL = ""
    main.SECURITY_PIN = "2519"
    main.ACTIVATION_PHRASE = "chaos protocol"
    main._failed_attempts = 0
    main._lockout_until = 0.0

    try:
        vec_a = [1.0] + [0.0] * 1535
        vec_b = [0.0, 1.0] + [0.0] * 1534

        res1 = asyncio.run(
            save_chat_example(
                role="user",
                content="bhai fastapi backend aur sqlite fts5 memory mast chal rahi hai",
                source_label="upgrade-test",
                embedding=vec_a,
                security_pin="2519",
                activation_phrase="chaos protocol",
            )
        )
        assert res1["ok"] is True
        assert res1["backend"] == "local_sqlite_fts5"

        # Deduplication check
        res1_dup = asyncio.run(
            save_chat_example(
                role="user",
                content="bhai fastapi backend aur sqlite fts5 memory mast chal rahi hai",
                source_label="upgrade-test-2",
                security_pin="2519",
                activation_phrase="chaos protocol",
            )
        )
        assert res1_dup["ok"] is True
        assert res1_dup["deduplicated"] is True
        assert res1_dup["id"] == res1["id"]

        res2 = asyncio.run(
            save_chat_example(
                role="assistant",
                content="quantum wormhole physics simulation ready",
                source_label="physics",
                embedding=vec_b,
                security_pin="2519",
                activation_phrase="chaos protocol",
            )
        )
        assert res2["ok"] is True

        # FTS5 search
        hits = asyncio.run(
            search_chat_history(
                query="fastapi sqlite",
                limit=5,
                security_pin="2519",
                activation_phrase="chaos protocol",
            )
        )
        assert len(hits) >= 1
        assert "fastapi" in hits[0]["content"]
        assert hits[0]["backend"] == "local_sqlite_fts5"

        # Hybrid vector + FTS search should rank vec_b highest for vec_b query
        hybrid_hits = asyncio.run(
            hybrid_search_memory(
                query="",
                embedding=vec_b,
                limit=2,
                security_pin="2519",
                activation_phrase="chaos protocol",
            )
        )
        assert len(hybrid_hits) == 2
        assert hybrid_hits[0]["id"] == res2["id"]
        assert hybrid_hits[0]["vector_similarity"] > 0.99

        # Word frequency
        freq = asyncio.run(
            analyze_word_frequency(
                limit=10,
                security_pin="2519",
                activation_phrase="chaos protocol",
            )
        )
        assert freq["ok"] is True
        assert freq["messages_analyzed"] == 1
        assert any(item["word"] == "fastapi" for item in freq["top_terms"])

        # Delete
        del_res = asyncio.run(
            delete_chat_example(
                example_id=res1["id"],
                security_pin="2519",
                activation_phrase="chaos protocol",
            )
        )
        assert del_res["ok"] is True
    finally:
        main.STATE_DB_PATH = orig_db
        main.DATABASE_URL = orig_url
        main.SECURITY_PIN = orig_pin
        main.ACTIVATION_PHRASE = orig_phrase


def test_ved_ingest_codebase_local_and_redaction(tmp_path):
    (tmp_path / ".gitignore").write_text("ignored_dir/\n*.log\n", encoding="utf-8")
    (tmp_path / "ignored_dir").mkdir()
    (tmp_path / "ignored_dir" / "skip.py").write_text("print('skip')", encoding="utf-8")
    (tmp_path / "app.log").write_text("noise", encoding="utf-8")
    (tmp_path / "binary.bin").write_bytes(b"\x00\x01\x02\x03")
    (tmp_path / "app.py").write_text(
        'OPENAI_KEY = "sk-testsecretkeyvalue1234567890abcdef"\nprint("hello ved chaos")\n',
        encoding="utf-8",
    )

    md_res = asyncio.run(ved_ingest_codebase(target=str(tmp_path), output_format="markdown", redact_secrets=True))
    assert md_res["ok"] is True
    assert md_res["branded_by"] == "Ved Chaos AI Codebase Ingestor"
    assert md_res["files_packed"] == 2  # .gitignore + app.py
    assert md_res["secrets_redacted"] >= 1
    assert "[REDACTED_BY_VED_CHAOS_SHIELD]" in md_res["digest"]
    assert "skip.py" not in md_res["digest"]
    assert "binary.bin" not in md_res["digest"]

    xml_res = asyncio.run(ved_ingest_codebase(target=str(tmp_path), output_format="xml", include_extensions=[".py"]))
    assert xml_res["ok"] is True
    assert "<ved_chaos_digest" in xml_res["digest"]
    assert xml_res["files_packed"] == 1


def test_ved_scan_supply_chain_offline_and_secrets(tmp_path):
    (tmp_path / "requirements.txt").write_text("fastapi==0.115.0\nhttpx==0.27.2\n", encoding="utf-8")
    (tmp_path / "package.json").write_text('{"dependencies": {"axios": "^1.7.0"}}', encoding="utf-8")
    (tmp_path / "config.py").write_text(
        'GITHUB_PAT = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"\n',
        encoding="utf-8",
    )

    res = asyncio.run(ved_scan_supply_chain(workspace_path=str(tmp_path), check_live_osv=False))
    assert res["ok"] is True
    assert res["branded_by"] == "Ved Chaos AI Supply-Chain Shield"
    assert res["dependencies_discovered"] == 3
    assert res["secret_findings_count"] >= 1
    assert res["security_grade"].startswith("F")


def test_ved_manage_reasoning_chain_persistence(tmp_path):
    orig_db = main.STATE_DB_PATH
    main.STATE_DB_PATH = tmp_path / "test_reasoning.db"
    try:
        step1 = asyncio.run(
            ved_manage_reasoning_chain(
                action="add_step",
                title="Upgrade Ved Chaos AI",
                thought="Add SQLite FTS5 fallback so memory works offline",
                thought_number=1,
                total_thoughts=2,
                confidence=0.92,
            )
        )
        assert step1["ok"] is True
        cid = step1["chain_id"]
        assert step1["next_thought_needed"] is True

        step2 = asyncio.run(
            ved_manage_reasoning_chain(
                action="add_step",
                chain_id=cid,
                thought="Add GitHub codebase digest & supply-chain shield",
                thought_number=2,
                total_thoughts=2,
                confidence=0.95,
            )
        )
        assert step2["ok"] is True
        assert step2["next_thought_needed"] is False

        conclude_res = asyncio.run(
            ved_manage_reasoning_chain(
                action="conclude",
                chain_id=cid,
                decision="Ship Ved Chaos AI v0.4.0 with 5 GitHub-inspired upgrades",
            )
        )
        assert conclude_res["ok"] is True
        assert conclude_res["status"] == "CONCLUDED"

        chain_data = asyncio.run(ved_manage_reasoning_chain(action="get_chain", chain_id=cid))
        assert chain_data["ok"] is True
        assert len(chain_data["steps"]) == 2
        assert chain_data["chain"]["status"] == "CONCLUDED"

        list_data = asyncio.run(ved_manage_reasoning_chain(action="list_chains"))
        assert list_data["ok"] is True
        assert any(c["chain_id"] == cid for c in list_data["chains"])
    finally:
        main.STATE_DB_PATH = orig_db


def test_ved_capabilities_manifest_and_github_radar():
    manifest = asyncio.run(ved_get_capabilities_manifest())
    assert manifest["ok"] is True
    assert manifest["name"] == "Ved Chaos AI"
    assert manifest["version"] == "0.4.0"
    assert manifest["total_mcp_tools"] == 41

    radar = asyncio.run(ved_scout_github_upgrades(topic_or_query="mcp", language="python", min_stars=100, limit=3))
    assert radar["ok"] is True
    assert radar["branded_by"] == "Ved Chaos AI GitHub Radar"
    assert radar["total_found"] >= 1
    assert "ved_compatibility" in radar["repositories"][0]

