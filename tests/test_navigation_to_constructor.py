from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestLinks, AuthHelper


# Содаём класс для проверки навигации из Личного кабинета в Конструктор
class TestNavigationToConstructor:
    # Проверяем переход из личного кабинета в конструктор по клику на кнопку "Конструктор"
    def test_navigation_from_personal_account_to_constructor(self, driver, test_email, test_password):
        # Переходим на страницу регистрации
        driver.get(TestLinks.registration_page_link)

        # Регистрация, попадаем на страничку логина
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)

        # Логин с зарегистрированными данными, попадаем на главную страницу
        AuthHelper.authenticate(driver, test_email, test_password)

        # Клик по кнопке «Личный кабинет»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()

        # Проверка перехода в личный кабинет
        WebDriverWait(driver, 10).until(EC.url_contains(TestLinks.personal_account_page_link))
        assert driver.current_url == TestLinks.personal_account_page_link, "Ошибка перехода в личный кабинет."

        # Клик по кнопке «Конструктор»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON_LOCATOR)).click()

        # Проверка перехода на главную страницу  (в Конструктор)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, "Ошибка перехода на страницу конструктора."

    # Проверяем переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_navigation_from_personal_account_to_constructor_via_logo(self, driver, test_email, test_password):
        # Переходим на страницу регистрации
        driver.get(TestLinks.registration_page_link)

        # Регистрация, попадаем на страничку логина
        AuthHelper.authenticate(driver, test_email, test_password, is_registration=True)

        # Логин с зарегистрированными данными, попадаем на главную страницу
        AuthHelper.authenticate(driver, test_email, test_password)

        # Клик по кнопке «Личный кабинет»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)).click()

        # Проверка перехода в личный кабинет
        WebDriverWait(driver, 10).until(EC.url_contains(TestLinks.personal_account_page_link))
        assert driver.current_url == TestLinks.personal_account_page_link, "Ошибка перехода в личный кабинет."

        # Клик на логотип Stellar Burgers
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGO_LOCATOR)).click()

        # Проверка перехода на главную страницу (в Конструктор)
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))
        assert driver.current_url == TestLinks.main_page_link, \
            "Ошибка перехода на главную страницу по клику на логотип."
