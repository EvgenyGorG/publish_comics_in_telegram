from pathlib import Path

import requests

from picture_work_instruments import download_picture, get_file_expansion


def main():
    comic_book_url = 'https://xkcd.com/353/info.0.json'

    response_from_comic_book = requests.get(comic_book_url)
    response_from_comic_book.raise_for_status()
    comic_book_info = response_from_comic_book.json()

    comic_book_image_url = comic_book_info['img']
    comic_book_name = 'python_comic_book'
    comic_book_name_expansion = get_file_expansion(comic_book_image_url)
    comic_book_full_name = f'{comic_book_name}{comic_book_name_expansion}'
    directory_for_images = Path(Path.cwd(), 'Files')

    download_picture(
        comic_book_full_name, comic_book_image_url, directory_for_images
    )


if __name__ == '__main__':
    main()