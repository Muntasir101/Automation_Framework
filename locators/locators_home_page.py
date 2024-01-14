from selenium.webdriver.common.by import By


class HomePageLocators:
    # Define locators
    TestCases = (By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a")
    SIGNUP_LOGIN = (By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a")

