from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input[name=firstname][required]")
    first_name.send_keys("Vlad")

    second_name = browser.find_element(By.CSS_SELECTOR, "input[name=lastname][required]")
    second_name.send_keys("Dutov")

    email = browser.find_element(By.CSS_SELECTOR, "input[name=email][required]")
    email.send_keys("vlad@dutov.com")

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.dirname(__file__))

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test_file.txt")
    file_input = browser.find_element(By.CSS_SELECTOR, "#file[required]")
    file_input.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
