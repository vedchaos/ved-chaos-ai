import asyncio
from main import (
    analyze_trading_technical_setup,
    calculate_position_risk_management,
    execute_paper_trade,
    PAPER_PORTFOLIO,
)

def test_calculate_position_risk_management():
    # Account: $10,000, 1% risk ($100), Entry: $100, Stop: $95 ($5 risk/unit) -> 20 units
    res = asyncio.run(calculate_position_risk_management(
        account_balance_usd=10000.0,
        risk_percentage=1.0,
        entry_price=100.0,
        stop_loss_price=95.0,
        target_profit_price=115.0,
    ))
    assert res["ok"] is True
    assert res["max_capital_at_risk_usd"] == 100.0
    assert res["recommended_units"] == 20.0
    assert res["total_position_size_usd"] == 2000.0
    assert res["risk_reward_ratio"] == "1:3.0"
    assert "EXCELLENT R:R SETUP" in res["verdict"]

def test_analyze_trading_technical_setup():
    candles = [100.0, 102.0, 104.0, 103.0, 106.0, 108.0, 110.0, 112.0]
    res = asyncio.run(analyze_trading_technical_setup(ticker="BTC/USDT", prices=candles, timeframe="4h"))
    assert res["ok"] is True
    assert res["ticker"] == "BTC/USDT"
    assert "indicators" in res
    assert "sma_fast" in res["indicators"]
    assert "rsi_14_estimate" in res["indicators"]
    assert "market_bias" in res
    assert res["support_level"] == 100.0
    assert res["resistance_level"] == 112.0

def test_execute_paper_trade_execution():
    initial_balance = PAPER_PORTFOLIO["virtual_balance_usd"]
    buy_res = asyncio.run(execute_paper_trade(
        action="BUY",
        ticker="SOL/USDT",
        quantity=2.0,
        price=150.0,
    ))
    assert buy_res["ok"] is True
    assert buy_res["virtual_balance_remaining_usd"] == initial_balance - 300.0
    assert buy_res["active_positions_count"] >= 1
    assert buy_res["trade_executed"]["ticker"] == "SOL/USDT"
