#!/usr/bin/python3

from flask import Flask, g, jsonify, request, Response
from flask_cors import CORS, cross_origin
import requests
import json
from xml.dom.minidom import parseString
import string
import sqlite3
import random
import blockchain

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/donate": {"origins": "http://localhost:4200"}, r"/charity": {"origins": "http://localhost:4200"}, r"/charities": {"origins": "http://localhost:4200"}, r"/login": {"origins": "http://localhost:4200"}, r"/register": {"origins": "http://localhost:4200"}})

@app.route('/transaction', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def transaction():
    donate_info = request.get_json()

    sender = donate_info['sender']
    recipient = donate_info['recipient']
    amount = donate_info['amount']
    description = donate_info['description']

    galileo.make_transaction(sender, recipient, amount, description)

@app.route('/charity', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def charity():
    charity_info = request.get_json()

    ein = charity_info['ein']

    js = galileo.get_transactions(ein)
    js['charity_navigator'] = charity_navigator.get_rating(ein)

    return Response(json.dumps(js), mimetype='application/json')

@app.route('/charities', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def charities():
    search_string = request.get_json()['search_string']
    query = 'SELECT * FROM charity WHERE charity.charityName LIKE \'%%s%\' ORDER BY charity.score DESC' % (
        search_string
    )

    rows = query_db(query)

    js = {'charities': []} 
    for row in rows:
        charity = {
            'ein': row['ein'],
            'charity_name': row['charity_name'],
            'score': row['score']
        }

        js['charities'].append(charity)

    return Response(json.dumps(js), mimetype='application/json')


@app.route('/login', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def login():
    login_info = request.get_json()
    print(login_info)

    username = login_info['username']
    password = login_info['password']

    js = get_user_data(username)
    return Response(json.dumps(js), mimetype='application/json')

@app.route('/register', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def register():
    register_info = request.get_json()
    print(register_info)

    username = register_info['username']
    password = register_info['password']

    is_charity = register_info['is_charity']
    if is_charity:
        ein = register_info['ein']
    else:
        ein = 'not_applicable'

    query = 'INSERT INTO user(username, password, is_charity, ein) values(\'%s\', \'%s\', \'%s\', \'%s\')' % (
        username,
        password,
        is_charity,
        ein
    )
    insert_db(query)

    js = get_user_data(username)
    return Response(json.dumps(js), mimetype='application/json')

def get_user_data(username):
    query = 'SELECT * FROM user WHERE user.username=\'%s\'' % (
        username
    )

    rows = query_db(query)
    if len(rows) != 1:
        return None

    user = rows[0]

    print(user)

    js = {
        'username': user['username'],
        'password': user['password'],
        'is_charity': user['is_charity'],
        'ein': user['ein'],
    }
    if user['is_charity'] == 1:
        #js['balance'] = blockchain.getBalance(user['username'])
        js['balance'] = 0

    return js

def insert_db(query):
    cur = get_db().cursor()
    cur.execute(query)
    get_db().commit()
    cur.close()

def query_db(query):
    cur = get_db().cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('../database/database.db')
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

