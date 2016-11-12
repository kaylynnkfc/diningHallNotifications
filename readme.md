# About

App created for personal use to get text messages with the menu for that day for Smith's dining halls.



# Crontab Setup:

* pip install -r requirements.txt
* sudo crontab -e
* Find where python and meals.py are stored
* Add lines (with correct paths):

      0 2 * * * /home/kaylynn/anaconda2/bin/python /home/kaylynn/Documents/WebDev/twilio/meals.py dinner

      30 7 * * SAT,SUN /home/kaylynn/anaconda2/bin/python /home/kaylynn/Documents/WebDev/twilio/meals.py brunch

# Flask Webapp Setup:

* pip install -r requirements.txt
* pip install flask
* python run.py
* go to page
