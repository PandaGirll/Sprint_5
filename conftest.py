import pytest
from selenium import webdriver
from generator import Generator


# фикстура драйвера
@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1920,1080')  # задали размер окна
    driver = webdriver.Chrome(options=chrome_options)  # инициализируем драйвер
    yield driver  # передаём драйвер в тесты
    driver.quit()  # закрываем драйвер


# фикстура для генерации логина
@pytest.fixture
def test_email():
    return Generator.generate_email()


# фикстура для генерации пароля
@pytest.fixture
def test_password():
    return Generator.generate_password()
