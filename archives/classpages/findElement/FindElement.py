class FindElement:
    def __init(self, driver):
        self.driver = driver

    def find_element(self, find_by, element_locator):
        self.driver.find_element(find_by, element_locator).location_once_scrolled_into_view
