from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration_case1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .first[required]")
        first_name_input.send_keys("Vlad")
        second_name_input = browser.find_element(By.CSS_SELECTOR, ".second_class > .second[required]")
        second_name_input.send_keys("Dutov")
        phone_input = browser.find_element(By.XPATH,
                                           "//input[contains(@placeholder, 'Input your email') and @required]")
        phone_input.send_keys("vlad@dutov.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(10)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         f"Test Failed: welcome text - '{welcome_text}'")

        time.sleep(10)
        browser.quit()

    def test_registration_case2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .first[required]")
        first_name_input.send_keys("Vlad")
        second_name_input = browser.find_element(By.CSS_SELECTOR, ".second_class > .second[required]")
        second_name_input.send_keys("Dutov")
        phone_input = browser.find_element(By.XPATH,
                                           "//input[contains(@placeholder, 'Input your email') and @required]")
        phone_input.send_keys("vlad@dutov.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(10)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         f"Test Failed: welcome text - '{welcome_text}'")

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
