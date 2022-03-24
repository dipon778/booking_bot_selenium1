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
        # currency_select = self.find_element(By.CSS_SELECTOR,
        #                                     'div.bui-group__item:nth-child(13) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')
        currency_select = self.find_element(By.CSS_SELECTOR,
                                            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        currency_select.click()

    def select_place(self, place=None):
        place_element = self.find_element(By.ID, 'ss')
        place_element.clear()
        place_element.send_keys(place)
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, ch_in, ch_out):
        ch_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{ch_in}"]')
        ch_in_element.click()
        ch_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{ch_out}"]')
        ch_out_element.click()

    def select_adults(self, adults=1):
        selection_of_adult_count = self.find_element(By.ID, 'xp__guests__toggle')
        selection_of_adult_count.click()

        decrease_adult_element = self.find_element(By.CSS_SELECTOR,
                                                   'div.sb-group__field:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(2)')

        increase_adults_elements = self.find_element(By.CSS_SELECTOR,
                                                     '#xp__guests__inputs-container > div > div > div.sb-group__field.sb-group__field-adults > div > div.bui-stepper__wrapper.sb-group__stepper-a11y > button.bui-button.bui-button--secondary.bui-stepper__add-button')

        # Collecting the number of adults value
        number_of_adults = self.find_element(By.ID, 'group_adults')
        print(number_of_adults.get_attribute("value"))

        while True:
            decrease_adult_element.click()
            if( int(number_of_adults.get_attribute("value")) == 1):
                break

        for i in range(adults - 1):
            increase_adults_elements.click()

    def click_search(self):
        place_search = self.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div[1]/div[4]/div[2]/button')
        place_search.click()

