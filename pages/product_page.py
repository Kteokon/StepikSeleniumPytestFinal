from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # def should_be_product_url(self):
    #     print(self.browser.current_url)
    #     assert "catalogue/coders-at-work_207/?promo=offer" == self.browser.current_url[self.browser.current_url.find("catalogue"):-1] #and self.get_product_name() == name and self.get_product_price() == price
    #     # assert True

    def should_be_add_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON), "No button to add the product"

    def add_product(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        button.click()

    def should_be_product_added(self, name, price):
        message_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE1).text
        message_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE2).text
        assert message_name == name and message_price == price