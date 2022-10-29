import pytest

from selenium import webdriver


@pytest.fixture(scope="function")
def browser_chrome():
    print("\nStarting browser for the test")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuitting browser")
    browser.quit()

