from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import TestLinks, AuthHelper


# Содаём класс для проверки перехода в личный кабинет
class TestNavigationToPersonalAccount:
    # Проверяем переход по клику на кнопку «Личный кабинет»
    def test_navigation_to_personal_account(self, driver, test_email, test_password):
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
