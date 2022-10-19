# Space Telegram

The program downloads photos on specified dates from the resources of Spacex and Nasa and then publishes them in the telegram channel

### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777/Lesson4-web-servises-API-Devman](https://github.com/VAChess777/Lesson4-web-servises-API-Devman), or clone the `git` repository to a local folder:
```
git clone https://github.com/VAChess777/Lesson4-web-servises-API-Devman.git
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### How to run the program:

Run the script ```fetch_spacex_launch_images.py``` with the command:
```bach
$ python fetch_spacex_launch_images.py {id}.
'Where id - is the flight_number of the launch of interest'
```
Run the script ```fetch_nasa_epic_picture.py``` with the command:
```bach
$ python fetch_nasa_epic_picture.py -d(--date) {YYYY-mm-dd}. '
'Where YYYY-mm-dd - is the start date for the download epic image day from NASA. '
'if you do not enter -s(--start_date), then default = today'
```
Run the script ```fetch_nasa_astronomy_image_day.py``` with the command:
```bach
'$ python fetch_nasa_astronomy_image_day.py -s(--start_date) {YYYY-mm-dd}. '
'Where YYYY-mm-dd - is the start date for the download astronomy image day from NASA. '
'if you do not enter -s(--start_date), then default = today'
```
Run the script ```images_nasa_telegram_bot.py``` with the command:
```bach
'$ python images_nasa_telegram_bot.py -t(--time) '
'{value in seconds(at least 15 seconds)}. '
'Where {value in seconds} this is the value in seconds of the frequency '
'of sending images to the channel by the bot'
' If you do not enter, then the default value is 14400 seconds(4 hours) '
```

### How the program works:

The program consists of 4 scripts:
```fetch_spacex_launch_images.py``` - 'The program downloads photos of Spacex launches by launch number (id).'
```fetch_nasa_epic_picture.py``` - 'The program downloads an epic image of the Earth of the day from a NASA server.'
```fetch_nasa_astronomy_image_day.py``` -  'The program downloads astronomical images of the day from the NASA server.'
```images_nasa_telegram_bot.py``` - 'The program edits the images to the required size and sends the images to the telegram channel'
            

### Features works of the program:

The `fetch_spacex_launch_images.py` program contains the functions:

* The `picture_latest_launch` function - checks and downloads photos from the last launch from the SpaceX server
* The `spacex_id_launch_picture` function - checks and downloads photos from the SpaceX server for the date
* The `create_parser` function - parser function
* The `def main():` main function

The `fetch_nasa_epic_picture.py` program contains the functions:

* The `nasa_epic_picture_number` function - gets the numbers of the required pictures from the server response
* The `nasa_epic_picture_urls` function - based on the numbers of the pictures gets the necessary links to the photos
* The `nasa_epic_picture_downloads` function - a function that immediately downloads pictures from the NASA server
* The `create_parser` function - parser function
* The `def main():` main function

The `fetch_nasa_astronomy_image_day.py` program contains the functions:

* The `nasa_astronomy_picture_day` function - downloads images from the NASA server on dates of interest
* The `create_parser` function - parser function
* The `def main():` main function

The `images_nasa_telegram_bot.py` program contains the functions:

* The `all_photos` function - gets all downloaded images from directories using the above scripts
* The `size_images_for_telegram` function - changes the size of the images to suitable for placement in the telegram
* The `create_parser` function - parser function
* The `def main():` main function

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
