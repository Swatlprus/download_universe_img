import time
import requests
from get_type_img import get_type_img
from pathlib import Path

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
