from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

# Function to open a browser and navigate to a given URL
def open_browser(url, name):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    print(f"✅ {name} opened.")
    time.sleep(5)  # Keep browser open for 5 seconds
    driver.quit()
    print(f"❎ {name} closed.")

# Create threads for Google and Microsoft
google_thread = threading.Thread(target=open_browser, args=("https://www.google.com", "Google"))
microsoft_thread = threading.Thread(target=open_browser, args=("https://www.bing.com", "Microsoft Bing"))

# Start both threads
google_thread.start()
microsoft_thread.start()

# Wait for both to finish
google_thread.join()
microsoft_thread.join()

print("✅ Both browsers tested successfully.")
