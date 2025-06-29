import requests
from utils.browser_setup import start_browser
from selenium.webdriver.common.by import By

driver = start_browser()
driver.get("https://www.flipkart.com")

links = driver.find_elements(By.TAG_NAME, "a")
print(f"🔗 Total links found: {len(links)}")

broken = 0
for link in links:
    url = link.get_attribute("href")
    if url and url.startswith("http"):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code >= 400:
                print(f"❌ Broken link: {url} [{response.status_code}]")
                broken += 1
        except Exception as e:
            print(f"❌ Exception for link {url}: {e}")
            broken += 1

print(f"🔍 Broken links count: {broken}")
driver.quit()
