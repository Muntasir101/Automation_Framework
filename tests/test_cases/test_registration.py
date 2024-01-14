from pages.base_page import BasePage
from pages.signup_login_page import SignupLoginPage


def test_home(setup):
    # open home page
    # 2. Navigate to url 'http://automationexercise.com'
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://automationexercise.com/")

    # 3. Verify that home page is visible successfully
    # Verify that the home page is visible
    assert base_page.get_page_title(), "Automation Exercise"

