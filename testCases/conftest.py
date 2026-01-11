import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addini("baseUrl", "Application base URL")
    parser.addini("username", "Login username")
    parser.addini("password", "Login password")
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
       assert False, 'Provide chrome, firefox or Arun'

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver


