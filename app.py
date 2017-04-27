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

@ask.launch
def start():
    welcome_msg = "Willkomen"
    return question(welcome_msg)


@ask.intent("Intent",convert={})
def Intent():
    session.attributes['current_dialog'] = ''
    speech = ""
    return question(speech).standard_card(title='',
                           text="",
                           large_image_url='').reprompt("")



@ask.intent("AMAZON.YesIntent",convert={})
def ResponseYesIntent():
    speech=""
    if session.attributes['current_dialog'] == '' :
        return question(speech)
    elif session.attributes['current_dialog'] == '' :
        return question(speech)
    else :
        return statement(speech)


@ask.intent("AMAZON.NoIntent")
def ResponseNoIntent():
    speech=""
    if session.attributes['current_dialog'] == '' :
        return question(speech)
    elif session.attributes['current_dialog'] == '' :
        return question(speech)
    else :
        return statement(speech)


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
