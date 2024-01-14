import pytest
from selenium import webdriver
from config.browser_config import BrowserConfig
from config.url_config import UrlConfig


@pytest.fixture
def setup():
    if BrowserConfig.BROWSER_NAME == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        if BrowserConfig.HEADLESS_MODE:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')  # Add more Chrome-specific arguments as needed
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif BrowserConfig.BROWSER_NAME == 'firefox':
        chrome_options = webdriver.FirefoxOptions()
        if BrowserConfig.HEADLESS_MODE:
            chrome_options.add_argument('--headless')
        driver = webdriver.Firefox()

    elif BrowserConfig.BROWSER_NAME == 'edge':
        chrome_options = webdriver.EdgeOptions()
        if BrowserConfig.HEADLESS_MODE:
            chrome_options.add_argument('--headless')
        driver = webdriver.Edge()

    else:
        raise ValueError("Unsupported browser:" + BrowserConfig.BROWSER_NAME)

    driver.get(UrlConfig.HOME_PAGE_URL)

    yield driver
    driver.quit()
