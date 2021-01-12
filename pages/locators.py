from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUSKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    BOOK_NAME = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner  strong")

    BOOK_PRICE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner  strong")

    BOOK_NAME_IN_PAGE = (By.TAG_NAME, "h1")

    BOOK_PRICE_IN_PAGE = (By.CLASS_NAME, "col-sm-6.product_main .price_color")