# Sprint_5

Проект для автотестов сервиса Stellar Burgers.

## Структура проекта

- `conftest.py`: содержит фикстуры для тестов.
- `locators.py`: описание локаторов элементов.
- `data.py`: тестовые данные.
- `generator.py`: генераторы email и паролей.
- `tests/`: директория с тестами. Тесты разделены по функциональности.

## Установка и запуск

1. Установка зависимостей:

```bash
pip install -r requirements.txt
```
2. Запуск тестов:

Для запуска тестов, убедитесь в наличии pytest в вашей среде разработки. Запустите следующую команду в терминале:

```bash
pytest test_books_collector.py
```
