from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ADD_TO_BASKET_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    PRODUCT_NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_COST_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(3)")
    BASKET_COST_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    TOTAL_BASKET_COST = (By.CSS_SELECTOR, ".basket-mini")
