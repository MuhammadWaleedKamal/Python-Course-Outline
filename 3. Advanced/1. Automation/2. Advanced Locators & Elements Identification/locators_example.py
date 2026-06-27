"""
Locator example.
Defines common Selenium locators for a login page.
"""

from selenium.webdriver.common.by import By

login_locators = {
    'username': (By.ID, 'username'),
    'password': (By.NAME, 'password'),
    'submit': (By.CSS_SELECTOR, 'button[type="submit"]'),
    'forgot_password': (By.LINK_TEXT, 'Forgot password?'),
}

for name, locator in login_locators.items():
    print(f"{name}: {locator}")

# Exercises:
# 1. Add a locator for a Remember me checkbox.
# 2. Define an XPath locator for the login button.
# 3. Explain why CSS selectors can be faster than XPath.
