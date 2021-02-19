from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket = self.browser.find_element(*ProductPageLocators.BUSKET_LINK)
        add_product_to_basket.click()


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

    def should_be_alert_for_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not presented"

    def should_be_alert_that_said_book_was_added(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Alert is not presented"

    def books_names_should_be_the_same(self):
        book_name_in_busket = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_PAGE).text
        assert book_name == book_name_in_busket, "Titels of books are different"

    def books_prices_should_be_the_same(self):
        book_price_in_busket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_PAGE).text
        assert book_price == book_price_in_busket, "Prices of books are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Something wrong with test 'should_not_be_success_message or our locator was missed"

