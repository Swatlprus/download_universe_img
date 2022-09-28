import os
import time
import requests
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import unquote


def get_type_img(url):
    unquote_url = unquote(url)
    urlparse_url = urlparse(unquote_url)
    file_extension = os.path.splitext(
        f'{urlparse_url.netloc}{urlparse_url.path}')[-1]
    return file_extension


def download_img(images_url, payload, name):
    Path("images").mkdir(parents=True, exist_ok=True)
    for img_number, url_img in enumerate(images_url):
        if name=='epic':
            filename = f'epic_{img_number}.png'
        elif name=='spacex':
            filename = f'spacex_{img_number}{get_type_img(url_img)}'
        elif name=='apod':
            filename = f'apod_{img_number}{get_type_img(url_img)}'
        path = Path('images', filename)
        time.sleep(1)
        response = requests.get(url_img, params=payload)
        response.raise_for_status()

        with open(path, 'wb') as file:
            file.write(response.content)
