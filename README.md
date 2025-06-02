# Публикация комиксов

Программа позволяет публиковать комиксы в группу или канал Telegram. Комиксы выбираются случайным образом из источника
[xkcd](https://xkcd.com/). Комиксы публикуются по одному, с комментарием автора. Временной промежуток между
публикациями можно настроить.

### Как установить

Python3 должен быть уже установлен. Рекомендуемая версия [Python 3.10](https://www.python.org/downloads/release/python-3100/).

Для изоляции проекта рекомендуется использовать `.venv` виртуальное окружение:

```shell
> python -m venv .venv
```

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```shell
> pip install -r requirements.txt
```

В файле `.env.example` можно ознакомиться с переменными окружения, они необходимы для корректной работы программы.
`TG_BOT_TOKEN`, `TG_GROUP_CHAT_ID` токен телеграм бота и чат id группы(канала) соответственно. Ознакомиться с 
туториалом о том, как зарегистрировать и получить токен бота, а так же о том, как создать группу или канал в телеграм 
можно по ссылке [Отложенный постинг](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/). Обратите внимание,
`TG_GROUP_CHAT_ID` должна иметь вид `@name_group`.
Переменная окружения `COMIC_BOOK_SEND_TIME` используется для настройки промежутка времени отправки,
по умолчанию используется отправка раз в день. Если вы хотите указать свое значение, 
добавьте переменную в `.env.example` 
файл в следующем виде: `COMIC_BOOK_SEND_TIME={number_of_seconds}`, где `{number_of_seconds}` 
количество секунд между отправкой.
Заполните все переменные окружения в файле `.env.example`, а затем переименуйте файл в `.env`.

### Запуск скрипта

```shell
> python publish_comics.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).


# Comic Publishing

This program allows you to publish comics to a Telegram group or channel.
Comics are selected randomly from the source [xkcd](https://xkcd.com/).
Comics are published one at a time, with the author’s commentary. The time interval between publications can be configured.

### How to Install

Python 3 must already be installed.
The recommended version is [Python 3.10](https://www.python.org/downloads/release/python-3100/).

To isolate the project, it is recommended to use a `.venv` virtual environment: 

```shell
> python -m venv .venv
```

Then use `pip` (or `pip3`, to avoid conflicts with Python 2) to install dependencies:

```shell
> pip install -r requirements.txt
```

You can review the environment variables in the `.env.example` file;
they are necessary for the program to work correctly.  
`TG_BOT_TOKEN` and `TG_GROUP_CHAT_ID` are the Telegram bot token and the chat ID of the group(or channel), respectively.  
You can find a tutorial on how to register and obtain a bot token, as well as how to create a Telegram group or channel, 
at [Scheduled Posting](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/). 
Note that `TG_GROUP_CHAT_ID` should be in the format `@group_name`.  
The environment variable `COMIC_BOOK_SEND_TIME` is used to set the time interval for sending.
By default, sending is once a day. If you want to specify your value, add the variable to the `.env.example`
file as follows: `COMIC_BOOK_SEND_TIME={number_of_seconds}`, where `{number_of_seconds}` 
the number of seconds between sending.  
Fill in all environment variables in the `.env.example` file, then rename the file to `.env`.

### Running the Script

```shell
> python publish_comics.py
```

### Project Purpose

The code was written for educational purposes as part of an online web development course at [dvmn.org](https://dvmn.org/).