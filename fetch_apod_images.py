import requests
from pathlib import Path
import time
from environs import Env
from get_type_img import get_type_img
from download_tool import download_img

def fetch_apod(nasa_token, count_apod):
    url = 'https://api.nasa.gov/planetary/apod'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    }
    payload = {'api_key': nasa_token, 'count': count_apod, 'thumbs': True}
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    url_images = []
    response_apod = response.json()
    for apod in response_apod:
        if apod['media_type'] == 'image':
            url_images.append(apod['url'])

    Path("images").mkdir(parents=True, exist_ok=True)
    for url_img_number, url_img in enumerate(url_images):
        download_img(url_img_number, url_img, headers, name='apod')


def main():
    env = Env()
    env.read_env()
    nasa_token = env("NASA_TOKEN")
    count_apod = env("COUNT_APOD")
    fetch_apod(nasa_token, count_apod)


if __name__ == '__main__':
    main()
