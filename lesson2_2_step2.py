from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = int(browser.find_element(By.ID, "num1").text)
    second_number = int(browser.find_element(By.ID, "num2").text)

    solution = first_number + second_number
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(solution))

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
