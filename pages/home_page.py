from locators.locators_home_page import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    # define home page actions
    def login(self, username, password):
        self.click_element(*HomePageLocators.TestCases)
