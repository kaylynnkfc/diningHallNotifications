import sys
from twilio.rest import TwilioRestClient
import requests
from bs4 import BeautifulSoup

def main():
    meal = sys.argv[1]
    menu = getMenu()

    messasge = ""

    if (meal == 'brunch'):
        message = "Brunch at Emerson:\n" + menu['Cushing/Emerson']['lunch'] + "\n Brunch at King:\n" + menu['King/Scales']['lunch']

    if (meal == 'dinner'):
        message = "Dinner at Emerson:\n" + menu['Cushing/Emerson']['dinner'] + "\n Dinner at King:\n" + menu['King/Scales']['dinner']

    sendMessage(message)


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
        food = p.find_all('p')

        entry = {}
        for j in range(len(mealNames)):
            meal = mealNames[j].decode_contents().lower()
            menu = food[j].decode_contents()
            menu = str(menu).replace("<br/>", "\n")
            entry[meal] = menu

        allInfo[hall] = entry

    return allInfo

def sendMessage(message):
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=my_phone, from_=twilio_phone, body=message)


if __name__ == "__main__":
    main()
