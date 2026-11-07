import asyncio
import tempfile
from pathlib import Path
from main import inspect_url_safety, inspect_file_threat

def test_inspect_url_safety_flags_phishing_and_payloads():
    # 1. Lookalike domain targeting PayPal
    res_phish = asyncio.run(inspect_url_safety("https://paypa1-security-verification.xyz/login"))
    assert res_phish["ok"] is True
    assert res_phish["is_safe"] is False
    assert res_phish["risk_score"] >= 60
    assert any("typosquatting" in f.lower() for f in res_phish["findings"])

    # 2. Dangerous executable download trap
    res_exe = asyncio.run(inspect_url_safety("https://legit-files.com/downloads/setup_updater.scr"))
    assert res_exe["ok"] is True
    assert res_exe["is_safe"] is False
    assert any("executable binary payload" in f.lower() for f in res_exe["findings"])

    # 3. Clean official URL
    res_clean = asyncio.run(inspect_url_safety("https://python.org"))
    assert res_clean["ok"] is True
    assert res_clean["is_safe"] is True
    assert res_clean["risk_score"] < 30

def test_inspect_file_threat_detects_malicious_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 1. Double extension test (invoice.pdf.exe)
        double_ext_file = tmp_path / "invoice.pdf.exe"
        double_ext_file.write_bytes(b"MZfakebinarycontent")
        res_double = asyncio.run(inspect_file_threat(str(double_ext_file)))
        assert res_double["ok"] is True
        assert res_double["is_safe"] is False
        assert res_double["risk_score"] >= 70
        assert any("Double extension" in f for f in res_double["findings"])

        # 2. Masquerading file (named clean.pdf but starting with MZ PE header)
        masq_file = tmp_path / "clean_document.pdf"
        masq_file.write_bytes(b"MZ\x90\x00\x03\x00\x00\x00")
        res_masq = asyncio.run(inspect_file_threat(str(masq_file)))
        assert res_masq["ok"] is True
        assert res_masq["is_safe"] is False
        assert any("Windows PE executable" in f for f in res_masq["findings"])
        assert res_masq["quarantine_recommended"] is True

        # 3. Clean legitimate text file
        clean_file = tmp_path / "normal_notes.txt"
        clean_file.write_text("Hello this is a regular clean text file.", encoding="utf-8")
        res_clean = asyncio.run(inspect_file_threat(str(clean_file)))
        assert res_clean["ok"] is True
        assert res_clean["is_safe"] is True
        assert res_clean["risk_score"] == 0
        assert res_clean["sha256"] != ""

