from pages.base_page import BasePage
from locators.locators_signup_login_page import SignupLoginPageLocators


class SignupLoginPage(BasePage):
    # define signup page actions
    def enter_name(self, username):
        self.input_text(*SignupLoginPageLocators.NEW_USER_NAME, text=username)

    def enter_email(self, email):
        self.input_text(*SignupLoginPageLocators.NEW_USER_EMAIL, text=email)

    def click_signup_button(self):
        self.click_element(*SignupLoginPageLocators.SIGNUP_BUTTON)
