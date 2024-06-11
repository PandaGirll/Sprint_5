from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from generator import Generator
from locators import TestLocators


class AuthHelper:
    # Метод для логина пользователя
    @staticmethod
    def login(driver, email, password):
        # Заполняем форму входа
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            TestLocators.EMAIL_LOCATOR))
        driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_LOCATOR).send_keys(password)
        # Нажимаем кнопку "Войти"
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOCATOR).click()

    # Метод для регистрации пользователя
    @staticmethod
    def registration(driver, email, password, name="Тест"):
        def fill_registration_form(driver, email, password, name):
            # Заполняем форму регистрации
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(TestLocators.NAME_LOCATOR))
            driver.find_element(*TestLocators.NAME_LOCATOR).send_keys(name)
            driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(email)
            driver.find_element(
                *TestLocators.PASSWORD_LOCATOR).send_keys(password)
            # Нажимаем кнопку "Зарегистрироваться"
            driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()

        fill_registration_form(driver, email, password, name)

        # Проверка, что пользователь уже существует
        while AuthHelper.is_user_already_exists(driver):
            email = Generator.generate_email()  # Генерируем новый email
            driver.refresh()  # Обновляем страницу
            fill_registration_form(driver, email, password, name)

    # Проверка успешности редиректа после логина
    @staticmethod
    def confirm_login_success(driver):
        # Проверяем, что мы на главной странице
        WebDriverWait(driver, 10).until(EC.url_to_be(
            TestLinks.main_page_link))

    # Проверка успешности редиректа после регистрации
    @staticmethod
    def confirm_registration_success(driver):
        # Проверяем, что мы на странице логина
        WebDriverWait(driver, 10).until(EC.url_to_be(
            TestLinks.login_page_link))

    # Проверка на появление ошибки после регистрации
    @staticmethod
    def is_user_already_exists(driver):
        # Проверка появления ошибки "Такой пользователь уже существует"
        try:
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located
                (TestLocators.ERROR_MESSAGE_LOCATOR))
            return True  # Ошибка появилась
        except TimeoutException:
            return False  # Ошибка не появилась
