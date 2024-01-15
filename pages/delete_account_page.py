from pages.base_page import BasePage
from locators.locators_delete_account_page import DeleteAccountLocators


class DeleteAccountPage(BasePage):
    # define delete page actions
    def get_delete_account_text(self):
        return self.get_element_text(*DeleteAccountLocators.ACCOUNT_DELETED_TEXT)

    def click_continue_button(self):
        self.click_element(*DeleteAccountLocators.CONTINUE_BUTTON)

