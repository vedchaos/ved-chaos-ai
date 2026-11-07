import asyncio
from main import scan_direct_bounties, fetch_latest_intelligence, deep_research_dossier

def test_scan_direct_bounties_schema_and_execution():
    res = asyncio.run(scan_direct_bounties(platform="all", min_budget_usd=20.0, keyword="python"))
    assert res["ok"] is True
    assert "bounties" in res
    assert isinstance(res["bounties"], list)
    assert len(res["bounties"]) > 0

    first = res["bounties"][0]
    assert "title" in first
    assert "budget_usd" in first
    assert "source" in first
    assert "client_contact" in first
    assert "tech_tags" in first
    assert first["budget_usd"] >= 20.0

def test_fetch_latest_intelligence_structure():
    res = asyncio.run(fetch_latest_intelligence(category="ai_tech", query="", limit=5))
    assert res["ok"] is True
    assert "intelligence" in res
    assert isinstance(res["intelligence"], list)
    assert len(res["intelligence"]) > 0

    item = res["intelligence"][0]
    assert "title" in item
    assert "summary" in item
    assert "url" in item or "verification_source" in item

def test_deep_research_dossier_structure():
    res = asyncio.run(deep_research_dossier(topic="Zero-Trust Authentication in FastMCP", research_depth="comprehensive"))
    assert res["ok"] is True
    assert res["domain"] == "CYBERSECURITY & DEFENSIVE ENGINEERING"
    assert "EXECUTIVE INTELLIGENCE DOSSIER" in res["dossier"]
    assert "Technical Mechanisms & Architecture" in res["dossier"]
    assert "Threat Modeling & Vulnerability Surface" in res["dossier"]
