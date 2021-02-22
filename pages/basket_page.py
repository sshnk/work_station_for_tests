from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_notification(self):
        self.should_not_be_product()
        self.should_not_be_notification()

    def should_not_be_notification(self):
        # Должно быть уведомление, что карзина пуста.
        assert self.is_element_present(*BasketPageLocators.BASKET_NOTIFICATION)

    def should_not_be_product(self):
        # не должно быть товара в корзине
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)


