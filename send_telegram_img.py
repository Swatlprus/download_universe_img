import telegram
import os
from environs import Env
import random
import time
import argparse


def post_img_telegram(sleep_time, telegram_token, telegram_chat_id, path_to_images):
    path_imgs=collect_img(path_to_images)
    bot = telegram.Bot(token=telegram_token)
    while True:
        random.shuffle(path_imgs)
        for img_file in path_imgs:
            compress_image(img_file)
            with open(img_file, 'rb') as photo:
                try:
                    bot.send_photo(chat_id=telegram_chat_id, photo=photo)
                except telegram.error.NetworkError:
                    print('Error Telegram Connection')
                    time.sleep(15)
            time.sleep(int(sleep_time))

def collect_img(path_to_images):
    path_imgs = []
    for root, dirs, files in os.walk(f'{path_to_images}'):
        pass
    for img_file in files:
            path_file_img = os.path.join(path_to_images, img_file)
            path_imgs.append(path_file_img)
    return path_imgs

def compress_image(path_file_img):
    max_size_img = 20971520
    small_resolution = (1600, 900)
    if os.path.getsize(path_file_img) > max_size_img:
                with open(path_file_img, 'rb') as image:
                    path_file_img = image.thumbnail(small_resolution)
    return path_file_img

def main():
    env = Env()
    env.read_env()
    telegram_token = env("TELEGRAM_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_images', default='images')
    args = parser.parse_args()
    telegram_chat_id = env("TELEGRAM_CHAT_ID")
    try:
        sleep_time = env("SLEEP_TIME")
    except ValueError:
        sleep_time = 14400
    post_img_telegram(sleep_time, telegram_token, telegram_chat_id, args.path_to_images)


if __name__ == '__main__':
    main()