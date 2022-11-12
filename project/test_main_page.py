import pytest

from .pages.main_page import MainPage
from .pages.constants import MainPageConstants
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, MainPageConstants.MAIN_PAGE_URL)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail(reason="This test works only in english locale.")
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, MainPageConstants.MAIN_PAGE_URL)
    main_page.open()
    main_page.should_be_view_basket_button_presented()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_that_basket_is_empty()
    basket_page.should_be_correct_message_that_basket_is_empty()
