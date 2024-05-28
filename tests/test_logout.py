from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestLinks, AuthHelper


# Содаём класс для проверки выхода
class TestLogout:
    # Проверяем выход по кнопке «Выйти» в личном кабинете
    def test_logout_from_personal_account(self, driver, test_email, test_password):
        # Переходим на страницу регистрации
        driver.get(TestLinks.registration_page_link)

        # Регистрация, попадаем на страничку логина
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)

        # Логин с зарегистрированными данными, попадаем на главную страницу
        AuthHelper.authenticate(driver, test_email, test_password)

        # Клик по кнопке «Личный кабинет»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()

        # Клик по кнопке «Выход»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON_LOCATOR)).click()

        # Проверка перехода на страницу логина
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.login_page_link))
        assert driver.current_url == TestLinks.login_page_link, \
            "Ошибка выхода из личного кабинета и перехода на страницу логина."
