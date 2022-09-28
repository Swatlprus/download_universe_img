import requests
import argparse
from pathlib import Path
from environs import Env
from download_tool import download_img

def fetch_apod(nasa_token, apod_amount):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': int(apod_amount), 'thumbs': True}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    url_images = []
    response_apod = response.json()
    url_images = [apod['url'] for apod in response_apod if apod['media_type'] == 'image']
    download_img(url_images, payload={}, name='apod')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apod_amount', default=30)
    args = parser.parse_args()
    env = Env()
    env.read_env()
    nasa_token = env("NASA_TOKEN")
    fetch_apod(nasa_token, args.apod_amount)


if __name__ == '__main__':
    main()