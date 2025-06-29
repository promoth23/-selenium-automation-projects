from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    # ✅ Setup Chrome WebDriver automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # --- Step 1: Login to SauceDemo ---
    username = "standard_user"
    password = "secret_sauce"
    login_url = "https://www.saucedemo.com/"
    driver.get(login_url)

    # ✅ Locate and interact with login form
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    assert login_button.is_enabled(), "Login button is disabled"
    login_button.click()

    time.sleep(3)  # Wait for Products page to load

    # ✅ Check successful login
    success_element = driver.find_element(By.CSS_SELECTOR, ".title")
    assert success_element.text == "Products", "Login failed or incorrect page"
    print("✅ Login successful and landed on Products page.")

    # --- Step 2: Navigation operations ---
    driver.get("https://www.google.com")
    print("🌐 Navigated to Google")
    time.sleep(2)

    driver.back()
    print("⬅️ Went back to Products page")
    time.sleep(2)

    # ✅ Use try-except for forward navigation to handle disconnected session
    try:
        driver.forward()
        print("➡️ Went forward to Google again")
        time.sleep(2)
    except Exception as e:
        print(f"⚠️ Couldn't go forward: {e}")

    driver.refresh()
    print("🔄 Page refreshed")
    time.sleep(2)

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    if driver:
        driver.quit()
        print("✅ Browser closed")

