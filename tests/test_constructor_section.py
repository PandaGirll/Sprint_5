from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from locators import TestLocators


# Содаём класс для проверки переходов к разделам конструктора
class TestNavigationInConstructor:
    # Проверяем переход в разделы конструктора по клику на вкладки
    # Вкладка Булки изначально выбрана и некликабельна
    def test_navigation_to_buns(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)
        # Клик по вкладке «Соусы» чтобы уйти с вкладки "Булки"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR)).click()
        # Клик по вкладке «Булки»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            TestLocators.CONSTRUCTOR_TAB_BUN_LOCATOR)).click()
        # Проверка, что вкладка "Булки" стала активной
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            TestLocators.ACTIVE_TAB_BUN_LOCATOR))
        # Определение ожидаемого и фактического результата
        buns_tab = driver.find_element(*TestLocators.ACTIVE_TAB_BUN_LOCATOR)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = buns_tab.get_attribute('class')
        assert expected_class in actual_class, "Вкладка 'Булки' не активна."

    def test_navigation_to_sauces(self, driver):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)
        # Клик по вкладке «Соусы»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR)).click()
        # Проверка, что вкладка "Соусы" стала активной
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                TestLocators.ACTIVE_TAB_SAUCE_LOCATOR))
        # Определение ожидаемого и фактического результата
        sauces_tab = driver.find_element(
            *TestLocators.ACTIVE_TAB_SAUCE_LOCATOR)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = sauces_tab.get_attribute('class')
        assert expected_class in actual_class, "Вкладка 'Соусы' не активна."

    def test_navigation_to_fillings(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)

        # Клик по вкладке «Начинки»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR)).click()
        # Проверка, что вкладка "Начинки" стала активной
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                TestLocators.ACTIVE_TAB_FILLING_LOCATOR))
        # Определение ожидаемого и фактического результата
        fillings_tab = driver.find_element(
            *TestLocators.ACTIVE_TAB_FILLING_LOCATOR)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = fillings_tab.get_attribute('class')
        assert expected_class in actual_class, "Вкладка 'Начинки' не активна."
