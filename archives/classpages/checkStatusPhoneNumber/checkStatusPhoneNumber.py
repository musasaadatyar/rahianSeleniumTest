from archives.locators.locators import *
from selenium.webdriver.common.by import By


class CheckStatusPhoneNumber:
    def __init__(self, driver):
        self.driver = driver

    def enter_submit_button_link_login(self):
        element = self.driver.find_element(By.XPATH,
                                           button_check_phone_number_xpath_locator)
        element.click()

    def enter_confirm_phone_number_link(self):
        element = self.driver.find_element(By.LINK_TEXT,
                                           confirm_phone_number_Link_text_locator)
        element.click()

    def close_pup_up_btn(self):
        element = self.driver.find_element(By.XPATH, close_btn_pup_up_xpath)
        if element:
            element.click()
            return element
