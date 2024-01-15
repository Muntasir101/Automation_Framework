from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Define locators
    NEW_USER_NAME = (By.CSS_SELECTOR, "form[method='post'] > input[name='name']")
    NEW_USER_EMAIL = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default")
    NEW_USER_SIGNUP = (By.CSS_SELECTOR, ".signup-form h2")

    LOGIN_ACCOUNT = (By.CSS_SELECTOR, ".login-form h2")
    LOGIN_EMAIL = (By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "form[method='post'] > input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default")

