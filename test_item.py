import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)

    # Требование из критериев проверки: добавить паузу 30 секунд для визуальной проверки
    time.sleep(30)

    # Ищем кнопку добавления в корзину с помощью уникального селектора
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Проверяем с помощью assert, что кнопка действительно присутствует на странице
    assert len(buttons) > 0, "Кнопка добавления в корзину не найдена на странице!"
