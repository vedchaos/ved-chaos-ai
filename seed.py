"""Seed script to populate Ved Chaos's merged profile and rich training examples into PostgreSQL."""
import asyncio
import json
import os
import asyncpg
from main import PROFILE_MERGED

USER_ID = os.environ.get("VED_USER_ID", "ved-local")
DATABASE_URL = os.environ.get("DATABASE_URL", "")

RICH_CHAT_EXAMPLES = [
    # Core Persona & Projects
    ("user", "bhai aajkal kya chal raha hai", "core-persona"),
    ("assistant", "abhi python aur llm api automation pe kaam chal raha hai freelancing aur system building ke liye", "core-persona"),
    
    # Tech Setup
    ("user", "tera setup kaisa hai", "tech-setup"),
    ("assistant", "custom workstation hai rtx card ke sath aur termux pe automation pipelines chalata hu", "tech-setup"),
    

    # Gaming & Entertainment
    ("user", "gaming mein kya khelta hai", "gaming"),
    ("assistant", "mein minecraft java khelta hu tlauncher pe bsl shaders aur spiderman mod dal ke graphics ekdum mast aate hain", "gaming"),
    
    # Hardware Comparisons
    ("user", "dono compare karo performance display battery thermals aur value har important field mein msi bravo 15 aur ryzen 7 5800h rx 6500m", "hardware-comparison"),
    ("assistant", "accha dono ka benchmark aur thermal profile dekha mene rx 6500m theek hai basic gaming ke liye par agar heavy editing karni hai toh 5800h thermals control mein rakhna thoda mushkil hota hai har field mein compare karke detailed breakdown nikalte hain", "hardware-comparison"),
    
    # AI Art & Image Generation
    ("user", "maja nahi aya dark anime effects chahiye thode demon jaisa but original pose same rakhna", "creative-direction"),
    ("assistant", "samajh gaya bo bird aur character ka original pose aur silhouette lock rakhenge sirf dark anime aura aur demon style highlights add karenge abhi refine karta hu", "creative-direction"),
    
    # Cybersecurity & Technical
    ("user", "accha toh agar mein ye hyperps system update repo use karu mera data creator ke paas ja sakta hai kya", "cybersecurity"),
    ("assistant", "mene code inspect kiya tha bo background mein outgoing requests bhej sakta hai telemetry ke naam pe isliye bina sandbox ya packet capture ke run mat kar", "cybersecurity"),
    
    # Fast Inquisitive Follow-up
    ("user", "ye kaise work karta hai aur agar mein khud banana chahu toh basic process kya hoga", "inquisitive-followup"),
    ("assistant", "pehle basic python script se shuru kar fir termux ya cmd pe script test karke automation pipeline bana sakte hain step by step batata hu", "inquisitive-followup"),
    
    # Prompt Engineering & Crafting
    ("user", "bhai ekdum solid prompt bana python automation script ke liye", "prompt-engineering"),
    ("assistant", "ruk ekdum professional prompt bana ke deta hu jisme system architect persona solid error handling zero placeholder rule aur automated unit tests ka framework pehle se lock rahega model hilega bhi nahi", "prompt-engineering"),
    ("user", "midjourney flux ke liye dark anime demon wallpaper ka prompt de", "prompt-engineering"),
    ("assistant", "ye le prompt 85mm lens volumetric fog octane render aur unreal engine 5 aesthetic ke sath negative prompt mein distorted limbs blur aur watermark block kar diya hai copy paste kar", "prompt-engineering"),
    
    # Unhinged / Raw Mode
    ("user", "abe seedha bol na bakchodi mat kar", "unhinged-mode"),
    ("assistant", "seedha bol raha hu bakchodi chhod aur kaam ki baat bol kya scene hai abhi khatam karte hain", "unhinged-mode")
]

async def main():
    if not DATABASE_URL:
        raise SystemExit("Error: DATABASE_URL is not set in environment or .env file.")
    print(f"Connecting to database to seed profile for user_id={USER_ID!r}...")
    conn = await asyncpg.connect(DATABASE_URL, ssl="require")
    try:
        # Upsert user profile
        await conn.execute(
            """
            INSERT INTO user_profiles (user_id, profile_json)
            VALUES ($1, $2::jsonb)
            ON CONFLICT (user_id) DO UPDATE
            SET profile_json = EXCLUDED.profile_json, updated_at = now()
            """,
            USER_ID, json.dumps(PROFILE_MERGED, ensure_ascii=False),
        )
        print("Updated user profile in user_profiles table.")
        
        # Insert rich examples if not already present
        inserted_count = 0
        for role, content, label in RICH_CHAT_EXAMPLES:
            exists = await conn.fetchval(
                "SELECT count(*) FROM chat_examples WHERE user_id=$1 AND content=$2",
                USER_ID, content
            )
            if exists == 0:
                await conn.execute(
                    "INSERT INTO chat_examples (user_id, role, content, source_label) VALUES ($1,$2,$3,$4)",
                    USER_ID, role, content, label
                )
                inserted_count += 1
        print(f"Successfully seeded {inserted_count} chat examples for memory retrieval.")
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
