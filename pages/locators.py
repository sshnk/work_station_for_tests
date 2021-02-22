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

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')

class BasketPageLocators():
    BASKET_NOTIFICATION = (By.CSS_SELECTOR, "#content_inner > p")

    PRODUCT_IN_BASKET = (By.XPATH, '//*[@id="content_inner"]/div[1]/div/h2')
