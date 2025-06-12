from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_url(self, name, price):
        assert "catalogue" in self.browser.current_url

    def should_be_add_product_button(self, name, price):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "No button to add the product"

    def add_product(self, name, price):
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        print(f"Товар {name} по цене {price} был добавлен в корзину")
        button.click()