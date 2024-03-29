import os


class FileConfig:
    SCREENSHOT_FILE_LOCATION_COMMON = os.path.join(os.getcwd(), 'Screenshots', 'common')
    SCREENSHOT_FILE_LOCATION_TESTCASE1 = os.path.join(os.getcwd(), 'Screenshots', 'tc1_registration')
    SCREENSHOT_FILE_LOCATION_TESTCASE2 = os.path.join(os.getcwd(), 'Screenshots', 'tc2_login_valid')
    SCREENSHOT_FILE_LOCATION_TESTCASE3 = os.path.join(os.getcwd(), 'Screenshots', 'tc3_login_invalid')
    SCREENSHOT_FILE_LOCATION_TESTCASE4 = os.path.join(os.getcwd(), 'Screenshots', 'tc4_logout')