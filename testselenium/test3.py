
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time




#launch browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open browser
driver.get("https://google.com")
time.sleep(3)
#search element
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("selenium")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.get("https://selenium.dev")
title=driver.title
print(title)
assert "Selenium" in title
time.sleep(3)
driver.quit()
