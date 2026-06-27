"""
WebDriver interactions example.
Shows Selenium commands for browser automation.
"""

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except ImportError:
    print("Selenium is not installed. Install it with pip install selenium.")
else:
    driver = webdriver.Chrome()  # Requires ChromeDriver on PATH
    driver.get("https://example.com")
    print("Page title:", driver.title)
    element = driver.find_element(By.TAG_NAME, "h1")
    print("Found heading text:", element.text)
    driver.back()
    driver.refresh()
    driver.quit()

# Exercises:
# 1. Add a click action for a button if it exists.
# 2. Use driver.forward() after navigating back.
# 3. Add a wait before locating the element.
