import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

def calculation(x):
    result = math.log(abs(12 * math.sin(int(x))))
    return result

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x = browser.find_element(By.ID, "input_value")
    x_value = x.text

    input_form = browser.find_element(By.TAG_NAME, "input")
    input_form.send_keys(str(calculation(x_value)))

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()