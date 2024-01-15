import os
import time

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage
from data.create_user import RegistrationData
from faker import Faker
from config.file_config import FileConfig


def test_case1_registration(setup):
    fake = Faker()

    sign_login_page = SignupLoginPage(setup)
    home_page = HomePage(setup)
    base_page = BasePage(setup)
    account_created_page = AccountCreatedPage(setup)
    delete_account_page = DeleteAccountPage(setup)

    # 1. open home page
    base_page.navigate_to_url("https://automationexercise.com/")

    # 2. Navigate to url 'http://automationexercise.com'
    base_page.navigate_to_url("https://automationexercise.com/")

    # 3. Verify that home page is visible successfully
    assert base_page.get_page_title(), "Automation Exercise"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_home_page.png")

    # 4. Click on 'Signup / Login' button
    home_page.click_signupLogin()

    # 5. Verify 'New User Signup!' is visible
    assert sign_login_page.get_new_user_signup_text(), "New User Signup!"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_new_user_signup.png")

    # 6. Enter name and email address
    sign_login_page.enter_name(RegistrationData.name)
    sign_login_page.enter_email(fake.email())

    # 7. Click 'Signup' button
    sign_login_page.click_signup_button()

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert sign_login_page.get_enter_account_information_text(), "Enter Account Information"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_enter_account_info.png")

    # 9. Fill details: Title, Name, Email, Password, Date of birth
    sign_login_page.select_title()
    sign_login_page.enter_password("123456")
    sign_login_page.select_day("20")
    sign_login_page.select_month("5")
    sign_login_page.select_year("2000")

    # 10. Select checkbox 'Sign up for our newsletter!'
    sign_login_page.click_news_letter()

    # 11. Select checkbox 'Receive special offers from our partners!'
    sign_login_page.click_special_offer()

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    sign_login_page.enter_first_name("John")
    sign_login_page.enter_last_name("smith")
    sign_login_page.enter_address1("NY")
    sign_login_page.enter_address2("land")
    sign_login_page.select_country("United States")
    sign_login_page.enter_state("United")
    sign_login_page.enter_city("United States")
    sign_login_page.enter_zipcode("12233")
    sign_login_page.enter_mobile("12345678")
    time.sleep(3)

    # 13. Click 'Create Account button'
    sign_login_page.click_create_account_button()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    assert account_created_page.get_account_created_text(), "ACCOUNT CREATED!"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_account_created.png")

    # 15. Click 'Continue' button
    account_created_page.click_continue_button()

    # 16. Verify that 'Logged in as username' is visible
    assert home_page.get_logged_user_name_text(), "Logged in as " + RegistrationData.name

    # 17. Click 'Delete Account' button
    home_page.click_delete_account()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert delete_account_page.get_delete_account_text(), "ACCOUNT DELETED!"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_account_deleted.png")
    delete_account_page.click_continue_button()

