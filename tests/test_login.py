from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestLinks, AuthHelper


# Содаём класс для проверки входа
class TestLogin:
    # Проверяем вход по кнопке «Войти в аккаунт» на главной
    # Нельзя просто так взять и войти с новым аккаунтом, сначала нужно зарегистрироваться
    def test_login_from_main_page(self, driver, test_email, test_password):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)
        # Регистрация
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)
        # Клик по кнопке «Войти в аккаунт»
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            TestLocators.LOGIN_BUTTON_LOCATOR)).click()
        # Логин
        AuthHelper.authenticate(driver, test_email, test_password)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, "Ошибка перехода на главную страницу после логина."

    # Проверяем вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver, test_email, test_password):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)
        # Регистрация
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)

        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)
        # Клик по кнопке "Личный Кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()
        # Логин
        AuthHelper.authenticate(driver, test_email, test_password)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, "Ошибка перехода на главную страницу после логина."

    # Проверяем вход через кнопку в форме регистрации
    def test_login_from_registration_link(self, driver, test_email, test_password):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)
        # Регистрация, попадаем на страничку логина
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)

        # На странице логина нажимаем на ссылку "Зарегистрироваться"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        # Логин через ссылку "Войти" с зарегистрированными данными
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        AuthHelper.authenticate(driver, test_email, test_password)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, "Ошибка перехода на главную страницу после логина."

    # Проверяем вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_link(self, driver, test_email, test_password):
        # Переход на страницу регистрации
        driver.get(TestLinks.registration_page_link)
        # Регистрация, попадаем на страничку логина
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)

        # На странице логина нажимаем на ссылку "Восстановить пароль"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()
        # Клик по ссылке "Войти" на странице восстановления пароля
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK_LOCATOR)).click()

        # Логин
        AuthHelper.authenticate(driver, test_email, test_password)
        # Дожидаемся загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        # Проверяем на соответствие текущий URL и ожидаемый результат
        assert driver.current_url == TestLinks.main_page_link, "Ошибка перехода на главную страницу после логина."
