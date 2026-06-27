"""
Selenium introduction example.
Shows a simple browser automation structure.
"""

try:
    from selenium import webdriver
except ImportError:
    print("Selenium is not installed. Install it with pip install selenium.")
else:
    driver = webdriver.Chrome()  # Requires ChromeDriver on PATH
    driver.get("https://example.com")
    print("Page title:", driver.title)
    driver.quit()

# Exercises:
# 1. Add comments for each Selenium step.
# 2. Replace Chrome() with Firefox() if using geckodriver.
# 3. Print the current URL after loading the page.
