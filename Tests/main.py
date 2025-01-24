import time
from driver.driver import WebDriver
from Pages.home_page import HomePage

def test_ui():
    web_driver = WebDriver()
    driver = web_driver.get_driver()

    try:
        driver.get("https://www.varzesh3.com/")
        home_page = HomePage(driver)
        home_page.click_login()
        home_page.input_phone_number()
        home_page.click_next_button()
        home_page.input_password()
        home_page.click_login_button()
        home_page.click_user_account()
        home_page.click_View_user_account()
        time.sleep(2)
        home_page.verify_user_account_text()
    finally:
        web_driver.quit()


test_ui()