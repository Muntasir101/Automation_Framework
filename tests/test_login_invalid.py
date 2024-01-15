from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.delete_account_page import DeleteAccountPage
from config.file_config import FileConfig
from config.log_config import LoggerConfig
from data.data_login import LoginData


def test_case3_login_invalid(setup):
    home_page = HomePage(setup)
    base_page = BasePage(setup)
    login_page = LoginPage(setup)

    test_log_instance = LoggerConfig()

    # 2. Navigate to url 'http://automationexercise.com'
    base_page.navigate_to_url("https://automationexercise.com/")
    test_log_instance.logger.info("....Start: test_case3_login_invalid.............")

    # 3. Verify that home page is visible successfully
    assert base_page.get_page_title(), "Automation Exercise"
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE2 + "\\verify_home_page.png")
    test_log_instance.logger.info("Verify home page is visible successfully.")

    # 4. Click on 'Signup / Login' button
    home_page.click_signupLogin()
    test_log_instance.logger.info("Click on 'Signup / Login' button successfully..")

    # 5. Verify 'Login to your account' is visible
    assert login_page.get_login_account_text(), "Login to your account"
    test_log_instance.logger.info("Verify 'Login to your account' is visible successfully..")
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE3 + "\\verify_login_page.png")

    # 6. Enter incorrect email address and password
    login_page.enter_login_email(LoginData.invalid_email)
    test_log_instance.logger.info("Enter correct Email address successfully..")

    login_page.enter_login_password(LoginData.invalid_password)
    test_log_instance.logger.info("Enter correct Password address successfully..")

    # 7. Click 'login' button
    login_page.click_login_button()
    test_log_instance.logger.info("Click 'login' button successfully..")

    # 8. Verify error 'Your email or password is incorrect!' is visible
    assert login_page.get_login_error_text(), "Your email or password is incorrect!"
    test_log_instance.logger.info("Verify error 'Your email or password is incorrect!' is visible")
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE3 + "\\verify_error_message.png")

    test_log_instance.logger.info("All steps complete successfully......")
    test_log_instance.logger.info("..........End: test_case3_login_invalid.............")
    test_log_instance.close_logger()
