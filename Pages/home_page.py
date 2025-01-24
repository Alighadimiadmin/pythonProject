from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".login"))
        )
        element.click()

    def input_phone_number(self):

        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "phone"))
        )
        element.send_keys("09195099029")

    def click_next_button(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "login-btn"))
        )
        element.click()

    def input_password(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "Password"))
        )
        element.send_keys("Gh@123456")

    def click_login_button(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "button"))
        )
        element.click()

    def click_user_account(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='dropdownMenuButton']/img[@alt='حساب کاربری']"))
        )
        element.click()

    def click_View_user_account(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'مشاهده حساب کاربری')]"))
        )
        element.click()

    def verify_user_account_text(self):
        expected_text = "علی171717"

        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[.='علی171717']"))
        )

        actual_text = element.text.strip()
        print(f"متن واقعی عنصر: '{actual_text}'")

        assert actual_text == expected_text, f"متن عنصر مطابق انتظار نبود. متن واقعی: '{actual_text}', متن مورد انتظار : '{expected_text}'"


