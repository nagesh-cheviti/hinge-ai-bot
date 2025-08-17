Hinge AI Bot
============

This project is an automation script using Appium and Google Generative AI (Gemini) to interact with the Hinge Android app. The bot extracts profile prompts, generates clever flirty comments using AI, and posts them as replies.

Features:
---------
- Launches the Hinge app on an Android emulator using Appium
- Extracts the prompt and answer text from a profile
- Generates a comment using Gemini AI
- Likes the profile and submits the comment
- Logs the prompt/comment interaction and saves a screenshot

Requirements:
-------------
- Python 3.x
- Appium-Python-Client
- google-generativeai
- Selenium

Setup Instructions:
-------------------
1. Clone the repository:
   git clone https://github.com/nagesh-cheviti/hinge-ai-bot.git

2. Navigate into the project directory:
   cd hinge-ai-bot

3. Create and activate a virtual environment (optional but recommended):
   python3 -m venv .venv
   source .venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Set up your Gemini API key:
   In config.py, set:
   GEMINI_API_KEY = "your-api-key"

6. Start your Android emulator (example):
   emulator -avd Pixel_6

7. Start the Appium server:
   appium

8. Run the bot:
   python3 appium_bot.py

File Structure:
---------------
- appium_bot.py         : Main automation logic
- ai_commenter.py       : Uses Gemini to generate comments
- config.py             : API key and Appium capabilities
- utils.py              : Logging and screenshots
- logs/                 : Stores CSV log of profiles
- screenshots/          : Saves profile screenshots
- requirements.txt      : Dependencies

Disclaimer:
-----------
This tool is for educational purposes only. Automated interaction on dating platforms may violate their terms of service. Use responsibly.
