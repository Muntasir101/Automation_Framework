from pages.base_page import BasePage
from locators.locators_login_page import LoginPageLocators


class LoginPage(BasePage):
    # define login page actions
    def get_login_account_text(self):
        return self.get_element_text(*LoginPageLocators.LOGIN_ACCOUNT)

    def enter_login_email(self, username):
        self.input_text(*LoginPageLocators.LOGIN_EMAIL, text=username)

    def enter_login_password(self, password):
        self.input_text(*LoginPageLocators.LOGIN_PASSWORD, text=password)

    def click_login_button(self):
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)

    def get_new_user_signup_text(self):
        return self.get_element_text(*LoginPageLocators.NEW_USER_SIGNUP)

    def enter_name(self, username):
        self.input_text(*LoginPageLocators.NEW_USER_NAME, text=username)

    def enter_email(self, email):
        self.input_text(*LoginPageLocators.NEW_USER_EMAIL, text=email)

    def click_signup_button(self):
        self.click_element(*LoginPageLocators.SIGNUP_BUTTON)
