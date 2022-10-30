import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Select a browser. Available browsers: Chrome (default) or Firefox.")
    parser.addoption('--language', action='store', default='en',
                     help="Select a preferred language for the web page.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    locale = request.config.getoption("language")
    if browser_name.lower() == "chrome":
        browser_options = Options()
        browser_options.add_experimental_option('prefs', {'intl.accept_languages': locale})
        print("\nStarting browser for the test")
        browser = webdriver.Chrome(options=browser_options)
    elif browser_name.lower() == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", locale)
        print("\nStarting browser for the test")
        browser = webdriver.Firefox(firefox_profile=profile)
    else:
        raise pytest.UsageError(f"'--browser={browser_name}' parameter value is not supported")
    yield browser
    print("\nQuitting browser")
    browser.quit()

