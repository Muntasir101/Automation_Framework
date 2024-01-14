from pages.base_page import BasePage
from pages.home_page import HomePage


def test_home(setup):
    # open home page
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://automationexercise.com/")

    # go to Test Cases page
    home_page = HomePage(setup)
    home_page.click_testCases()
