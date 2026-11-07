import asyncio
from main import audit_code_vulnerabilities

def test_ast_detects_sqli_in_execute():
    insecure_code = """
import asyncpg
async def query_user(conn, user_name):
    query = f"SELECT * FROM users WHERE name = '{user_name}'"
    return await conn.execute(f"SELECT * FROM users WHERE name = '{user_name}'")
"""
    res = asyncio.run(audit_code_vulnerabilities(insecure_code, language="python"))
    assert res["passed_audit"] is False
    assert res["vulnerabilities_found"] >= 1
    vulns = [v["vulnerability"] for v in res["vulnerability_details"]]
    assert any("SQL Injection via f-string" in v for v in vulns)

def test_ast_detects_command_injection():
    insecure_code = """
import os
import subprocess
def run_backup(path):
    os.system("tar -czf backup.tar.gz " + path)
    subprocess.call("echo done", shell=True)
"""
    res = asyncio.run(audit_code_vulnerabilities(insecure_code, language="python"))
    assert res["passed_audit"] is False
    vulns = [v["vulnerability"] for v in res["vulnerability_details"]]
    assert any("Command Injection Vector via os.system" in v for v in vulns)
    assert any("Shell Injection in subprocess with shell=True" in v for v in vulns)

def test_ast_detects_eval_and_pickle():
    insecure_code = """
import pickle
def execute_dynamic(serialized_data, formula):
    data = pickle.loads(serialized_data)
    return eval(formula)
"""
    res = asyncio.run(audit_code_vulnerabilities(insecure_code, language="python"))
    assert res["passed_audit"] is False
    vulns = [v["vulnerability"] for v in res["vulnerability_details"]]
    assert any("Insecure Deserialization via pickle" in v for v in vulns)
    assert any("Arbitrary Code Execution via eval" in v for v in vulns)

def test_clean_parameterized_code_passes():
    clean_code = """
import subprocess
async def safe_fetch(conn, user_id: int):
    # Parameterized query with bound parameters
    return await conn.fetch("SELECT id, name FROM users WHERE id = $1", user_id)

def safe_process_runner(filename: str):
    return subprocess.run(["python", "-m", "worker", "--file", filename], shell=False, check=True)
"""
    res = asyncio.run(audit_code_vulnerabilities(clean_code, language="python"))
    assert res["passed_audit"] is True
    assert res["security_grade"] == "A+ (SECURE)"
    assert res["vulnerabilities_found"] == 0

