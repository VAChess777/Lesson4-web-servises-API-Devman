from pathlib import Path

import requests


def get_pictures_latest_launch(path, url):
    url_latest_launch = f"{url}/{'latest'}"
    response = requests.get(url_latest_launch)
    response.raise_for_status()
    image_latest_launch = response.json()["links"]["flickr"]["original"]
    for images_numbers, image_latest_launch in enumerate(image_latest_launch, 1):
        filename = f'spacex_latest_launch_{images_numbers}.jpg'
        image = requests.get(image_latest_launch).content
        with open(Path(f'{path}', f'{filename}'), 'wb') as file:
            file.write(image)


def get_pictures_by_launch_id(spacex_launch_id, path, url):
    response = requests.get(url)
    response.raise_for_status()
    images_launch = response.json()[spacex_launch_id]['links']['flickr']['original']
    for images_numbers, images_launch in enumerate(images_launch, 1):
        filename = f'spacex_{images_numbers}.jpg'
        image = requests.get(images_launch).content
        with open(Path(f'{path}', f'{filename}'), 'wb') as file:
            file.write(image)


def create_parser():
    parser = argparse.ArgumentParser(
        description=
        'The program downloads photos of Spacex launches by launch number (id).'
    )
    parser.add_argument(
        'id',
        help=
        'Enter the command in console: $ python fetch_spacex_launch_images.py {id}. '
        'Where id - is the flight_number of the launch of interest',
        nargs='?',
        type=int,
        default=None,
    )
    return parser


def main():
    url = 'https://api.spacexdata.com/v5/launches'
    Path("images_SpaceX").mkdir(parents=True, exist_ok=True)
    path = "images_SpaceX"
    parser = create_parser()
    spacex_launch_id = parser.parse_args().id
    if spacex_launch_id:
        get_pictures_by_launch_id(spacex_launch_id, path, url)
    else:
        get_pictures_latest_launch(path, url)
        if get_pictures_latest_launch(path, url) is None:
            print('There are no images from the last launch spacex on the server')


if __name__ == "__main__":

    main()
