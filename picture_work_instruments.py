from os.path import split, splitext
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests


def download_picture(picture_name, picture_url, images_file_path):
    response = requests.get(picture_url)
    response.raise_for_status()

    with open(Path(images_file_path, picture_name), 'wb') as picture:
        picture.write(response.content)


def get_file_extension(url):
    url_parts = urlparse(url)
    url_path = url_parts.path
    url_name = unquote(split(url_path)[1])
    file_extension = splitext(url_name)[1]

    return file_extension