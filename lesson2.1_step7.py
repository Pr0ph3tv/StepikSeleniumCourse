from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_value = treasure.get_attribute("valuex")
    solution = calc(x_value)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(solution)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
