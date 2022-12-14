import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.constants import LoginPageConstants
from .pages.constants import ProductsConstants


@pytest.mark.user_add_to_basket_tests
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LoginPageConstants.LOGIN_URL)
        login_page.open()
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, ProductsConstants.BOOK_CODERS_AT_WORK)
        product_page.open()
        product_page.should_be_product_page()
        product_page.should_not_be_notification_that_product_is_added_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, ProductsConstants.BOOK_HACKERS_DELIGHT)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.should_be_notification_that_product_is_added_to_basket()
        product_page.is_product_name_in_notification_equal_to_description()
        product_page.should_be_notification_with_total_basket_cost()
        product_page.is_product_price_equal_to_basket_cost()


@pytest.mark.need_review
@pytest.mark.parametrize('offer_number', [pytest.param(number, marks=pytest.mark.xfail(
    number == 7, reason="The presence of a bug on the page is conceived according to the task."))
                                          for number in range(10)])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_notification_that_product_is_added_to_basket()
    product_page.is_product_name_in_notification_equal_to_description()
    product_page.should_be_notification_with_total_basket_cost()
    product_page.is_product_price_equal_to_basket_cost()


@pytest.mark.xfail(reason="This test is incorrect")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, ProductsConstants.BOOK_CODERS_AT_WORK)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.should_not_be_notification_that_product_is_added_to_basket()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, ProductsConstants.BOOK_CODERS_AT_WORK)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_not_be_notification_that_product_is_added_to_basket()


@pytest.mark.xfail(reason="This test is incorrect.")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, ProductsConstants.BOOK_CODERS_AT_WORK)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.notification_that_product_is_added_to_basket_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, ProductsConstants.BOOK_THE_CITY_AND_THE_STARS)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, ProductsConstants.BOOK_THE_CITY_AND_THE_STARS)
    product_page.open()
    product_page.should_be_product_page()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.xfail(reason="This test works only in english locale.")
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, ProductsConstants.BOOK_THE_GIRL_WHO_PLAYED_WITH_NON_FIRE)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_be_view_basket_button_presented()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_that_basket_is_empty()
    basket_page.should_be_correct_message_that_basket_is_empty()
