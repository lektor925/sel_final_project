import math

from selenium.common.exceptions import NoAlertPresentException

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        self.should_be_cart_button()
        self.add_product_to_cart()
        self.solve_quiz_and_get_code()

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
