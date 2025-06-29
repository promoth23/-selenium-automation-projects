from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ✅ Step 1: Open Chrome browser
driver = webdriver.Chrome()

# ✅ Step 2: Go to the website
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()
time.sleep(2)

# ✅ Step 3: Locate the "Red" checkbox
checkbox = driver.find_element(By.XPATH, '//*[@id="Content"]/div[1]/blockquote[1]/form/input[1]')

# ✅ Step 4: Tick it if not selected
if not checkbox.is_selected():
    checkbox.click()
    print("✅ Checkbox selected (ticked).")
    time.sleep(2)

# ✅ Step 5: Untick it if selected
if checkbox.is_selected():
    checkbox.click()
    print("❎ Checkbox unselected (unticked).")

# ✅ Final wait before closing
time.sleep(3)
driver.quit()
print("🧹 Browser closed.")
