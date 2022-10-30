import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_display(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_cart_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    time.sleep(10)
    assert add_to_cart_button.is_displayed(), "'Add to cart' button is not presented."
