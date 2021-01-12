from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_product_to_basket()     # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()   # Посчитать результат математического выражения и ввести ответ
    page.should_be_alert_for_book_name()                    # Бинарные проверки на появление алерта.
    page.should_be_alert_that_said_book_was_added()          # Бинарные проверки на появление алерта.
    page.books_names_should_be_the_same()                   # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    page.books_prices_should_be_the_same()                  # Цена должна соответствовать заявленой.



