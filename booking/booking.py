import booking.constant as constant
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r'/usr/local/bin/chromedriver', teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(5)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(constant.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, "div.bui-group__item:nth-child(1) > button:nth-child(1)")
        print("this line is executing")
        currency_element.click()
        currency_select = self.find_element(By.CSS_SELECTOR, 'div.bui-group__item:nth-child(13) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')
        currency_select.click()
