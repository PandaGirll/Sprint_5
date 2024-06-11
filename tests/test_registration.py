from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators


# Содаём класс для проверки регистрации
class TestRegistration:
    # Проверяем успешную регистрацию
    def test_successful_registration(self, driver, test_email, test_password):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)
        # Используем функцию для регистрации
        AuthHelper.registration(driver, test_email, test_password, )
        # Проверяем перенаправление на страницу логина после регистрации
        AuthHelper.confirm_registration_success(driver)
        # Проверяем текущий URL и ожидаемый результат
        current_url = driver.current_url
        expected_result = TestLinks.login_page_link
        assert expected_result == current_url, (
            "Ошибка перехода на страницу логина после успешной регистрации."
        )

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
        driver.find_element(
            *TestLocators.PASSWORD_LOCATOR).send_keys(invalid_pass)
        # Клик по кнопке регистрации
        driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()
        # Ожидаем сообщение об ошибке
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                TestLocators.WRONG_PASS_MESSAGE_LOCATOR)).text
        expected_error_msg = "Некорректный пароль"
        assert expected_error_msg == error_message, (
            "Не отображается сообщение о некорректном пароле."
        )
