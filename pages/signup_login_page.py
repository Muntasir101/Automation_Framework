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

    def get_new_user_signup_text(self):
        return self.get_element_text(*SignupLoginPageLocators.NEW_USER_SIGNUP)

    def get_enter_account_information_text(self):
        return self.get_element_text(*SignupLoginPageLocators.ENTER_ACCOUNT_INFORMATION)

    def select_title(self):
        self.click_element(*SignupLoginPageLocators.TITLE)

    def enter_password(self, password):
        self.input_text(*SignupLoginPageLocators.PASSWORD, text=password)

    def select_day(self, value):
        self.select_dropdown_option_by_value(*SignupLoginPageLocators.DAY, value)

    def select_month(self, value):
        self.select_dropdown_option_by_value(*SignupLoginPageLocators.MONTH, value)

    def select_year(self, value):
        self.select_dropdown_option_by_value(*SignupLoginPageLocators.YEAR, value)

    def click_news_letter(self):
        self.click_element(*SignupLoginPageLocators.NEWS_LETTER)

    def click_special_offer(self):
        self.click_element(*SignupLoginPageLocators.SPECIAL_OFFER)

    def enter_first_name(self, firstname):
        self.input_text(*SignupLoginPageLocators.FIRST_NAME, text=firstname)

    def enter_last_name(self, lastname):
        self.input_text(*SignupLoginPageLocators.LAST_NAME, text=lastname)

    def enter_company(self, company):
        self.input_text(*SignupLoginPageLocators.COMPANY, text=company)

    def enter_address1(self, address1):
        self.input_text(*SignupLoginPageLocators.ADDRESS1, text=address1)

    def enter_address2(self, address2):
        self.input_text(*SignupLoginPageLocators.ADDRESS2, text=address2)

    def select_country(self, value):
        self.select_dropdown_option_by_value(*SignupLoginPageLocators.COUNTRY, value)

    def enter_state(self, state):
        self.input_text(*SignupLoginPageLocators.STATE, text=state)

    def enter_city(self, city):
        self.input_text(*SignupLoginPageLocators.CITY, text=city)

    def enter_zipcode(self, zipcode):
        self.input_text(*SignupLoginPageLocators.ZIPCODE, text=zipcode)

    def enter_mobile(self, mobile):
        self.input_text(*SignupLoginPageLocators.MOBILE, text=mobile)

    def click_create_account_button(self):
        self.click_element(*SignupLoginPageLocators.CREATE_ACCOUNT_BUTTON)

