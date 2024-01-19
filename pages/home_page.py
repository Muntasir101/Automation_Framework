from pages.base_page import BasePage
from locators.locators_home_page import HomePageLocators


class HomePage(BasePage):
    # define home page actions
    def click_testCases(self):
        self.click_element(*HomePageLocators.TestCases)

    def click_signupLogin(self):
        self.click_element(*HomePageLocators.SIGNUP_LOGIN)

    def get_logged_user_name_text(self):
        return self.get_element_text(*HomePageLocators.LOGGED_IN_USER_NAME)

    def click_delete_account(self):
        self.click_element(*HomePageLocators.DELETE_ACCOUNT)

    def click_logout(self):
        self.click_element(*HomePageLocators.LOGOUT)

