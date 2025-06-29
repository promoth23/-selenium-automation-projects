from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.get("https://testpages.eviltester.com/styled/basic-html-form-test.html")
driver.maximize_window()
time.sleep(2)

# Find the dropdown element
dropdown = Select(driver.find_element(By.NAME, "dropdown"))

# Select by visible text
dropdown.select_by_visible_text("Drop Down Item 3")
print("✅ Selected by visible text")

# Select by value
dropdown.select_by_value("dd4")
print("✅ Selected by value (Drop Down Item 4)")

# Select by index (starts from 0)
dropdown.select_by_index(2)
print("✅ Selected by index (Drop Down Item 2)")

# Count all dropdown values
options = dropdown.options
print(f"Total dropdown options: {len(options)}")

# Loop through all dropdown values
for option in options:
    print("Option:", option.text)
    if option.text == "Drop Down Item 1":
        dropdown.select_by_visible_text(option.text)
        print("✅ Found and selected Drop Down Item 1")
        break

# Wait and quit
time.sleep(3)
driver.quit()




