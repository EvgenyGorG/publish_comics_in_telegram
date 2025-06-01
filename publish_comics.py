from time import sleep
import os
import random
import sys
from pathlib import Path

import requests
import telegram
from dotenv import load_dotenv

from picture_work_instruments import download_picture, get_file_extension


def get_number_of_comics():
    comic_book_url = 'https://xkcd.com/info.0.json'

    response_from_comic_book = requests.get(comic_book_url)
    response_from_comic_book.raise_for_status()
    comic_book_info = response_from_comic_book.json()

    return comic_book_info['num']


def get_env_variable(name, default=None, required=False):
    value = os.getenv(name, default)

    if required and (value is None or value == ''):
        print(f'Ошибка: обязательная переменная окружения "{name}" не задана.', file=sys.stderr)
        sys.exit(1)

    return value


def main():
    load_dotenv()
    tg_bot_token = get_env_variable('TG_BOT_TOKEN', required=True)
    tg_chat_id = get_env_variable('TG_GROUP_CHAT_ID', required=True)
    send_time = int(get_env_variable('COMIC_BOOK_SEND_TIME', default=14400))
    tg_bot = telegram.Bot(token=tg_bot_token)

    directory_for_images = Path(Path.cwd(), 'Files')
    first_check = True

    while True:
        try:
            number_of_comics = get_number_of_comics()
            random_comic_book = random.randint(1, number_of_comics)
            comic_book_url = f'https://xkcd.com/{random_comic_book}/info.0.json'

            response_from_comic_book = requests.get(comic_book_url)
            response_from_comic_book.raise_for_status()
            comic_book_info = response_from_comic_book.json()

            comic_book_image_url = comic_book_info['img']
            comic_book_comment = comic_book_info['alt']
            comic_book_name = comic_book_info['title']
            comic_book_name_extension = get_file_extension(comic_book_image_url)
            comic_book_full_name = f'{comic_book_name}{comic_book_name_extension}'

            download_picture(
                comic_book_full_name, comic_book_image_url, directory_for_images
            )

            with open(Path(directory_for_images, comic_book_full_name), 'rb') as image:
                tg_bot.send_document(
                    chat_id=tg_chat_id,
                    document=image
                )
            tg_bot.send_message(chat_id=tg_chat_id, text=comic_book_comment)

            Path.unlink(Path(directory_for_images, comic_book_full_name))

            sleep(send_time)

        except telegram.error.NetworkError:
            if first_check:
                first_check = False
                sleep(5)
            else:
                sleep(30)


if __name__ == '__main__':
    main()