from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, "input_value").text
    solution = calc(x_value)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(solution)

    robots_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robots_checkbox.click()

    robots_radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_radiobutton)
    robots_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()