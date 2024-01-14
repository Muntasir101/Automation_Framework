from pages.base_page import BasePage
from locators.locators_home_page import HomePageLocators


class HomePage(BasePage):
    # define home page actions
    def click_testCases(self):
        self.click_element(*HomePageLocators.TestCases)

    def click_signupLogin(self):
        self.click_element(*HomePageLocators.SIGNUP_LOGIN)
