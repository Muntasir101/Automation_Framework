from selenium.webdriver.common.by import By


class HomePageLocators:
    # Define locators
    TestCases = (By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a")
    SIGNUP_LOGIN = (By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a")

    LOGGED_IN_USER_NAME = (By.CSS_SELECTOR, "li:nth-of-type(10) > a")

    DELETE_ACCOUNT = (By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a")

