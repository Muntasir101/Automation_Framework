from selenium.webdriver.common.by import By


class SignupLoginPageLocators:
    # Define locators
    NEW_USER_NAME = (By.CSS_SELECTOR, "form[method='post'] > input[name='name']")
    NEW_USER_EMAIL = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default")
    NEW_USER_SIGNUP = (By.CSS_SELECTOR, ".signup-form h2")

    # Signup page
    ENTER_ACCOUNT_INFORMATION = (By.CSS_SELECTOR, ".login-form .text-center:nth-child(1) b")
    TITLE = (By.CSS_SELECTOR, "[action] .radio-inline:nth-child(3) [type]")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    DAY = (By.CSS_SELECTOR, "select#days")
    MONTH = (By.CSS_SELECTOR, "select#months")
    YEAR = (By.CSS_SELECTOR, "select#years")
    NEWS_LETTER = (By.CSS_SELECTOR, "input#newsletter")
    SPECIAL_OFFER = (By.CSS_SELECTOR, "input#optin")

    FIRST_NAME = (By.CSS_SELECTOR, "input#first_name")
    LAST_NAME = (By.CSS_SELECTOR, "input#last_name")
    COMPANY = (By.CSS_SELECTOR, "input#company")
    ADDRESS1 = (By.CSS_SELECTOR, "input[name='address1']")
    ADDRESS2 = (By.CSS_SELECTOR, "input[name='address2']")
    COUNTRY = (By.CSS_SELECTOR, "select#country")
    STATE = (By.CSS_SELECTOR, "input#state")
    CITY = (By.CSS_SELECTOR, "input#city")
    ZIPCODE = (By.CSS_SELECTOR, "input#zipcode")
    MOBILE = (By.CSS_SELECTOR, "input#mobile_number")

    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[action] .btn-default")

