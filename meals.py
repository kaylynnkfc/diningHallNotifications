# This file is for use in a cronjob
# It is run with one command line argument (brunch or dinner), which specifies meal
# Feel free to add lunch, I didn't need that functionality
# MUST be modified to include your twilio info

import sys
from twilio.rest import TwilioRestClient
import requests
from bs4 import BeautifulSoup

def main():
    meal = sys.argv[1]
    menu = getMenu()

    messasge = ""

    # Change these values to represent what you need in your message
    if (meal == 'brunch'):
        message = "Brunch at Emerson:\n" + menu['Cushing/Emerson']['lunch'] + "\n\n Brunch at King:\n" + menu['King/Scales']['lunch']

    if (meal == 'dinner'):
        message = "Dinner at Emerson:\n" + menu['Cushing/Emerson']['dinner'] + "\n\n Dinner at King:\n" + menu['King/Scales']['dinner']

    print(message)

    # sendMessage(message)

# This parses the entire menu and returns a well formated data structure, see above for usage
def getMenu():
    url = "https://www.smith.edu/diningservices/menu_poc/cbord_menus.php"
    r = requests.get(url)

    parser = BeautifulSoup(r.text, 'html.parser')
    divs = parser.find_all('div', {'class':'smith-menu-wrapper context'})

    allInfo = {}

    for i in divs:
        p = BeautifulSoup(str(i), 'html.parser')
        mealNames = p.find_all('h4')
        hall = p.find_all('span')[0].decode_contents()
        food = p.find_all('table')

        entry = {}
        for j in range(len(mealNames)):
            meal = mealNames[j].decode_contents().lower()
            menu = food[j].decode_contents()
            menu = str(menu).replace("</td></tr><tr><td>", "\n")
            menu = str(menu).replace("<tr><td>", "")
            menu = str(menu).replace("</td></tr>", "")
            entry[meal] = menu

        allInfo[hall] = entry

    return allInfo

# This sends the text message.
# TODO: Fill in your info.
def sendMessage(message):

    # account_sid = ""
    # auth_token = ""
    # my_phone = ""
    # twilio_phone = ""

    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=my_phone, from_=twilio_phone, body=message)


if __name__ == "__main__":
    main()
