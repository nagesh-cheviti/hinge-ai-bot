# Helpers: logging, screenshots
import time
import csv
from datetime import datetime

def log_profile(profile_id, prompt, comment):
    timestamp = datetime.now().isoformat()
    with open("logs/profile_log.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([profile_id, prompt, comment, timestamp])

def take_screenshot(driver, profile_id):
    filepath = f"screenshots/profile_{profile_id:03d}.png"
    driver.save_screenshot(filepath)
