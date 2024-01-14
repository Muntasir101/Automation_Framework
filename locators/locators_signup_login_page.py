from selenium.webdriver.common.by import By


class SignupLoginPageLocators:
    # Define locators
    NEW_USER_NAME = (By.CSS_SELECTOR, "form[method='post'] > input[name='name']")
    NEW_USER_EMAIL = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default")
