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
        # Проверяем, что логин был успешен
        AuthHelper.confirm_login_success(driver)

    @staticmethod
    def registration(driver, email, password, name="Тест"):
        # Заполняем форму регистрации
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            TestLocators.NAME_LOCATOR))
        driver.find_element(*TestLocators.NAME_LOCATOR).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_LOCATOR).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_LOCATOR).send_keys(password)
        # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.REGISTER_BUTTON_LOCATOR).click()
        # Проверка, что пользователь уже существует
        if AuthHelper.is_user_already_exists(driver):
            # Генерируем новый email, и# обновляем страницу
            email = Generator.generate_email()
            driver.refresh()  # Обновляем страницу для повторной регистрации
            # Регистрируемся заново с новым email
            AuthHelper.registration(driver, email, password, name)
        else:
            # Проверяем, что регистрация была успешна
            AuthHelper.confirm_registration_success(driver)

    @staticmethod
    def confirm_login_success(driver):
        # Проверяем, что мы на главной странице
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

    @staticmethod
    def confirm_registration_success(driver):
        # Проверяем, что мы на странице логина
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.login_page_link))

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
