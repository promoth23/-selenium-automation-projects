from utils.browser_setup import start_browser
import time

driver = start_browser()
driver.get("https://www.flipkart.com")
time.sleep(3)

driver.save_screenshot("screenshots/homepage.png")
print("✅ Screenshot saved as 'homepage.png'")
driver.quit()
