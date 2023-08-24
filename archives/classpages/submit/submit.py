from archives.locators.locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Submit:
    def __init__(self, driver):
        self.driver = driver

    def enter_submit_button_link_login(self):
        element = self.driver.find_element(By.XPATH,
                                           submit_button_xpath_login_locator)
        element.click()

    def enter_national_code(self, national_code):
        element = self.driver.find_element(By.ID, national_cod_submit_id_locator)
        # element.send_keys(national_code)
        ActionChains(self.driver).send_keys_to_element(element, national_code).perform()

    def clear_enter_national_code(self):
        self.driver.find_element(By.ID, national_cod_submit_id_locator).clear()

    def enter_phone_number(self, phone_number):
        element = self.driver.find_element(By.ID, phone_number_submit_id_locator)
        ActionChains(self.driver).send_keys_to_element(element, phone_number).perform()

    def clear_enter_phone_number(self):
        self.driver.find_element(By.ID, phone_number_submit_id_locator).clear()

    def enter_birth_date(self, birth_date):
        element = self.driver.find_element(By.ID, birthday_submit_id_locator)
        element.send_keys(birth_date)

    def clear_enter_birth_date(self):
        self.driver.find_element(By.ID, birthday_submit_id_locator).clear()

    def enter_password(self, password):
        element = self.driver.find_element(By.ID, password_submit_id_locator)
        ActionChains(self.driver).send_keys_to_element(element, password).perform()

    def clear_enter_password(self):
        self.driver.find_element(By.ID, password_submit_id_locator).clear()

    def confirm_password(self, confirm_password):
        element = self.driver.find_element(By.ID, confirm_password_submit_id_locator)
        ActionChains(self.driver).send_keys_to_element(element, confirm_password).perform()

    def clear_confirm_password(self):
        self.driver.find_element(By.ID, confirm_password_submit_id_locator).clear()

    def click_submit_btn(self):
        element = self.driver.find_element(By.ID, button_submit_id_locator)
        element.click()

    def enter_users_link(self):
        element = self.driver.find_element(By.LINK_TEXT, input_users_button_link)
        element.click()

    def click_submit_enter_submit_main_page(self):
        self.driver.find_element(By.XPATH, enter_submit_button_main_page_locator).click()
