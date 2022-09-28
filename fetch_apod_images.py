import requests
import argparse
from environs import Env
from work_with_img import download_img

def fetch_apod(nasa_api_token, apod_amount):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_api_token, 'count': int(apod_amount), 'thumbs': True}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    url_images = []
    response_apod = response.json()
    url_images = [apod['url'] for apod in response_apod if apod['media_type'] == 'image']
    download_img(url_images, payload={}, name='apod')

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