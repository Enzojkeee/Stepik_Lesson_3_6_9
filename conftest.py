from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                      default="chrome", help="Choose browser:Chrome or Firefox")
    parser.addoption('--language', action ='store',
                     default='ru', help="Choose your language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart Chrome browser")
        browser=webdriver.Chrome()
    elif browser_name == "firefox":
        print("start Firefox browser")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser name should be chrome or firefox")
    yield browser
    print("\nQuit browser")
    browser.quit()
@pytest.fixture(scope='function')
def language(request):
    user_language = request.config.getoption('language')
    return user_language
