from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(2)

# Step 2: Locate username and password fields
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

# Step 3: Enter credentials
username.send_keys("student")       # ✅ Correct username
password.send_keys("Password123")   # ✅ Correct password

# Step 4: Click login button
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# Step 5: Optional – Check if login is successful
time.sleep(2)
if "Logged In Successfully" in driver.page_source:
    print("✅ Login successful!")
else:
    print("❌ Login failed!")

driver.quit()
