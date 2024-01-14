import time

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage


def test_case1_registration(setup):
    sign_login_page = SignupLoginPage(setup)
    home_page = HomePage(setup)
    base_page = BasePage(setup)

    # 1. open home page
    base_page.navigate_to_url("https://automationexercise.com/")

    # 2. Navigate to url 'http://automationexercise.com'
    base_page.navigate_to_url("https://automationexercise.com/")

    # 3. Verify that home page is visible successfully
    assert base_page.get_page_title(), "Automation Exercise"

    # 4. Click on 'Signup / Login' button
    home_page.click_signupLogin()

    # 5. Verify 'New User Signup!' is visible
    assert sign_login_page.get_new_user_signup_text(), "New User Signup!"

    # 6. Enter name and email address
    sign_login_page.enter_name("Admin")
    sign_login_page.enter_email("admin@automationexercise.com")

    # 7. Click 'Signup' button
    sign_login_page.click_signup_button()

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert sign_login_page.get_enter_account_information_text(), "Enter Account Information"

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
    time.sleep(8)

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number

    # 13. Click 'Create Account button'

    # 14. Verify that 'ACCOUNT CREATED!' is visible

    # 15. Click 'Continue' button

    # 16. Verify that 'Logged in as username' is visible

    # 17. Click 'Delete Account' button

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
