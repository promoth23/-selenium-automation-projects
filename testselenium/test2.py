from selenium import webdriver
from selenium. webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#launch browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open browser
driver.get("http://www.selenium.dev")
driver.maximize_window()
time.sleep(5)

driver.forward()

title=driver.title
print(title)
assert"Selenium"in title
time.sleep(5)
driver.get("http://www.google.com")
driver.quit()
