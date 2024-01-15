from config.file_config import FileConfig
from config.log_config import LoggerConfig
from pages.base_page import BasePage


def test_home(setup):
    test_log_instance = LoggerConfig()
    # open home page
    test_log_instance.logger.info("....Start: test_home.............")
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://automationexercise.com/")
    test_log_instance.logger.info("Home page open successfully..")
    base_page.take_screenshot(FileConfig.SCREENSHOT_FILE_LOCATION_COMMON + "\\verify_home_page.png")
    test_log_instance.logger.info("..........End: test_home.............")
    test_log_instance.close_logger()
