from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TestLinks
from locators import TestLocators


# Содаём класс для проверки переходов к разделам конструктора
class TestNavigationInConstructor:
    # Проверяем переход в разделы конструктора по клику на соответствующие вкладки

    # Вкладка Булки изначально выбрана и некликабельна
    def test_navigation_to_buns(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)

        # Прокрутка к разделу «Булки»
        buns_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUNS_SECTION_LOCATOR))
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_section)

        # Проверка, что раздел «Булки» виден в области просмотра
        assert buns_section.is_displayed(), "Ошибка отображения раздела «Булки»."

    def test_navigation_to_sauces(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)

        # Клик по вкладке «Соусы» и прокрутка к разделу «Соусы»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR)).click()
        sauces_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.SAUCES_SECTION_LOCATOR))
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_section)

        # Проверка, что раздел «Соусы» виден в области просмотра
        assert sauces_section.is_displayed(), "Ошибка отображения раздела «Соусы»."

    def test_navigation_to_fillings(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)

        # Клик по вкладке «Начинки» и прокрутка к разделу «Начинки»
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR)).click()
        fillings_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.FILLINGS_SECTION_LOCATOR))
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_section)

        # Проверка, что раздел «Начинки» виден в области просмотра
        assert fillings_section.is_displayed(), "Ошибка отображения раздела «Начинки»."

    # Альтернативный вариант проверки навигации по клику на вкладки, булки в конце, чтобы были кликабельны

    def test_navigation_to_sauces_section(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)

        # Клик по вкладке «Соусы»
        sauces_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_SAUCE_LOCATOR))
        driver.execute_script("arguments[0].click();", sauces_tab)

        # Проверка, что отображается подраздел «Соусы»
        sauces_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.SAUCES_SECTION_LOCATOR))
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_section)
        assert sauces_section.is_displayed(), "Ошибка отображения раздела «Соусы»."

    def test_navigation_to_fillings_section(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)

        # Клик по вкладке «Начинки»
        fillings_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_FILLING_LOCATOR))
        driver.execute_script("arguments[0].click();", fillings_tab)

        # Проверка, что отображается подраздел «Начинки»
        fillings_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.FILLINGS_SECTION_LOCATOR))
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_section)
        assert fillings_section.is_displayed(), "Ошибка отображения раздела «Начинки»."

    def test_navigation_to_buns_section(self, driver, test_email, test_password):
        # Переход на главную страницу
        driver.get(TestLinks.main_page_link)

        # Клик по вкладке «Булки»
        buns_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_TAB_BUN_LOCATOR))
        driver.execute_script("arguments[0].click();", buns_tab)

        # Проверка, что отображается подраздел «Булки»
        buns_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.BUNS_SECTION_LOCATOR))
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_section)
        assert buns_section.is_displayed(), "Ошибка отображения раздела «Булки»."
