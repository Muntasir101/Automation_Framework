import pytest
from selenium import webdriver
from config.browser_config import BrowserConfig
from config.url_config import UrlConfig

import pytest
from selenium import webdriver
from config.browser_config import BrowserConfig


@pytest.fixture
def setup():
    if BrowserConfig.BROWSER_NAME == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        if BrowserConfig.HEADLESS_MODE:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')  # Add more Chrome-specific arguments as needed
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

    elif BrowserConfig.BROWSER_NAME == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        if BrowserConfig.HEADLESS_MODE:
            firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)

    elif BrowserConfig.BROWSER_NAME == 'edge':
        edge_options = webdriver.EdgeOptions()
        if BrowserConfig.HEADLESS_MODE:
            edge_options.use_chromium = True
            edge_options.add_argument('--headless')
        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError("Unsupported browser:" + BrowserConfig.BROWSER_NAME)

    yield driver
    driver.quit()
