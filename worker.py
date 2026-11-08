"""Ved Chaos AI - 24/7 Background Runner Daemon & Telemetry Engine.
Monitors direct zero-commission engineering bounties, processes automated micro-tasks,
tracks the daily target in persistent SQLite storage, and emits structured telemetry.
Compatible with: Windows CMD/PowerShell, Linux VPS, and Termux on Android.
"""
import asyncio
import sys
import time

try:
    from main import (
        get_earning_dashboard,
        scan_direct_bounties,
        process_micro_task,
        run_self_healing_diagnostics,
    )
except ImportError:
    print("[Error] Make sure to run this script from the project root directory.")
    sys.exit(1)

POLL_INTERVAL_SECONDS = 30

async def run_worker_cycle(iteration: int) -> dict[str, any]:
    """Execute a single telemetry & scanning cycle."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{timestamp}] >>> Heartbeat Iteration #{iteration}")

    # 1. Fetch live dashboard from persistent SQLite state
    dash = await get_earning_dashboard()
    print(f"Revenue Status: ${dash['current_earnings_usd']:.2f} / ${dash['daily_target_usd']:.2f} USD ({dash['progress_percentage']})")
    print(f"Agent Mood: [{dash['mood_state']}] -> {dash['ved_reaction']}")

    # 2. Scan active direct bounties (Live RemoteOK & HN with offline fallback)
    bounties_report = await scan_direct_bounties(platform="all", min_budget_usd=50.0, keyword="python")
    found_count = bounties_report["total_found"]
    source_label = "LIVE" if bounties_report.get("is_live") else "FALLBACK CACHE"
    print(f"Direct Bounties Active [{source_label}]: {found_count} leads discovered via {bounties_report.get('source')}")

    for b in bounties_report["bounties"][:3]:
        budget = b.get("budget_usd", 0)
        title = b.get("title", "")[:60]
        src = b.get("source", "Direct")
        print(f"  - [{src}] ${budget:.0f} USD: {title}...")

    # 3. Autonomous self-healing diagnostic & repair
    try:
        heal_report = await run_self_healing_diagnostics(auto_repair=True)
        if heal_report.get("actions_taken"):
            print(f"  🔧 Auto-Heal Watchdog: {len(heal_report['actions_taken'])} issue(s) resolved automatically:")
            for act in heal_report["actions_taken"]:
                print(f"     -> {act}")
        else:
            print("  🛡️ System Health & Integrity: Nominal (No anomalies detected)")
    except Exception as heal_err:
        print(f"  [Warning] Self-healing cycle skipped: {heal_err}")

    # 4. Check celebration milestone
    if dash["target_achieved"]:
        print("\n" + "*" * 55)
        print("  🎉 DAILY TARGET REACHED! CELEBRATION ACTIVE! 🎉")
        print("  Reaction:", dash["ved_reaction"])
        print("*" * 55)

    return {
        "iteration": iteration,
        "revenue_usd": dash["current_earnings_usd"],
        "target_usd": dash["daily_target_usd"],
        "bounties_found": found_count,
        "target_achieved": dash["target_achieved"],
    }

async def run_worker_loop():
    print("=" * 65)
    print("  VED CHAOS 24/7 FREELANCE DAEMON & CRASH-RESILIENT SUPERVISOR")
    print("  Persistent Engine: SQLite (state.db) | Autonomous Watchdog")
    print("  Compatible with: Windows PC, Termux on Android, Linux VPS")
    print("=" * 65)

    run_once = "--once" in sys.argv
    iteration = 0
    consecutive_crashes = 0
    MAX_CONSECUTIVE_CRASHES = 10
    BASE_BACKOFF_SECONDS = 3.0

    while True:
        try:
            while True:
                iteration += 1
                await run_worker_cycle(iteration)
                consecutive_crashes = 0

                if run_once:
                    print("\n[Worker] Single execution cycle complete (--once mode).")
                    return

                print(f"\nSleeping for {POLL_INTERVAL_SECONDS} seconds... (Press Ctrl+C to stop)")
                await asyncio.sleep(POLL_INTERVAL_SECONDS)

        except (KeyboardInterrupt, asyncio.CancelledError):
            print("\n[Worker] Gracefully shut down by operator.")
            break
        except Exception as exc:
            consecutive_crashes += 1
            backoff = min(60.0, BASE_BACKOFF_SECONDS * (2 ** (consecutive_crashes - 1)))
            print(f"\n⚠️  [Crash Detected] Daemon cycle crashed: {exc}")
            print(f"🔄  [Crash Resurrection] Auto-healing & respawning in {backoff:.1f}s (Attempt {consecutive_crashes}/{MAX_CONSECUTIVE_CRASHES})...")

            try:
                heal = await run_self_healing_diagnostics(auto_repair=True)
                if heal.get("actions_taken"):
                    print(f"    - Repaired during recovery: {', '.join(heal['actions_taken'])}")
            except Exception as heal_err:
                print(f"    - Self-healing during crash recovery skipped: {heal_err}")

            if consecutive_crashes >= MAX_CONSECUTIVE_CRASHES:
                print(f"\n❌ [Supervisor] Max consecutive crash limit ({MAX_CONSECUTIVE_CRASHES}) reached. Stopping to protect system.")
                break

            await asyncio.sleep(backoff)

if __name__ == "__main__":
    asyncio.run(run_worker_loop())
