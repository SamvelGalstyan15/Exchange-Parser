# Exchange

Скрипт для автоматического отслеживания курсов валют в банках Армении и конвертации валют.

## Функционал
- Парсинг актуальных курсов AMD и RUB с сайта `rate.am`.
- Использование `undetected-chromedriver` для обхода защиты от ботов.
- Класс `Change` для удобного расчета конвертации из USD в AMD, RUB и EUR.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com
   cd Exchange
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   # Создание окружения
   python -m venv venv

   # Активация (Windows)
   .\venv\Scripts\activate

   # Активация (macOS/Linux)
   source venv/bin/activate
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск

Запустите основной скрипт:
```bash
python Change.py
```

Введите сумму в USD, когда программа запросит ввод, чтобы получить результат конвертации.

## Стек технологий
- Python 3.x
- Selenium
- undetected-chromedriver
