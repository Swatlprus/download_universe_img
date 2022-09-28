import requests
import datetime
from environs import Env
from work_with_img import create_path


def fetch_epic(nasa_api_token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': nasa_api_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images_url = []
    response_earth = response.json()
    for earth in response_earth:
        image_name = earth['image']
        image_date = datetime.datetime.fromisoformat(earth['date'])
        date_image_for_link = image_date.strftime('%Y/%m/%d')
        link_on_EPIC = f'https://api.nasa.gov/EPIC/archive/natural/{date_image_for_link}/png/{image_name}.png'
        images_url.append(link_on_EPIC)
    create_path(images_url, payload, name='epic')
    

def main():
    env = Env()
    env.read_env()
    nasa_api_token = env("NASA_API_TOKEN")
    fetch_epic(nasa_api_token)


if __name__ == '__main__':
    main()