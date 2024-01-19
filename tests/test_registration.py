from data.data_login import LoginData
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage
from data.data_create_user import RegistrationData
from config.file_config import FileConfig
from config.log_config import LoggerConfig


def test_case1_registration(setup):

    base_page = BasePage(setup)

    home_page = HomePage(setup)

    signup_page = SignupPage(setup)
    login_page = LoginPage(setup)

    account_created_page = AccountCreatedPage(setup)
    delete_account_page = DeleteAccountPage(setup)
    test_log_instance = LoggerConfig()

    # 1. open home page
    test_log_instance.logger.info("....Start: test_case1_registration.............")
    base_page.navigate_to_url("https://automationexercise.com/")
    test_log_instance.logger.info("Open home page successfully...")

    # 2. Navigate to url 'http://automationexercise.com'
    base_page.navigate_to_url("https://automationexercise.com/")

    # 3. Verify that home page is visible successfully
    assert base_page.get_page_title(), "Automation Exercise"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_home_page.png")
    test_log_instance.logger.info("Verify home page is visible successfully.")

    # 4. Click on 'Signup / Login' button
    home_page.click_signupLogin()
    test_log_instance.logger.info("Click on 'Signup / Login' button successfully..")

    # 5. Verify 'New User Signup!' is visible
    assert login_page.get_new_user_signup_text(), "New User Signup!"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_new_user_signup.png")
    test_log_instance.logger.info("Verify 'New User Signup!' is visible successfully..")

    # 6. Enter name and email address
    login_page.enter_name(RegistrationData.name)
    login_page.enter_email(RegistrationData.email)
    test_log_instance.logger.info("Enter name and email address successfully..")

    # 7. Click 'Signup' button
    login_page.click_signup_button()
    test_log_instance.logger.info("Click 'Signup' button successfully..")

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert signup_page.get_enter_account_information_text(), "Enter Account Information"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_enter_account_info.png")
    test_log_instance.logger.info("Verify 'ENTER ACCOUNT INFORMATION' is visible successfully..")

    # 9. Fill details: Title, Name, Email, Password, Date of birth
    signup_page.select_title()
    test_log_instance.logger.info("Title select successfully..")
    signup_page.enter_password("123456")
    test_log_instance.logger.info("Enter Password successfully..")
    signup_page.select_day("20")
    test_log_instance.logger.info(signup_page.get_day_dropdown_all_options())
    signup_page.get_day_dropdown_all_options()
    test_log_instance.logger.info("Select Day successfully..")
    signup_page.select_month("5")
    test_log_instance.logger.info("Select Month successfully..")
    signup_page.select_year("2000")
    test_log_instance.logger.info("Select Year successfully..")

    # 10. Select checkbox 'Sign up for our newsletter!'
    signup_page.click_news_letter()
    test_log_instance.logger.info("Select checkbox 'Sign up for our newsletter! successfully..")

    # 11. Select checkbox 'Receive special offers from our partners!'
    signup_page.click_special_offer()
    test_log_instance.logger.info("Select checkbox 'Receive special offers from our partners! successfully..")

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    signup_page.enter_first_name(RegistrationData.name)
    test_log_instance.logger.info("Enter First name successfully..")
    signup_page.enter_last_name(RegistrationData.name)
    test_log_instance.logger.info("Enter Last name successfully..")
    signup_page.enter_address1("NY")
    test_log_instance.logger.info("Enter Address 1 successfully..")
    signup_page.enter_address2("land")
    test_log_instance.logger.info("Enter Address 2 successfully..")
    signup_page.select_country("United States")
    test_log_instance.logger.info("Select Country successfully..")
    signup_page.enter_state("United")
    test_log_instance.logger.info("Enter State successfully..")
    signup_page.enter_city("United States")
    test_log_instance.logger.info("Enter City successfully..")
    signup_page.enter_zipcode("12233")
    test_log_instance.logger.info("Enter Zipcode successfully..")
    signup_page.enter_mobile("12345678")
    test_log_instance.logger.info("Enter Mobile successfully..")

    # 13. Click 'Create Account button'
    signup_page.click_create_account_button()
    test_log_instance.logger.info("Click 'Create Account button successfully..'")

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    assert account_created_page.get_account_created_text(), "ACCOUNT CREATED!"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_account_created.png")
    test_log_instance.logger.info("Verify 'ACCOUNT CREATED!' is visible'")

    # 15. Click 'Continue' button
    account_created_page.click_continue_button()
    test_log_instance.logger.info("Click 'Continue' button' successfully..")

    # 16. Verify that 'Logged in as username' is visible
    assert home_page.get_logged_user_name_text(), "Logged in as " + RegistrationData.name
    test_log_instance.logger.info("Verify that 'Logged in as username' is visible")

    # 17. Click 'Delete Account' button
    home_page.click_delete_account()
    test_log_instance.logger.info("Click 'Delete Account' button successfully..")

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert delete_account_page.get_delete_account_text(), "ACCOUNT DELETED!"
    test_log_instance.logger.info("Verify that 'ACCOUNT DELETED!' is visible")
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_account_deleted.png")
    delete_account_page.click_continue_button()
    test_log_instance.logger.info("click 'Continue' button successfully..")

    test_log_instance.logger.info("All steps complete successfully......")
    test_log_instance.logger.info("..........End: test_case1_registration.............")
    test_log_instance.close_logger()
