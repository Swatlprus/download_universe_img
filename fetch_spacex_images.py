import requests
from pathlib import Path
import time
import argparse
from get_type_img import get_type_img
from download_tool import download_img

def fetch_spacex_launch(id_launch):
    url = f'https://api.spacexdata.com/v5/launches/{id_launch}'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response_spacex_launch = response.json()
    url_images = response_spacex_launch['links']['flickr']['original']

    Path("images").mkdir(parents=True, exist_ok=True)
    for url_img_number, url_img in enumerate(url_images):
        download_img(url_img_number, url_img, headers, name='spacex')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id_launch', default='latest')
    args = parser.parse_args()
    fetch_spacex_launch(args.id_launch)


if __name__ == '__main__':
    main()