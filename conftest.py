import pytest
from selenium import webdriver
from config.browser_config import BrowserConfig
from config.url_config import UrlConfig


@pytest.fixture
def setup():
    if BrowserConfig.BROWSER == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif BrowserConfig.BROWSER == 'firefox':
        driver = webdriver.Firefox()
    elif BrowserConfig.BROWSER == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser:" + BrowserConfig.BROWSER)

    driver.get(UrlConfig.HOME_PAGE_URL)

    yield driver
    driver.quit()
