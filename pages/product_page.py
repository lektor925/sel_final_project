import math

from selenium.common.exceptions import NoAlertPresentException

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        self.should_be_cart_button()
        self.add_product_to_cart()
        self.solve_quiz_and_get_code()
        self.should_be_added_product_message()
        self.should_be_price_product_message()

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON), "Cart button is not presented"

    def add_product_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        cart_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_added_product_message(self):
        prod_mess = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT).text
        prod_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert prod_mess == prod_name, 'Название продукта не соответствует сообщению'

    def should_be_price_product_message(self):
        price_mess = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_PRODUCT).text
        prod_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_mess == prod_price, 'Цена продукта не соответствует сообщению'
