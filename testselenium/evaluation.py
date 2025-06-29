from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ 1. Open browser and visit website
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.google.com")

# ✅ 2. Search something in search bar (example: "Selenium Python")
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)
print("✅ Searched for 'Selenium Python'")

# ✅ 3. Tab undo: Go back to previous page (Google home)
time.sleep(2)
driver.back()
print("⬅️ Went back to Google homepage")

# ✅ 4. Tab redo: Go forward to search results again
time.sleep(2)
driver.forward()
print("➡️ Went forward to search results")

# ✅ 5. Page refresh
time.sleep(2)
driver.refresh()
print("🔄 Page refreshed")

# ✅ 6. Use explicit wait (Wait for the search box to reappear)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    print("⏳ Search box is visible again using explicit wait")
except:
    print("❌ Search box not found")

# ✅ End: Close browser
time.sleep(3)
driver.quit()
print("✅ Browser closed")
