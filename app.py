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

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
orderQuestion = "Moechtest du etwas noch bestellt?"
orderFinish = "Ok, Vielen Dank fur deine Bestellung"

orderArray = {}

orderContent = []

@ask.launch
def start():
    welcome_msg = "Willkomen"+orderQuestion
    return question(welcome_msg)


@ask.intent("OrderByNumberIntent",convert={'menuNumber':int})
def OrderByNumberIntent(menuNumber):
    orderContent.append(menuNumber)
    speech = "Sie haben Nummer "+str(menuNumber)+" bestellt. "+orderQuestion
    return question(speech).reprompt(orderQuestion)



@ask.intent("AMAZON.YesIntent",convert={})
def ResponseYesIntent():
    return question(orderQuestion)


@ask.intent("AMAZON.NoIntent")
def ResponseNoIntent():
    #orderArray[sessionId] = orderContent
    print (str(orderContent))
    return statement(orderFinish).standard_card(title='Bestellung',
                           text="Bestellung Nummer",
                           large_image_url='')


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


if __name__ == '__main__':
    app.run(debug=True)
