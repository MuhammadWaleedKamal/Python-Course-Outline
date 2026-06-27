# WebDriver Interactions & Commands

## Interacting with Elements

### Click
```python
element = driver.find_element(By.ID, "button")
element.click()
```

### Send Keys (Type)
```python
textbox = driver.find_element(By.NAME, "username")
textbox.send_keys("myusername")
```

### Submit Form
```python
form = driver.find_element(By.ID, "login_form")
form.submit()
```

### Clear Text
```python
textbox = driver.find_element(By.ID, "search")
textbox.clear()
```

## Getting Element Information

```python
# Get text
text = element.text

# Get attribute
href = element.get_attribute("href")
value = element.get_attribute("value")

# Check if displayed
is_displayed = element.is_displayed()

# Check if enabled
is_enabled = element.is_enabled()

# Check if selected
is_selected = element.is_selected()
```

## Navigation

```python
# Open URL
driver.get("https://example.com")

# Go back
driver.back()

# Go forward
driver.forward()

# Refresh
driver.refresh()
```

## Waits

### Implicit Wait (Global)
```python
driver.implicitly_wait(10)  # 10 seconds
```

### Explicit Wait (Specific)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.presence_of_element_located((By.ID, "element_id"))
)
```

## Common Commands

```python
# Switch frames
driver.switch_to.frame("frame_id")
driver.switch_to.default_content()

# Switch windows
driver.switch_to.window(window_handle)

# Execute JavaScript
driver.execute_script("javascript_code")

# Scroll
driver.execute_script("window.scrollBy(0, 500)")

# Take screenshot
driver.save_screenshot("screenshot.png")
```
