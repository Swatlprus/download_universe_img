import requests
import argparse
from work_with_img import download_img
from work_with_img import create_path

def fetch_spacex_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    response_spacex_launch = response.json()
    images_url = response_spacex_launch['links']['flickr']['original']
    create_path(images_url, payload={}, name='spacex')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default='latest')
    args = parser.parse_args()
    fetch_spacex_launch(args.launch_id)


if __name__ == '__main__':
    main()