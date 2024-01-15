from pages.base_page import BasePage
from locators.locators_login_page import LoginPageLocators
from locators.locators_signup_page import SignupPageLocators


class LoginPage(BasePage):
    # define signup page actions

    def get_new_user_signup_text(self):
        return self.get_element_text(*LoginPageLocators.NEW_USER_SIGNUP)

    def enter_name(self, username):
        self.input_text(*LoginPageLocators.NEW_USER_NAME, text=username)

    def enter_email(self, email):
        self.input_text(*LoginPageLocators.NEW_USER_EMAIL, text=email)

    def click_signup_button(self):
        self.click_element(*LoginPageLocators.SIGNUP_BUTTON)
