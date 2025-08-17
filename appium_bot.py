from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from config import APPIUM_CAPS
from ai_commenter import get_ai_comment
from utils import log_profile, take_screenshot

import time

# Setup Appium capabilities
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "16")
options.set_capability("deviceName", "emulator-5554")
options.set_capability("appPackage", "co.hinge.app")
options.set_capability("appActivity", "co.hinge.app.ui.AppActivity")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("noReset", True)
options.set_capability("newCommandTimeout", 600)

# Start Appium session
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# ✅ Ensure the app is active
driver.activate_app("co.hinge.app")

# Give app time to load
time.sleep(5)

for i in range(1):
    try:
        print(f"\n🔄 Processing profile #{i + 1}")

        # Wait for prompt to appear
        prompt_bubble = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.ID, "co.hinge.app:id/prompt_bubble"))
        )[0]  # First prompt only

        question_view = prompt_bubble.find_element(By.ID, "co.hinge.app:id/question")
        answer_view = prompt_bubble.find_element(By.ID, "co.hinge.app:id/answer")

        question_text = question_view.text.strip()
        answer_text = answer_view.text.strip()
        full_prompt = f"{question_text} {answer_text}"

        print(f"🧠 Prompt text: {full_prompt}")


        # Generate AI comment based on prompt
        comment = get_ai_comment(full_prompt)

        # Tap like button (use Accessibility ID or fallback to resource ID)
        like_button_prompt = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[@resource-id='co.hinge.app:id/prompt_bubble']//android.widget.ImageButton[@resource-id='co.hinge.app:id/like_button']"
            ))
        )
        like_button_prompt.click()

        time.sleep(1)

        # Enter comment
        # Tap comment box first to make it focusable
        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "co.hinge.app:id/comment_composition_view"))
        )
        comment_box.click()  # required to activate

        # Then send keys (AI comment)
        comment_box.send_keys(comment)


        # Send comment
        send_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//androidx.compose.ui.platform.ComposeView[@resource-id="co.hinge.app:id/buttons_layout"]/android.view.View/android.view.View[2]'))
        )
        send_btn.click()


        print(f"✅ Commented: {comment}")

        # Log and take screenshot
        log_profile(i + 1, full_prompt, comment)
        take_screenshot(driver, i + 1)

        time.sleep(3)

    except Exception as e:
        print(f"❌ Error on profile #{i + 1}: {e}")
        continue

# End session
driver.quit()
