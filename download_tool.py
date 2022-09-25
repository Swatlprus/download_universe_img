import time
import requests
from get_type_img import get_type_img
from pathlib import Path

def download_img(url_img_number, url_img, headers, payload, name):
    if name=='epic':
        filename = f'epic_{url_img_number}.png'
        payload = payload
    elif name=='spacex':
        filename = f'spacex_{url_img_number}{get_type_img(url_img)}'
        payload= {}
    elif name=='apod':
        filename = f'apod_{url_img_number}{get_type_img(url_img)}'
        payload= {}
    path = Path('images', filename)
    time.sleep(1)
    response = requests.get(url_img, headers=headers, params=payload)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)
