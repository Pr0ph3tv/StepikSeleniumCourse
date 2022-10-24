from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    solution = calc(x_value.text)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(solution)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_radiobutton = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
    robots_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
