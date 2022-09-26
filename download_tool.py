import time
import requests
from get_type_img import get_type_img
from pathlib import Path

def download_img(url_images, headers, payload, name):
    Path("images").mkdir(parents=True, exist_ok=True)
    for url_img_number, url_img in enumerate(url_images):
        if name=='epic':
            filename = f'epic_{url_img_number}.png'
        elif name=='spacex':
            filename = f'spacex_{url_img_number}{get_type_img(url_img)}'
        elif name=='apod':
            filename = f'apod_{url_img_number}{get_type_img(url_img)}'
        path = Path('images', filename)
        time.sleep(1)
        response = requests.get(url_img, headers=headers, params=payload)
        response.raise_for_status()

        with open(path, 'wb') as file:
            file.write(response.content)
