from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from generator import Generator
from locators import TestLocators


# Ссылки на страницы
class TestLinks:
    main_page_link = "https://stellarburgers.nomoreparties.site/"
    login_page_link = "https://stellarburgers.nomoreparties.site/login"
    registration_page_link = "https://stellarburgers.nomoreparties.site/register"
    forgot_password_page_link = "https://stellarburgers.nomoreparties.site/forgot-password"
    personal_account_page_link = "https://stellarburgers.nomoreparties.site/account/profile"


# Универсальная функция для регистрации и авторизации
class AuthHelper:
    @staticmethod
    def authenticate(driver, email, password, is_registration=False):
        while True:
            if is_registration:
                # Предполагаем, что страница регистрации уже открыта
                driver.find_element(*TestLocators.NAME_LOCATOR).send_keys("Тест")

            # Заполняем форму входа или регистрации
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.EMAIL_LOCATOR))
            driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(email)
            driver.find_element(*TestLocators.PASSWORD_LOCATOR).send_keys(password)

            # Нажимаем кнопку «Войти» или «Зарегистрироваться» соответственно.
            driver.find_element(
                *TestLocators.LOGIN_BUTTON_LOCATOR if not is_registration else TestLocators.REGISTER_BUTTON_LOCATOR).click()

            if is_registration:
                # Проверка появления ошибки "Такой пользователь уже существует"
                try:
                    WebDriverWait(driver, 3).until(
                        EC.visibility_of_element_located(TestLocators.ERROR_MESSAGE_LOCATOR)
                    )
                    # Если ошибка появилась, генерируем новый email
                    email = Generator.generate_email()
                    driver.refresh()  # Обновляем страницу для повторной регистрации
                except TimeoutException:
                    break  # Если ошибка не появилась, выходим из цикла
            else:
                break

        # После логина проверяем, что мы на главной странице.
        expected_url_substring = "/login" if is_registration else "/"
        WebDriverWait(driver, 10).until(EC.url_contains(expected_url_substring))
