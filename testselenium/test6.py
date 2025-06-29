
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()
time.sleep(2)

# ✅ List of values for the checkboxes we want to select
checkbox_values = ['red', 'blue']

for value in checkbox_values:
    cb = driver.find_element(By.XPATH, f"//input[@type='checkbox' and @value='{value}']")
    if cb.is_selected():
        cb.click()
        print("is slected")
        time.sleep(2)
for value in checkbox_values:
    cb = driver.find_element(By.XPATH, f"//input[@type='checkbox' and @value='{value}']")
    if not cb.is_selected():
        cb.click()
        print("is not selected")
        time.sleep(2)

driver.close()