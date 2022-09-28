import requests
import argparse
from download_tool import download_img

def fetch_spacex_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    response_spacex_launch = response.json()
    url_images = response_spacex_launch['links']['flickr']['original']
    download_img(url_images, payload={}, name='spacex')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default='latest')
    args = parser.parse_args()
    fetch_spacex_launch(args.launch_id)


if __name__ == '__main__':
    main()