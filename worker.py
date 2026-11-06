"""24/7 Background Runner Daemon (Windows CMD / Android Termux Compatible).
Monitors zero-commission bounties, tracks the daily $500 target, and prints live status telemetry.
"""
import asyncio
import sys
import time

try:
    from main import (
        DAILY_EARNING_STATE,
        get_earning_dashboard,
        scan_direct_bounties,
        process_micro_task,
    )
except ImportError:
    print("[Error] Make sure to run this script from the project directory.")
    sys.exit(1)

POLL_INTERVAL_SECONDS = 30

async def run_worker_loop():
    print("=" * 60)
    print("  VED CHAOS 24/7 FREELANCE DAEMON & BOUNTY SCANNER")
    print(f"  Target: ${DAILY_EARNING_STATE['daily_target_usd']} USD / day | Engine: Active")
    print("  Compatible with: Windows PC, Termux on Android, Linux VPS")
    print("=" * 60)

    iteration = 0
    try:
        while True:
            iteration += 1
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[{timestamp}] >>> Heartbeat Iteration #{iteration}")

            # 1. Fetch live dashboard
            dash = await get_earning_dashboard()
            print(f"Revenue Status: ${dash['current_earnings_usd']} / ${dash['daily_target_usd']} USD ({dash['progress_percentage']})")
            print(f"Agent Mood: [{dash['mood_state']}] -> {dash['ved_reaction']}")

            # 2. Scan active direct bounties
            bounties_report = await scan_direct_bounties(platform="all", min_budget_usd=50.0, keyword="python")
            found_count = bounties_report["total_found"]
            print(f"Direct Zero-Fee Bounties Active: {found_count} leads ready to pitch")
            for b in bounties_report["bounties"][:2]:
                print(f"  - [{b['source']}] ${b['budget_usd']} USD: {b['title'][:65]}...")

            # 3. Check celebration condition
            if dash["target_achieved"]:
                print("\n" + "*" * 50)
                print("  🎉 DAILY TARGET REACHED! CELEBRATION ACTIVE! 🎉")
                print("  Reaction:", dash["ved_reaction"])
                print("*" * 50)

            print(f"Sleeping for {POLL_INTERVAL_SECONDS} seconds... (Press Ctrl+C to stop)")
            await asyncio.sleep(POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\n[Worker] Gracefully shut down by user.")

if __name__ == "__main__":
    asyncio.run(run_worker_loop())

