import argparse
import os
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv


def nasa_epic_picture_number(nasa_api_key_epic, nasa_url):
    payload = {
        'api_key': nasa_api_key_epic
    }
    response = requests.get(
        nasa_url,
        params=payload
    )
    response.raise_for_status()
    image_numbers = []
    for image in response.json():
        image_numbers.append(image.get('image'))
    return image_numbers[:]


def nasa_epic_picture_urls(image_numbers, date, nasa_api_key_epic):
    year, month, day = date.split('-')
    urls_epic_image_list = []
    for image_number in image_numbers:
        picture_url = \
            f'https://api.nasa.gov/EPIC/archive/natural/' \
            f'{year}/{month}/{day}/png/{image_number}.png'
        urls_epic_image_list.append(picture_url)
    urls_epic_image_list_api = []
    for url in urls_epic_image_list:
        payload = {
            'api_key': nasa_api_key_epic
        }
        response = requests.get(
            url,
            params=payload
        )
        response.raise_for_status()
        urls_epic_image_list_api.append(response.url)
    return urls_epic_image_list_api


def nasa_epic_picture_downloads(urls_epic_image_list_api, path):
    for images_number, urls_epic_image_list_api in enumerate(urls_epic_image_list_api, 1):
        filename = f'nasa_epic_{images_number}.png'
        image = requests.get(urls_epic_image_list_api).content
        with open(f'{path}/{filename}', 'wb') as file:
            file.write(image)


def create_parser():
    parser = argparse.ArgumentParser(
        description=
        'The program downloads an epic image of the Earth of the day from a NASA server.'
    )
    parser.add_argument(
        '-d',
        '--date',
        default=datetime.today().strftime('%Y-%m-%d'),
        help=
        'Enter the command in console: '
        '$ python fetch_nasa_epic_picture.py -d(--date) {YYYY-mm-dd}. '
        'Where YYYY-mm-dd - is the start date for the download epic image day from NASA. '
        'if you do not enter -s(--start_date), then default = today'
    )
    return parser


def main():
    load_dotenv()
    nasa_api_key_epic = os.environ['NASA_API_KEY_EPIC']
    parser = create_parser()
    date = parser.parse_args().date
    Path('image_Earth_Nasa').mkdir(parents=True, exist_ok=True)
    path = 'image_Earth_Nasa'
    nasa_url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    image_numbers = nasa_epic_picture_number(nasa_api_key_epic, nasa_url)
    urls_epic_image_list_api = nasa_epic_picture_urls(image_numbers, date, nasa_api_key_epic)
    nasa_epic_picture_downloads(urls_epic_image_list_api, path)
    if not nasa_epic_picture_urls(image_numbers, date, nasa_api_key_epic):
        print(f'There is no epic Earth image on the server for the date: {date}')

if __name__ == '__main__':

    main()