from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from auth_helper import AuthHelper
from data import TestLinks
from locators import TestLocators


# Содаём класс для проверки входа
class TestLogin:
    # Проверяем вход по кнопке «Войти в аккаунт» на главной
    # Нельзя просто так взять и войти с новым аккаунтом, сначала нужно
    # зарегистрироваться
    def test_login_from_main_page(self, driver, registered_user):
        test_mail, test_pass = registered_user
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)
        # Клик по кнопке «Войти в аккаунт»
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            TestLocators.LOGIN_BUTTON_LOCATOR)).click()
        # Логин
        AuthHelper.login(driver, test_mail, test_pass)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, (
            "Ошибка перехода на главную страницу после логина."
        )

    # Проверяем вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver, registered_user):
        test_mail, test_pass = registered_user
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)
        # Клик по кнопке "Личный Кабинет"
        WebDriverWait(
            driver, 5).until(
            EC.element_to_be_clickable(
                TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        # Логин
        AuthHelper.login(driver, test_mail, test_pass)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, (
            "Ошибка перехода на главную страницу после логина."
        )

    # Проверяем вход через кнопку в форме регистрации
    def test_login_from_registration_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        # Переходим на страницу регистрации
        driver.get(TestLinks.registration_page_link)
        # Логин через ссылку "Войти" с зарегистрированными данными
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            TestLocators.LOGIN_LINK_LOCATOR)).click()
        AuthHelper.login(driver, test_mail, test_pass)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, (
            "Ошибка перехода на главную страницу после логина."
        )

    # Проверяем вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        # Переходим на страницу логина
        driver.get(TestLinks.login_page_link)
        # На странице логина нажимаем на ссылку "Восстановить пароль"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                TestLocators.LOGIN_LINK_LOCATOR)).click()
        # Клик по ссылке "Войти" на странице восстановления пароля
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                TestLocators.LOGIN_LINK_LOCATOR)).click()

        # Логин
        AuthHelper.login(driver, test_mail, test_pass)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, (
            "Ошибка перехода на главную страницу после логина."
        )
