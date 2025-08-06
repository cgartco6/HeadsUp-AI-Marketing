import schedule
import time
from content_creator import generate_content
from social_poster import auto_post
from growth_tracker import track_targets

# Business tier classification
def detect_business_size(monthly_scans):
    if monthly_scans < 50: return "SMB"
    elif 50 <= monthly_scans < 500: return "Medium"
    else: return "Enterprise"

# Self-healing content pipeline
def daily_marketing_routine():
    try:
        # 1. Generate demo content
        demo_video = generate_content(
            platform="TikTok", 
            business_tier="SMB",
            language="Zulu"
        )
        
        # 2. Auto-post to social media
        auto_post(
            content=demo_video,
            platforms=["TikTok", "WhatsApp", "Facebook"],
            optimal_times=True
        )
        
        # 3. Track growth targets
        current_subs = track_targets()
        print(f"Current subscribers: {current_subs}/1000 target")
        
    except Exception as e:
        print(f"Self-healing triggered: {str(e)}")
        # Retry after 15 minutes
        schedule.every(15).minutes.do(daily_marketing_routine)

# Schedule daily at 8:00 AM SAST
schedule.every().day.at("08:00").do(daily_marketing_routine)

while True:
    schedule.run_pending()
    time.sleep(60)
