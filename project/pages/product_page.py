from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_name()
        self.should_be_add_to_basket_button()
        self.should_be_total_basket_cost()

    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "Product URL is incorrect."

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented."

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "'Add to basket' button is not presented."

    def should_be_total_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_BASKET_COST), "Total basket cost is not presented."

    def should_be_notification_that_product_is_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_NOTIFICATION),\
            "Notification that product was added to the basket is not presented."

    def should_not_be_notification_that_product_is_added_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_NOTIFICATION),\
            "Notification that product was added to the basket is presented but should not be."

    def notification_that_product_is_added_to_basket_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_NOTIFICATION),\
            "Notification that product was added to the basket is presented but should disappear."

    def should_be_notification_with_total_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_NOTIFICATION),\
            "Notification with total basket cost is not presented."

    def is_product_name_in_notification_equal_to_description(self):
        product_name_in_description = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_notification = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_NOTIFICATION).text
        assert product_name_in_description == product_name_in_notification,\
            "Product name in description is not equal to the one in notification."

    def is_product_price_equal_to_basket_cost(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_cost_in_notification = self.browser.find_element(*ProductPageLocators.BASKET_COST_IN_NOTIFICATION).text
        assert product_price == basket_cost_in_notification,\
            "Product price and basket cost in some elements are not equal."

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
