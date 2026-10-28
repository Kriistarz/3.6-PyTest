from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        """Нажатие на кнопку добавления в корзину"""
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        """Возвращает динамическое название товара со страницы"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает динамическую цену товара со страницы"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_message_about_adding(self, product_name, product_price):
        """Проверяет, что название и цена в сообщении совпадают с переданными аргументами"""
        # Считываем текст из всплывающих сообщений
        message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        message_product_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE).text

        # Сравниваем полученное сообщение с переданным названием товара
        assert product_name == message_product_name, (
            f"Название товара в сообщении не совпадает! Ожидалось: '{product_name}', получено: '{message_product_name}'"
        )
        # Сравниваем полученную цену с переданной ценой
        assert product_price == message_product_price, (
            f"Цена товара в сообщении не совпадает! Ожидалось: '{product_price}', получено: '{message_product_price}'"
        )
