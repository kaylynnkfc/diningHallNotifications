# About

App created for personal use to get text messages with the menu for that day for Smith's dining halls.
Two main ways to use: through a cron job, or through the webapp. Instructions for setup are below.
Note that the cron job automates the texts, whereas the webapp sends texts when a button is pressed.

If you want to use yourself, you need API information from Twilio (mine has been removed) and you should probably customize what dining halls/meals you are interested in.

## Notes:
* The structure of the page I'm parsing may change. This code worked on 11/12/16.
* This project has a specific audience (students at Smith College), but feel free to contribute

## Crontab Setup:

* pip install -r requirements.txt
* sudo crontab -e
* Find where python and meals.py are stored
* Add lines (with correct paths):

      0 2 * * * [python path] [path to]meals.py [meal: dinner or brunch]

      30 7 * * SAT,SUN [python path] [path to]meals.py [meal: dinner or brunch]

## Flask Webapp Setup:

* pip install -r requirements.txt
* pip install flask
* python run.py
* go to page


## Screenshots:

![img]
[img]: /images/screenshot.png
