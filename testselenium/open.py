from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# Wait for the page to load
time.sleep(2)

# Find the search box and type a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium testing")
search_box.send_keys(Keys.RETURN)  # Press Enter

# Wait to view results
time.sleep(5)

# Close browser
driver.quit()