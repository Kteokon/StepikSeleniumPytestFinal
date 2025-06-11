from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "No button to add the product"

    def add_product(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        button.click()