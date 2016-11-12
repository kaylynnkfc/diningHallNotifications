from flask import Flask
from flask import render_template
from twilio.rest import TwilioRestClient
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def sendMessage():
    client = TwilioRestClient(account_sid, auth_token)

    menus = getMenuInfo()
    message = "Dinner at Emerson:\n" + menus["Cushing/Emerson"]['dinner'] + "\nDinner at King:\n" + menus['King/Scales']['dinner']
    message = client.messages.create(to=my_phone, from_=twilio_phone, body=message)
    return render_template('sent.html')


def getMenuInfo():
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


if __name__ == "__main__":
    app.run(debug=True)
