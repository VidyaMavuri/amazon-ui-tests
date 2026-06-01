from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def open(self):
        self.driver.get("https://www.amazon.com")

    def search(self, query):
        self.type(self.SEARCH_BOX, query)
        self.click(self.SEARCH_BUTTON)
