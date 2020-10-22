from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form .btn')
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, '#messages .alert:first-child > .alertinner strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, '#content_inner h1')
    MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, '#messages .alert:last-child > .alertinner strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '#content_inner .price_color')
