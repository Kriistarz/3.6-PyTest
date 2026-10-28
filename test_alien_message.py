import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список ссылок из задания на Stepik
stepik_urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('link', stepik_urls)
def test_collect_alien_messages(browser, link):
    browser.get(link)

    time.sleep(20)

    # Вычисляем актуальный ответ на основе текущего времени (как указано в задании)
    answer = str(math.log(int(time.time())))

    # Находим поле ввода, очищаем и вводим ответ
    input_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
    )
    input_field.clear()
    input_field.send_keys(answer)

    # Нажимаем кнопку «Отправить»
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    submit_button.click()

    # Ожидаем появления опционального фидбека (черного блока с текстом)
    feedback = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )

    feedback_text = feedback.text

    # Проверяем, что текст равен "Correct!" (если нет — тест упадет и покажет скрытый кусочек)
    assert feedback_text == "Correct!", f"Найден кусочек сообщения: {feedback_text}"
