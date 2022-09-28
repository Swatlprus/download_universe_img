import requests
import datetime
from environs import Env
from download_tool import download_img


def fetch_epic(nasa_api_token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': nasa_api_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    url_images = []
    response_earth = response.json()
    for earth in response_earth:
        name_image = earth['image']
        date_image = datetime.datetime.fromisoformat(earth['date'])
        date_image_for_link = date_image.strftime('%Y/%m/%d')
        link_on_EPIC = f'https://api.nasa.gov/EPIC/archive/natural/{date_image_for_link}/png/{name_image}.png'
        url_images.append(link_on_EPIC)
    download_img(url_images, payload, name='epic')
    

def main():
    env = Env()
    env.read_env()
    nasa_api_token = env("NASA_API_TOKEN")
    fetch_epic(nasa_api_token)


if __name__ == '__main__':
    main()