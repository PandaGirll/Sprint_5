import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestLinks, AuthHelper


# Содаём класс для проверки регистрации
class TestRegistration:

    # Проверяем успешную регистрацию
    def test_successful_registration(self, driver, test_email, test_password):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)

        # Используем универсальную функцию для регистрации
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)

        # Ожидаем перенаправление на страницу логина после успешной регистрации
        WebDriverWait(driver, 5).until(EC.url_to_be(TestLinks.login_page_link))

        # Проверяем текущий URL и ожидаемый результат
        current_url = driver.current_url
        expected_result = TestLinks.login_page_link
        assert expected_result == current_url, "Ошибка перехода на страницу логина после успешной регистрации."

    # Проверяем ошибку для некорректного пароля
    def test_invalid_password_registration(self, driver, test_email):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)
        invalid_pass = "123"

        # Ввод имени пользователя
        driver.find_element(*TestLocators.NAME_LOCATOR).send_keys("Тест")
        # Ввод email
        driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(test_email)
        # Ввод некорректного пароля
        driver.find_element(*TestLocators.PASSWORD_LOCATOR).send_keys(invalid_pass)
        # Клик по кнопке регистрации
        driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()

        # Ожидаем сообщение об ошибке
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.WRONG_PASS_MESSAGE_LOCATOR)).text
        expected_error_msg = "Некорректный пароль"
        assert expected_error_msg == error_message, "Не отображается сообщение о некорректном пароле."
