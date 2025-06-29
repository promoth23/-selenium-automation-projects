from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Open a blank page
driver.get("https://www.google.com")
time.sleep(2)

# Inject a JavaScript alert box into the page
driver.execute_script("alert('🚨 This is an alert box from Selenium!');")

# Wait and accept the alert
time.sleep(2)
alert = driver.switch_to.alert
print("Alert text:", alert.text)  # Optional: Print alert message
alert.accept()  # Click "OK"

print("✅ Alert handled.")
driver.quit()
