from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def get_driver(self):
        return self.driver

    def quit(self):
        self.driver.quit()