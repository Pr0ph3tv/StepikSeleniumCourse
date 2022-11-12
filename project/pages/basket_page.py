from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
from .constants import BasketPageConstants


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_page_site_path_presented()
        self.should_be_basket_site_path_presented()
        self.should_be_page_header_presented()
        self.should_be_basket_header_presented()

    def should_be_empty_basket(self):
        self.should_be_message_that_basket_is_empty()
        self.should_be_correct_message_that_basket_is_empty()
        self.should_not_be_products_formset_presented_when_basket_is_empty()
        self.should_not_be_other_elements_presented_when_basket_is_empty()

    def should_not_be_empty_basket(self):
        self.should_not_be_message_that_basket_is_empty()
        self.should_be_products_formset_presented_when_basket_is_not_empty()
        self.should_be_other_elements_presented_when_basket_is_not_empty()

    def should_be_basket_url(self):
        assert BasketPageConstants.BASKET_URL_PATH in self.browser.current_url, "Basket page URL is incorrect."

    def should_be_basket_site_path_presented(self):
        basket_site_path = self.browser.find_element(*BasePageLocators.PAGE_SITE_PATH).text
        print(f"basket_site_path={basket_site_path}, Header= {BasketPageConstants.BASKET_PAGE_HEADER}")
        assert BasketPageConstants.BASKET_PAGE_HEADER == basket_site_path, "Basket site path is incorrect."

    def should_be_basket_header_presented(self):
        basket_header = self.browser.find_element(*BasePageLocators.PAGE_HEADER).text
        assert BasketPageConstants.BASKET_PAGE_HEADER in basket_header, "Basket header is incorrect."

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE),\
            "Message that basket is empty is not presented when basket is empty."

    def should_be_correct_message_that_basket_is_empty(self):
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        message_text = self.browser.execute_script("""
        return jQuery(arguments[0]).contents().filter(function() {
            return this.nodeType == Node.TEXT_NODE;
        }).text();
        """, basket_empty_message)
        print(f"result = {message_text}, Basket_message {BasketPageConstants.BASKET_PAGE_EMPTY_MESSAGE}")
        assert BasketPageConstants.BASKET_PAGE_EMPTY_MESSAGE in message_text,\
            "Message that the basket is empty is not correct."

    def should_be_products_formset_presented_when_basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORMSET),\
            "Basket is not empty and basket formset is not presented."

    def should_be_other_elements_presented_when_basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.MULTIPLE_BASKET_ELEMENTS),\
            "Other elements are not presented when the basket is not empty."

    def should_not_be_message_that_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Message that basket is empty is presented when basket is not empty."

    def should_not_be_products_formset_presented_when_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET),\
            "Basket is empty and basket formset is presented."

    def should_not_be_other_elements_presented_when_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.MULTIPLE_BASKET_ELEMENTS),\
            "Other elements are presented when the basket is empty."
