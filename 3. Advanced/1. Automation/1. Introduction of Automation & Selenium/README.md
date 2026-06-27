# Introduction to Automation & Selenium

## What is Selenium?

Tool for automating web browser interactions.

## Installation

```bash
pip install selenium

# Download WebDriver
# Chrome: https://chromedriver.chromium.org/
# Firefox: https://github.com/mozilla/geckodriver/releases
```

## Basic Structure

```python
from selenium import webdriver

# Open browser
driver = webdriver.Chrome()

# Navigate
driver.get("https://example.com")

# Close browser
driver.quit()
```

## Browser Interactions

```python
# Navigate
driver.get(url)          # Open URL
driver.back()            # Back button
driver.forward()         # Forward
driver.refresh()         # Refresh

# Window management
driver.maximize_window()
driver.set_window_size(800, 600)

# Get info
title = driver.title
url = driver.current_url
```

## Finding Elements

```python
from selenium.webdriver.common.by import By

# Find single element
element = driver.find_element(By.ID, "element_id")
element = driver.find_element(By.NAME, "name")
element = driver.find_element(By.CLASS_NAME, "class")
element = driver.find_element(By.CSS_SELECTOR, "selector")
element = driver.find_element(By.XPATH, "//xpath")

# Find multiple elements
elements = driver.find_elements(By.CLASS_NAME, "class")
```

## Best Practices

✅ Always close browser (use quit())
✅ Use waits for dynamic elements
✅ Handle exceptions
✅ Make tests independent
❌ Hard-coded delays (use waits instead)
