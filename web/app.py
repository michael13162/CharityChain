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
import galileo
import charity_navigator

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/donate": {"origins": "http://localhost:4200"}, r"/charity": {"origins": "http://localhost:4200"}, r"/charities": {"origins": "http://localhost:4200"}, r"/login": {"origins": "http://localhost:4200"}, r"/register": {"origins": "http://localhost:4200"}})

@app.route('/donate', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def donate():
    donate_info = request.get_json()
    print(donate_info)

    username = donate_info['username']
    ein = donate_info['ein']
    amount = donate_info['amount']
    description = donate_info['description']

    galileo.create_transaction(username_to_account_id(username), ein_to_account_id(ein), amount, description)

@app.route('/charity', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def charity():
    charity_info = request.get_json()
    print(charity_info)

    ein = charity_info['ein']

    trans_history = galileo.get_trans_history(ein_to_account_id(ein))
    charity_info = charity_navigator.get_rating_info(ein)
    
    js = {
        'trans_history': trans_history,
        'charity_info': charity_info
    }
    return Response(json.dumps(js), mimetype='application/json')

@app.route('/charities', methods=['GET'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def charities():
    query = 'SELECT * FROM charity ORDER BY rating DESC'

    rows = query_db(query)

    js = {'charities': []} 
    for row in rows:
        charity = {
            'ein': row['ein'],
            'tag_line': row['tag_line'],
            'charity_name': row['charity_name'],
            'rating': row['rating']
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

    account_id = galileo.create_account(username)
	
    is_charity = register_info['is_charity']
    if is_charity:
        ein = register_info['ein']
    else:
        ein = 'not_applicable'

    query = 'INSERT INTO user(username, password, account_id, is_charity, ein) values(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
        username,
        password,
        account_id,
        is_charity,
        ein
    )
    insert_db(query)

    js = get_user_data(username)
    return Response(json.dumps(js), mimetype='application/json')

def username_to_account_id(username):
    query = 'SELECT user.account_id FROM user WHERE user.username=\'%s\'' % (
        username
    )

    rows = query_db(query)

    return rows[0]['account_id']

def ein_to_account_id(ein):
    query = 'SELECT user.account_id FROM user WHERE user.ein=\'%s\'' % (
        ein
    )

    rows = query_db(query)

    return rows[0]['account_id']

def get_user_data(username):
    query = 'SELECT * FROM user WHERE user.username=\'%s\'' % (
        username
    )

    rows = query_db(query)
    user = rows[0]

    js = {
        'username': user['username'],
        'password': user['password'],
        'is_charity': user['is_charity'],
        'ein': user['ein'],
    }
    if user['is_charity'] == 1:
        #js['balance'] = blockchain.getBalance(user['username'])
        js['balance'] = 0
    
    print(js)
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

