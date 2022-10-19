import argparse
import os
import random
import time

from PIL import Image
import telegram


from dotenv import load_dotenv


def all_photos():
    directories = [
        'image_day_Nasa',
        'image_Earth_Nasa',
        'images_SpaceX'
    ]
    all_images = []
    for directory in directories:
        for name in os.listdir(directory):
            all_images.append(f'{directory}/{name}')
    random.shuffle(all_images)
    return all_images


def size_images_for_telegram(all_images):
    for image_name in all_images:
        image = Image.open(image_name)
        image.thumbnail((1280, 1280))
        image.save(f'{image_name}')


def create_parser():
    parser = argparse.ArgumentParser(
        description=
            'The program edits the images to the required size '
            'and sends the images to the telegram channel'
    )
    parser.add_argument(
        '-i',
        '--image',
        default=False,
        help=
            'Enter the command in console:'
            '$ python images_nasa_telegram_bot.py -i(--image) '
            '{image_day_Nasa(image_Earth_Nasa or images_SpaceX)/'
            'the name of the file to be sent in the telegram channel}. '
            'Where image_day_Nasa(image_Earth_Nasa or images_SpaceX) '
            'is the directories where the necessary images are located.'
            ' If you do not enter, then enter the frequency of photo '
            'publication in the telegram channel'
    )
    parser.add_argument(
        '-t',
        '--time',
        default=14400,
        type=int,
        help=
        'Enter the command in console:'
        '$ python images_nasa_telegram_bot.py -t(--time) '
        '{value in seconds(at least 15 seconds)}. '
        'Where {value in seconds} this is the value in seconds of the frequency '
        'of sending images to the channel by the bot'
        ' If you do not enter, then the default value is 14400 seconds(4 hours) '
    )
    return parser


def main():
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=telegram_bot_token)
    parser = create_parser()
    image_publish = parser.parse_args().image
    time_delay = parser.parse_args().time
    all_images = all_photos()
    size_images_for_telegram(all_images)
    if image_publish:
        bot.send_photo(
            chat_id=chat_id,
            photo=open(image_publish, 'rb')
        )
    else:
        while True:
            for image_name in all_images:
                time.sleep(time_delay)
                bot.send_photo(
                    chat_id=chat_id,
                    photo=open(f'{image_name}', 'rb')
                )


if __name__ == '__main__':

    main()