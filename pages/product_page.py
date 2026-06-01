from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    CART_CONFIRMATION = (By.CSS_SELECTOR, "#sw-atc-details-single-container")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def is_added_to_cart(self):
        return self.wait_for(self.CART_CONFIRMATION)
