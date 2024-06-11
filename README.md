# Проект автоматизации тестирования веб-приложения «Stellar Burgers»

## Описание проекта

Проект предназначен для автоматизации тестирования различных аспектов веб-приложения. Основными технологиями для написания автотестов являются фреймворк `pytest` и библиотека `Selenium WebDriver`. Тесты охватывают регистрацию, вход, навигацию, и выход из аккаунта, а также проверки корректности работы раздела «Конструктор».

## Описание тестов

### Регистрация
1. **Успешная регистрация**.
2. **Проверка ошибки для некорректного пароля**.

### Вход
1. **Вход по кнопке «Войти в аккаунт» на главной**.
2. **Вход через кнопку «Личный кабинет»**.
3. **Вход через кнопку в форме регистрации**.
4. **Вход через кнопку в форме восстановления пароля**.

### Переход в личный кабинет
1. **Проверка перехода по клику на «Личный кабинет»**.

### Переход из личного кабинета в конструктор
1. **Проверка перехода по клику на «Конструктор»**.
2. **Проверка перехода по клику на логотип Stellar Burgers**.

### Выход из аккаунта
1. **Проверка выхода по кнопке «Выйти» в личном кабинете**.

### Раздел «Конструктор»
1. **Проверка, что работают переходы к разделам: «Булки», «Соусы», «Начинки»**.

## Структура проекта
```
│
├── conftest.py
├── data.py
├── generator.py
├── locators.py
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   └── test_navigation_to_account.py
│   └── test_navigation_to_constructor.py
│   └── test_logout.py
│   └── test_constructor.py
└── pytest.ini
```

- `conftest.py`: содержит фикстуры для тестов.
- `data.py`: тестовые данные.
- `generator.py`: генераторы email и паролей.
- `locators.py`: описание локаторов элементов.

- `tests/`: директория с тестами. Тесты разделены по функциональности.

### Использование генератора учетных записей

В проекте используется класс `Generator` для генерации тестовых учетных записей. Этот класс предоставляет методы для генерации случайных email-адресов и паролей.
При генерации создаётся почта в формате: имя_фамилия_номер когорты_любые 3 цифры@домен. Например, test_testov_1_999@yandex.ru. 
Это нужно, чтобы при запуске тестов регистрироваться с уникальной почтой, так тесты остаются независимыми.

### Универсальная функция для регистрации и авторизации пользователей

В тестах используется вспомогательный класс `AuthHelper` для регистрации и логина пользователя. Этот класс предоставляет следующие методы:
- `AuthHelper.authenticate(driver, email, password, is_registration)` — Метод для регистрации и входа в систему. Если `is_registration` установлено в `True`, сначала выполняется регистрация, затем вход.
Также метод учитывает возможность ошибки при генерации повторяющихся логинов.

## Установка проекта

1. Склонируйте репозиторий на свой локальный компьютер:

```bash
   git clone <URL репозитория>
```
2. Перейдите в каталог проекта:
   
```bash
   cd <название репозитория>
   ```
   
3. Создайте виртуальное окружение для Python:
   
```bash
   python -m venv venv
   ```
   
4. Активируйте виртуальное окружение:
- На Windows:
     
```bash
     venv\Scripts\activate
```
     
- На MacOS/Linux:
     
```bash
     source venv/bin/activate
```
     
5. Установите зависимости:
   
```bash
   pip install pytest
   pip install selenium
   ```

## Запуск проекта

Для запуска тестов используйте команду `pytest`:

```bash
pytest -v
```
