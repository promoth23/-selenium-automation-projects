from utils.browser_setup import start_browser
from utils.excel_reader import read_credentials
from pages.login_page import LoginPage
import time

# Load data from Excel
credentials = read_credentials("data/credentials.xlsx")

for username, password in credentials:
    print(f"\n🔁 Testing login: {username} / {password}")
    driver = start_browser()

    login_page = LoginPage(driver)
    login_page.load("https://practicetestautomation.com/practice-test-login/")
    login_page.login(username, password)
    time.sleep(2)

    if "Logged In Successfully" in driver.page_source:
        print("✅ Login Success")
    else:
        print("❌ Login Failed")

    driver.quit()