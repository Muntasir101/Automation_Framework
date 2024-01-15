from pages.base_page import BasePage
from locators.locators_login_page import LoginPageLocators
from locators.locators_signup_page import SignupPageLocators


class SignupPage(BasePage):
    # define signup page actions
    def get_enter_account_information_text(self):
        return self.get_element_text(*SignupPageLocators.ENTER_ACCOUNT_INFORMATION)

    def select_title(self):
        self.click_element(*SignupPageLocators.TITLE)

    def enter_password(self, password):
        self.input_text(*SignupPageLocators.PASSWORD, text=password)

    def select_day(self, value):
        self.select_dropdown_option_by_value(*SignupPageLocators.DAY, value)

    def select_month(self, value):
        self.select_dropdown_option_by_value(*SignupPageLocators.MONTH, value)

    def select_year(self, value):
        self.select_dropdown_option_by_value(*SignupPageLocators.YEAR, value)

    def click_news_letter(self):
        self.click_element(*SignupPageLocators.NEWS_LETTER)

    def click_special_offer(self):
        self.click_element(*SignupPageLocators.SPECIAL_OFFER)

    def enter_first_name(self, firstname):
        self.input_text(*SignupPageLocators.FIRST_NAME, text=firstname)

    def enter_last_name(self, lastname):
        self.input_text(*SignupPageLocators.LAST_NAME, text=lastname)

    def enter_company(self, company):
        self.input_text(*SignupPageLocators.COMPANY, text=company)

    def enter_address1(self, address1):
        self.input_text(*SignupPageLocators.ADDRESS1, text=address1)

    def enter_address2(self, address2):
        self.input_text(*SignupPageLocators.ADDRESS2, text=address2)

    def select_country(self, value):
        self.select_dropdown_option_by_value(*SignupPageLocators.COUNTRY, value)

    def enter_state(self, state):
        self.input_text(*SignupPageLocators.STATE, text=state)

    def enter_city(self, city):
        self.input_text(*SignupPageLocators.CITY, text=city)

    def enter_zipcode(self, zipcode):
        self.input_text(*SignupPageLocators.ZIPCODE, text=zipcode)

    def enter_mobile(self, mobile):
        self.input_text(*SignupPageLocators.MOBILE, text=mobile)

    def click_create_account_button(self):
        self.click_element(*SignupPageLocators.CREATE_ACCOUNT_BUTTON)

