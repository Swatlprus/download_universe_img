import telegram
import os
from environs import Env
from PIL import Image
import random
import time
import argparse


def post_img_telegram(sleep_time, telegram_token, telegram_chat_id, path_to_images):
    max_size_img = int(20971520)
    small_resolution = (1600, 900)
    for root, dirs, files in os.walk(f'{path_to_images}'):
        pass
    bot = telegram.Bot(token=telegram_token)
    try:
        while True:
            random.shuffle(files)
            for file_img in files:
                path_file_img = os.path.join(path_to_images, file_img)
                if os.path.getsize(path_file_img) > max_size_img:
                    image = Image.open(path_file_img)
                    path_file_img = image.thumbnail(small_resolution)
                with open(path_file_img, 'rb') as photo:
                    bot.send_photo(chat_id=telegram_chat_id, photo=photo)
                time.sleep(int(sleep_time))
    except telegram.error.NetworkError:
        time.sleep(3)
        with open(path_file_img, 'rb') as photo:
            bot.send_photo(chat_id=telegram_chat_id, photo=photo)


def main():
    env = Env()
    env.read_env()
    telegram_token = env("TELEGRAM_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_images', default='images')
    args = parser.parse_args()
    telegram_chat_id = env("TELEGRAM_CHAT_ID")
    if env("SLEEP_TIME"):
        sleep_time = env("SLEEP_TIME")
    else:
        sleep_time = 14400
    post_img_telegram(sleep_time, telegram_token, telegram_chat_id, args.path_to_images)


if __name__ == '__main__':
    main()