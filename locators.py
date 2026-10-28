from selenium.webdriver.common.by import By

class BasePageLocators():
    pass

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    # Кнопка добавления в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    # Название товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    # Цена товара
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")
    # Название товара в сообщении об успехе
    SUCCESS_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    # Цена товара в сообщении об успехе
