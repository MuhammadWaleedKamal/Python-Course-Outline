# Advanced Locators & Elements Identification

## Locator Types

### ID Locator
```python
element = driver.find_element(By.ID, "element_id")
```

### Name Locator
```python
element = driver.find_element(By.NAME, "element_name")
```

### Class Name Locator
```python
element = driver.find_element(By.CLASS_NAME, "class_name")
```

### CSS Selector
```python
# By class
element = driver.find_element(By.CSS_SELECTOR, ".class")

# By ID
element = driver.find_element(By.CSS_SELECTOR, "#id")

# By attribute
element = driver.find_element(By.CSS_SELECTOR, "[name='value']")

# By tag
element = driver.find_element(By.CSS_SELECTOR, "button")
```

### XPath
```python
# By text
element = driver.find_element(By.XPATH, "//*[text()='Login']")

# By attribute
element = driver.find_element(By.XPATH, "//input[@name='username']")

# By position
element = driver.find_element(By.XPATH, "//button[1]")

# Relative
element = driver.find_element(By.XPATH, "//form//input[1]")
```

## Best Practices

✅ Use ID first (most reliable)
✅ Use CSS selectors (faster)
✅ Use XPath as last resort
✅ Make locators maintainable
❌ Hard-coded indices
❌ Overly complex XPaths

## Locator Priority

1. ID (most specific)
2. Name
3. Class Name
4. CSS Selector
5. XPath (most flexible)
