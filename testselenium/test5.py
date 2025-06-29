from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.w3schools.com/howto/howto_css_dropdown.asp")  # Has hover menu
time.sleep(3)

# Initialize ActionChains
actions = ActionChains(driver)

# Locate the dropdown button (hoverable element)
dropdown = driver.find_element(By.CLASS_NAME, "dropbtn")

# Move to element (hover)
actions.move_to_element(dropdown).perform()
print("Hovered over dropdown")

time.sleep(2)

# Optional: Click one of the dropdown links
link = driver.find_element(By.LINK_TEXT, "Link 1")
actions.move_to_element(link).click().perform()
print("Clicked on Link 1")

# Wait and close
time.sleep(3)
driver.quit()
