import requests
import argparse
from work_with_img import download_imgs, get_type_img


def fetch_spacex_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    response_spacex_launch = response.json()
    image_paths = []
    image_urls = []
    for img_number, url_img in enumerate(response_spacex_launch["links"]["flickr"]["original"]):
        image_urls.append(url_img)
        filename = f"spacex_{img_number}{get_type_img(url_img)}"
        image_paths.append(filename)
    download_imgs(image_urls, image_paths)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--launch_id", default="latest")
    args = parser.parse_args()
    fetch_spacex_launch(args.launch_id)


if __name__ == "__main__":
    main()
