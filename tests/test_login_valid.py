from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.delete_account_page import DeleteAccountPage
from config.file_config import FileConfig
from config.log_config import LoggerConfig
from data.data_login import LoginData


def test_case2_login_valid(setup):
    home_page = HomePage(setup)
    base_page = BasePage(setup)
    login_page = LoginPage(setup)
    delete_account_page = DeleteAccountPage(setup)

    test_log_instance = LoggerConfig()

    # 1. open home page
    test_log_instance.logger.info("..........test_case2_login_valid Start.............")
    base_page.navigate_to_url("https://automationexercise.com/")
    test_log_instance.logger.info("Open home page successfully...")

    # 2. Navigate to url 'http://automationexercise.com'
    base_page.navigate_to_url("https://automationexercise.com/")

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
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE2 + "\\verify_login_page.png")

    # 6. Enter correct email address and password
    login_page.enter_login_email(LoginData.valid_email)
    test_log_instance.logger.info("Enter correct Email address successfully..")

    login_page.enter_login_password(LoginData.valid_password)
    test_log_instance.logger.info("Enter correct Password address successfully..")

    # 7. Click 'login' button
    login_page.click_login_button()
    test_log_instance.logger.info("Click 'login' button successfully..")

    # 8. Verify that 'Logged in as username' is visible
    assert home_page.get_logged_user_name_text(), "Logged in as " + LoginData.valid_name
    test_log_instance.logger.info("Verify that 'Logged in as username' is visible")
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE2 + "\\verify_logged.png")

    """
    # 9. Click 'Delete Account' button
    home_page.click_delete_account()
    test_log_instance.logger.info("Click 'Delete Account' button successfully..")

    # 10. Verify that 'ACCOUNT DELETED!' is visible
    assert delete_account_page.get_delete_account_text(), "ACCOUNT DELETED!"
    test_log_instance.logger.info("Verify that 'ACCOUNT DELETED!' is visible")
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_TESTCASE1 + "\\verify_account_deleted.png")
    """

    test_log_instance.logger.info("All steps complete successfully......")
    test_log_instance.logger.info("..........test_case2_login_valid END.............")
    test_log_instance.logger.info(".......................")
