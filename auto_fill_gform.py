from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# --- CONFIGURATION ---

# Replace with your Google Form URL
form_url = "https://docs.google.com/forms/d/e/1FAIpQLScXXXXXX/viewform"

# Example answers for each question (adjust to your form)
answers = {
    "Name": "Shubhankar Mestry",
    "Email": "mshubh555@gmail.com",
    "Feedback": "Great experience! Loved it."
}

# --- SCRIPT START ---

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.get(form_url)

time.sleep(2)  # wait for page to load fully

# Find all input fields and textareas
inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], textarea")

# Fill fields with your data
for field in inputs:
    label = field.get_attribute("aria-label") or ""
    for key, value in answers.items():
        if key.lower() in label.lower():
            field.send_keys(value)
            break

# Click the submit button
submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_button.click()

print("✅ Form submitted successfully!")
time.sleep(2)
driver.quit()
