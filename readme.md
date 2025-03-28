
Bot Parser
A Python-based bot parser that collects prices from websites by parsing HTML content using Selenium. This bot can be integrated into a larger Telegram bot, which retrieves and processes data asynchronously.

Features
Price Parsing: Collects prices from specified websites by loading them using Selenium WebDriver.

Headless Browsing: Runs the Selenium WebDriver in headless mode to avoid opening a browser window.

Requirements:
Python 3.7 or higher  
aiogram  
Selenium  
pandas  
openpyxl  
SQLite  
python-dotenv  
Chrome WebDriver  

Install Dependencies
To set up the project, make sure you have all the required dependencies installed. You can do this by creating a virtual environment and installing the dependencies via pip.

Set up a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```
Install required Python packages:

```pip install -r requirements.txt```
If you don't have requirements.txt, you can manually install the dependencies:

```pip install aiogram selenium pandas openpyxl python-dotenv```
You will also need to install the Chrome WebDriver. You can download it from https://googlechromelabs.github.io/chrome-for-testing/.

Download and install the appropriate WebDriver for your platform.

Make sure to replace constants.CHROMEDRIVER_PATH with the path to the ChromeDriver executable on your system.

Configuration
Before running the script, ensure that your SQLite database is correctly set up and the sites table contains the data to be parsed. The DatabaseManager class will automatically create the necessary tables if they do not exist.

Modify the following variables:

constants.DB_PATH: Path to your SQLite database.

constants.CHROMEDRIVER_PATH: Path to the ChromeDriver executable.

add .env file with your telegram bot token
```
TOKEN = "0181683736:GGGaMghtthbyhn5697969tReF1VN1xLy9wW_MNhftvy"

```
Usage
Example Usage
Create the Parser object and run it to get prices:
```
from parser import Parser

parser = Parser()
average_price = await parser.get_prices()

if average_price:
    print(f"Average Price: {average_price}")
else:
    print("No prices found.")
```
To run the bot (if integrated with Telegram bot), call the ```dp.start_polling()``` as shown in your main.py file.

Logging
This project uses Python's built-in logging library for logging errors and information. You can configure the logging level based on your needs:

```
import logging

logging.basicConfig(level=logging.INFO)
```
By setting the logging level to INFO, you will see general logs, including info and error logs. For debugging, you can change the level to DEBUG.

Contributing
If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request with your changes.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Bot Parser (Русский)
Парсер для бота на Python, который собирает цены с сайтов, парсит HTML-контент с использованием Selenium. Этот бот может быть интегрирован в более крупный Telegram-бот, который асинхронно извлекает и обрабатывает данные.

Возможности
Парсинг цен: Собирает цены с указанных сайтов, загружая их с использованием Selenium WebDriver.

Работа в headless-режиме: Запускает Selenium WebDriver в headless-режиме, избегая открытия окна браузера.

Требования:  
Python 3.7 или выше  
aiogram  
Selenium  
pandas  
openpyxl  
SQLite  
python-dotenv  
Chrome WebDriver  

Установка зависимостей
Для настройки проекта убедитесь, что все необходимые зависимости установлены. Вы можете сделать это, создав виртуальное окружение и установив зависимости через pip.

Создайте виртуальное окружение (рекомендуется, но не обязательно):
```
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows
```
Установите необходимые пакеты Python:

```pip install -r requirements.txt```
Если у вас нет файла requirements.txt, установите зависимости вручную:

```pip install aiogram selenium pandas openpyxl python-dotenv```

Также вам нужно будет установить Chrome WebDriver. Скачайте его с https://googlechromelabs.github.io/chrome-for-testing/.

Скачайте и установите подходящий WebDriver для вашей платформы.

Убедитесь, что вы указали правильный путь к исполняемому файлу ChromeDriver в constants.CHROMEDRIVER_PATH.

Конфигурация
Перед запуском скрипта убедитесь, что ваша SQLite база данных правильно настроена, а таблица sites содержит данные для парсинга. Класс DatabaseManager автоматически создаст необходимые таблицы, если они не существуют.

Измените следующие переменные:

constants.DB_PATH: Путь к вашей базе данных SQLite.

constants.CHROMEDRIVER_PATH: Путь к исполняемому файлу ChromeDriver.

Добавьте файл .env с токеном вашего бота:
```
TOKEN = "0181683736:GGGaMghtthbyhn5697969tReF1VN1xLy9wW_MNhftvy"

```

Использование
Пример использования
Создайте объект Parser и выполните парсинг для получения цен:

```
from parser import Parser

parser = Parser()
average_price = await parser.get_prices()

if average_price:
    print(f"Average Price: {average_price}")
else:
    print("No prices found.")
```
Чтобы запустить бота (если интегрирован с Telegram-ботом), вызовите dp.start_polling(), как показано в вашем файле main.py.

Логирование
В проекте используется встроенная библиотека Python logging для логирования ошибок и информации. Вы можете настроить уровень логирования в зависимости от ваших нужд:

```
import logging

logging.basicConfig(level=logging.INFO)
```
Установив уровень логирования на INFO, вы будете видеть общие логи, включая информацию и ошибки. Для отладки можно изменить уровень на DEBUG.

Вклад
Если вы хотите внести свой вклад в этот проект, пожалуйста, форкните репозиторий, создайте новую ветку и отправьте pull request с вашими изменениями.

Лицензия
Этот проект лицензирован под MIT License — см. файл LICENSE для подробностей.

Future Improvements
Performance Optimization: Refactor certain parts of the code to improve performance, especially when parsing large datasets.

Cross-Browser Support: Add support for browsers other than Chrome (e.g., Firefox, Safari) to enhance compatibility.

Error Handling: Improve error handling and logging to make the system more robust and easier to debug.

User Interface: Develop a GUI to simplify user interaction for those who prefer not to work with the command line.

Internationalization (i18n): Add support for multiple languages to make the application accessible to a global audience.

TODO
Automated Tests: Write unit and integration tests to ensure code stability and reliability.

Database Scaling: Improve the database schema and queries for handling a larger number of sites or entries efficiently.
