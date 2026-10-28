import pytest
from pages.product_page import ProductPage

# Список ссылок с параметрами от offer0 до offer9,
# где один из них содержит баг (по заданию курса, это обычно offer7, но проверим автотестом)
urls = [
    f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}"
    for i in range(10)
]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    # Считываем название и цену ДО добавления
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Добавляем в корзину и решаем квиз
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    # Проверяем корректность сообщения об успехе
    page.should_be_message_about_adding(product_name, product_price)

    page.should_be_message_about_adding(product_name, product_price)
