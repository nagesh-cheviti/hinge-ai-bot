# Configuration: Gemini key, Appium caps
GEMINI_API_KEY = "AIzaSyAF1uw5jngiUgmbdcv9hCztYPZAgNX51EM"

APPIUM_CAPS = {
    "platformName": "Android",
    "platformVersion": "16",
    "deviceName": "emulator-5554",
    "appPackage": "co.hinge.app",
    "appActivity": "co.hinge.app.ui.AppActivity",
    "automationName": "UiAutomator2",
    "noReset": True,
    "newCommandTimeout": 600
}



