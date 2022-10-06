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


def download_imgs(image_urls, image_paths, payload={}):
    Path("images").mkdir(parents=True, exist_ok=True)
    for url_img, filename in zip(image_urls, image_paths):
        path = Path('images', filename)
        response = requests.get(url_img, params=payload)
        response.raise_for_status()
        with open(path, 'wb') as file:
            file.write(response.content)