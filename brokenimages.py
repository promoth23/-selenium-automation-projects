import requests
from utils.browser_setup import start_browser
from selenium.webdriver.common.by import By

driver = start_browser()
driver.get("https://www.flipkart.com")

images = driver.find_elements(By.TAG_NAME, "img")
print(f"🖼️ Total images found: {len(images)}")

broken = 0
for img in images:
    src = img.get_attribute("src")
    if src and src.startswith("http"):
        try:
            response = requests.head(src, allow_redirects=True, timeout=5)
            if response.status_code >= 400:
                print(f"❌ Broken image: {src} [{response.status_code}]")
                broken += 1
        except Exception as e:
            print(f"❌ Exception for image {src}: {e}")
            broken += 1

print(f"🔍 Broken images count: {broken}")
driver.quit()
