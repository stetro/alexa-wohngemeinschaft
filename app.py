from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

from random import randint

from flask import Flask
from flask import make_response

from flask import request
from flask import Flask, render_template

import requests

from flask_ask import Ask, statement, question, session, context
import logging

import json

app = Flask(__name__,static_url_path='')

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
orderQuestion = "Moechtest du noch etwas bestellen?"
orderFinish = "Ok, Vielen Dank fuer deine Bestellung"

orderArray = {}

orderContent = []
sessionId = "39"
@ask.launch
def start():
    welcome_msg = "Herzlich willkommen im Wohngemeinschaft. Um mir ihrer Bestellung aufzugeben, sagen Sie bitte einfach Starte Wohngemeinschaft.  Moechten Sie direkt bestellen, dann sagen Sie einfach. starte Wohngemeinschaft und bestelle. gefolgt von der Menuenummer oder dem Namen."+orderQuestion
    sessionId = "39"
    return question(welcome_msg)


@ask.intent("OrderByNumberIntent",convert={'menuNumber':int})
def OrderByNumberIntent(menuNumber):
    if menuNumber == None:
        speech =" Ich habe die Nummer nicht verstanden."
        return question(speech).reprompt(orderQuestion)
    orderContent.insert(0,menuNumber)
    print(orderContent)
    speech = "Sie haben die Nummer "+str(menuNumber)+" bestellt. "+orderQuestion
    print(speech)

    return question(speech).reprompt(orderQuestion)

@ask.intent("AMAZON.YesIntent",convert={})
def ResponseYesIntent():
    return question(orderQuestion)


@ask.intent("AMAZON.NoIntent")
def ResponseNoIntent():
    orderArray[sessionId] = orderContent
    return statement(orderFinish)


def get_alexa_location():
    URL =  "https://api.amazonalexa.com/v1/devices/{}/settings" \
           "/address".format(context.System.device.deviceId)
    TOKEN =  context.System.user.permissions.consentToken
    HEADER = {'Accept': 'application/json',
             'Authorization': 'Bearer {}'.format(TOKEN)}
    r = requests.get(URL, headers=HEADER)
    if r.status_code == 200:
        return(r.json())

@ask.intent("LocationIntent")
def getLocation():
    location = get_alexa_location()
    city = "Your City is {}! ".format(location["city"].encode("utf-8"))
    address = "Your address is {}! ".format(location["addressLine1"].encode("utf-8"))
    speech = city + address
    return statement(speech)

@app.route('/api/orders', methods=['GET'])
def orders():
    res = json.dumps(orderArray)
    return res

if __name__ == '__main__':
    app.run(debug=True)
