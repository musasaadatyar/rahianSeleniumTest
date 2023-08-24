from archives.locators.locators import *
from selenium.webdriver.common.by import By


class OrganizationSystem:
    def __init__(self, driver):
        self.driver = driver

    def click_organization_management_menu(self):
        self.driver.find_element(By.XPATH, system_management_btn_menu_xpath_locator).click()

    def click_organization_identity_menu(self):
        self.driver.find_element(By.XPATH, structure_organization_btn_menu_xpath_locator).click()

    def click_organization_role_menu(self):
        self.driver.find_element(By.XPATH, role_organization_btn_menu_xpath_locator).click()

    def click_user_management_menu(self):
        self.driver.find_element(By.XPATH, user_management_btn_menu_xpath_locator).click()

    def click_access_management_menu(self):
        self.driver.find_element(By.XPATH, user_access_management_btn_menu_xpath_locator).click()
