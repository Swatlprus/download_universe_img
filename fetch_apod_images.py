from venv import create
import requests
import argparse
from environs import Env
from work_with_img import download_img, get_type_img


def fetch_apod(nasa_api_token, apod_amount):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_api_token, 'count': int(apod_amount), 'thumbs': True}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images_url = []
    image_paths = []
    response_apod = response.json()
    for img_number, apod in enumerate(response_apod):
        if apod['media_type']=='image':
            images_url.append(apod['url'])
            filename = f'apod_{img_number}{get_type_img(apod["url"])}'
            image_paths.append(filename)
    download_img(images_url, image_paths, payload={})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', default=15)
    args = parser.parse_args()
    env = Env()
    env.read_env()
    nasa_api_token = env("NASA_API_TOKEN")
    fetch_apod(nasa_api_token, args.number)


if __name__ == '__main__':
    main()