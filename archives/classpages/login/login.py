from archives.locators.locators import *
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, national_cod_login_id_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, password_login_id_locator).send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element(By.XPATH, enter_user_button_login_xpath_locator).click()

    def click_on_submit_btn(self):
        self.driver.find_element(By.LINK_TEXT, submit_button_link_login_locator).click()

    def click_conform_phon_number(self):
        self.driver.find_element(By.LINK_TEXT, conform_phone_link_login_locator).click()

    def click_submit_enter_submit_main_page(self):
        self.driver.find_element(By.XPATH, enter_submit_button_main_page_locator).click()
