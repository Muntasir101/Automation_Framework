from pages.base_page import BasePage
from locators.locators_signup_login_page import SignupLoginPageLocators


class SignupLoginPage(BasePage):
    # define signup page actions
    def type_name(self):
        self.input_text(*SignupLoginPageLocators.NEW_USER_NAME, "Admin")

    def type_password(self):
        self.input_text(*SignupLoginPageLocators.NEW_USER_EMAIL, "Admin@mail.com")

    def click_signupButton(self):
        self.click_element(*SignupLoginPageLocators.SIGNUP_BUTTON)
