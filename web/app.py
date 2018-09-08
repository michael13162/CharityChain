#!/usr/bin/python3h

from flask import Flask
from flask import request
from flask import jsonify
#import blockchain

app = Flask(__name__)

@app.route('/', methods=['GET'])
def info():
    return "It's running!"

