from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    PAGE_SITE_PATH = (By.CSS_SELECTOR, ".breadcrumb .active")
    PAGE_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ADD_TO_BASKET_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    PRODUCT_NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_COST_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(3)")
    BASKET_COST_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    TOTAL_BASKET_COST = (By.CSS_SELECTOR, ".basket-mini")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "#content_inner > p a")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    MULTIPLE_BASKET_ELEMENTS = (By.CSS_SELECTOR, ".col-sm-6")
