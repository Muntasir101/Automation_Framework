from pages.base_page import BasePage
from locators.locators_account_created_page import AccountCreatedLocators


class AccountCreatedPage(BasePage):
    # define account create page actions
    def get_account_created_text(self):
        return self.get_element_text(*AccountCreatedLocators.ACCOUNT_CREATED_TEXT)

    def click_continue_button(self):
        self.click_element(*AccountCreatedLocators.CONTINUE_BUTTON)

    def logged_in_username_text(self):
        return self.get_element_text(*AccountCreatedLocators.LOGIN_USERNAME_TEXT)
