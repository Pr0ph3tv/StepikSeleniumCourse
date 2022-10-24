import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

def calculation(x):
    result = math.log(abs(12 * math.sin(int(x))))
    return result

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, "input_value")
    x_value = x.text

    input_form = browser.find_element(By.TAG_NAME, "input")
    input_form.send_keys(str(calculation(x_value)))

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
