#!/usr/bin/python3h

from flask import Flask
from flask import request
from flask import jsonify
import requests
from xml.dom.minidom import parseString
import string
import random
import blockchain

app = Flask(__name__)

def galileo_cert_auth():
	data = {'apiLogin':'','apiTransKey':'','providerId':'','transactionId':'30323-random-string-86881'}
	r = requests.post('https://sandbox-api.gpsrv.com/intserv/4.0/ping', data=payload, cert='galileo148.pem')

@app.route('/', methods=['GET']) 
def info():
    return "It's running!"

