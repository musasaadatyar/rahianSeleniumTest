from archives.locators.locators import *
from selenium.webdriver.common.by import By


class SubmitPhoneNumber:
    def __init__(self, driver):
        self.driver = driver

    def enter_phone_number(self, phone_number):
        element = self.driver.find_element(By.ID, phone_number_submit_phone_id_locator).location_once_scrolled_into_view
        element.send_key(phone_number)

    def enter_national_code(self, national_code):
        element = self.driver.find_element(By.ID, national_cod_submit_id_locator).location_once_scrolled_into_view
        element.send_key(national_code)

    def click_confirm_phone_number_btn_click(self):
        element = self.driver.find_element(By.XPATH,
                                           confirm_number_submit_phone_xpath_locator).location_once_scrolled_into_view
        element.click()

    def enter_users_link_btn(self):
        element = self.driver.find_element
