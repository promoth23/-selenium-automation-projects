from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#launch browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#open browser
driver.get("https://google.com")
driver.maximize_window()
time.sleep(3)

driver.execute_script("window.open('https://microsoft.com');")
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
print("TAB 2:",driver.title)
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
print("TAB 1:",driver.title)
time.sleep(3)

driver.quit()


