import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Step 1: Go to LinkedIn login
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for manual 2FA/CAPTCHA
    input("🔐 Complete CAPTCHA or 2FA in browser, then press Enter here to continue...")

    # Step 2: Navigate to Jobs page
    driver.get("https://www.linkedin.com/jobs")
    WebDriverWait(driver, 15).until(EC.title_contains("Jobs"))
    print("✅ Navigated to LinkedIn Jobs")

    # Step 3: Enter job title
    search_box_xpath = "//input[contains(@aria-label, 'Search by title') or contains(@placeholder, 'Search jobs')]"
    search_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, search_box_xpath)))
    search_box.clear()
    search_box.send_keys("Python Developer")
    search_box.send_keys(Keys.RETURN)

    # Step 4: Scroll and load job cards
    print("⏳ Loading job listings...")
    scroll_pause = 2
    job_cards_xpath = "//ul[contains(@class, 'jobs-search-results__list')]/li"
    last_height = driver.execute_script("return document.body.scrollHeight")
    job_listings = []

    for i in range(10):
        print(f"🔄 Scroll attempt {i+1}")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)

        job_listings = driver.find_elements(By.XPATH, job_cards_xpath)
        print(f"📄 Jobs loaded so far: {len(job_listings)}")

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("✅ Reached end of scrollable content.")
            break
        last_height = new_height

    if not job_listings:
        print("❌ No job listings found.")
    else:
        print(f"✅ Found {len(job_listings)} job listings.")
        for i, job in enumerate(job_listings[:5]):  # Print first 5 job titles
            try:
                title = job.find_element(By.CSS_SELECTOR, "h3").text
                company = job.find_element(By.CSS_SELECTOR, "h4").text
                print(f"{i+1}. {title} at {company}")
            except:
                continue

except TimeoutException as te:
    print(f"❌ Timeout Error: {te}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
finally:
    time.sleep(5)
    driver.quit()
    print("🔚 Browser closed.")
