import requests
from pathlib import Path
import time
import datetime
from environs import Env
from get_type_img import get_type_img
from download_tool import download_img


def fetch_epic(nasa_token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    }
    payload = {'api_key': nasa_token}

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    url_images = []
    response_earth = response.json()
    for earth in response_earth:
        name_image = earth['image']
        date_image = datetime.datetime.fromisoformat(earth['date'])
        date_image_for_link = date_image.strftime('%Y/%m/%d')
        link_on_EPIC = f'https://api.nasa.gov/EPIC/archive/natural/{date_image_for_link}/png/{name_image}.png'
        url_images.append(link_on_EPIC)

    Path("images").mkdir(parents=True, exist_ok=True)
    for url_img_number, url_img in enumerate(url_images):
        download_img(url_img_number, url_img, payload, headers, name='epic')


def main():
    env = Env()
    env.read_env()
    nasa_token = env("NASA_TOKEN")
    fetch_epic(nasa_token)


if __name__ == '__main__':
    main()