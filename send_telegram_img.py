import re
import telegram
import os
from environs import Env
from PIL import Image
import random
import time
import argparse


def post_img_telegram(time_sleep, telegram_token, path_to_images):
    for root, dirs, files in os.walk(f'{path_to_images}'):
        pass
    bot = telegram.Bot(token=telegram_token)
    while True:
        random.shuffle(files)
        for file_img in files:
            path_file_img = f'{path_to_images}/{file_img}'
            if os.path.getsize(path_file_img) > 20971520:
                image = Image.open(path_file_img)
                path_file_img = image.thumbnail((1600, 900))
            bot.send_photo(chat_id='@img_universe', photo=open(path_file_img, 'rb'))
            time.sleep(int(time_sleep))

def main():
    env = Env()
    env.read_env()
    telegram_token = env("TELEGRAM_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_images')
    args = parser.parse_args()
    if env("TIME_SLEEP"):
        time_sleep = env("TIME_SLEEP")
    else:
        time_sleep = 14400
    post_img_telegram(time_sleep, telegram_token, args.path_to_images)


if __name__ == '__main__':
    main()