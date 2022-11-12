from mimesis import Person
from mimesis.locales import Locale

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is incorrect."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented."

    def register_new_user(self):
        new_user = Person(Locale.EN)
        email = new_user.email()
        password = new_user.password(length=10)
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        registration_email.send_keys(email)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        registration_password.send_keys(password)
        registration_password_repeated = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD)
        registration_password_repeated.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_button.click()
        pass
