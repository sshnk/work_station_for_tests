from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


# параметрезируем тест и проверяем разные промо акции. Что бы не дублировать тест - мы его параметризируем и
# проверяем сразу 10 промо акций в одном тесте.
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail(reason='now this link is broken, known bug')),  #
                                  # данный маркер показывает что тест падает и мы знаем об этом, если он вдруг
                                  # пройдёт на это нужно обратить внимание
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # бинарная проверка, блок с алертом, что в карзину что то добавлено не
    # должен быть отображен
    page.message_should_disappeared()  # Дополнительная проверка, что такой алерт вообще присутствует, но в нашем
    # случае не появился.
    page.add_product_to_basket()  # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()  # Посчитать результат математического выражения и ввести ответ
    page.should_be_alert_for_book_name()  # Бинарные проверки на появление алерта.
    page.should_be_alert_that_said_book_was_added()  # Бинарные проверки на появление алерта.
    page.books_names_should_be_the_same()  # Название товара в сообщении должно совпадать с тем товаром, который вы
    # действительно добавили.
    page.books_prices_should_be_the_same()  # Цена должна соответствовать заявленой.


# специально сломанный тест для проверок - он помечен маркером
@pytest.mark.xfail(reason="broken test for tasks")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()  # Бинарная проверка на отсутствие уведамления


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # Бинарная проверка на отсутствие уведамления


# специально сломанный тест для проверок - он помечен маркером
@pytest.mark.xfail(reason="broken test for tasks")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_should_disappeared()  # уведомление должно пропадать


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()  # ожидаем url с соответствующим параметром


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # у пользователя есть возможность перейти на страницу с логином


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basketpage()  # у пользователя есть возможность перейти на страницу "Корзина"
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_notification()  # корзина должна быть пуста
    basket_page.should_not_be_product_notification()  # уведомлений не должно быть


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):  # создаём рандомного нового юзера перед проверками
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "gfjdksgjfdksgjfdk1212432")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):  # все тесты которые делались для гостевого пользователя,
        # делаем для залогиненого пользователя
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"  # сылку взяли с
        # промоофером, дополнительно проверить, что промо акции для залогиненого пользователя работают.
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.message_should_disappeared()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_alert_for_book_name()
        page.should_be_alert_that_said_book_was_added()
        page.books_names_should_be_the_same()
        page.books_prices_should_be_the_same()
