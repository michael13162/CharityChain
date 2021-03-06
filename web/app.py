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

    '''
    if ein_to_account_id(ein) is None:
        return

    galileo.create_transaction(username_to_account_id(username), ein_to_account_id(ein), amount, description)
    '''

    query = 'INSERT INTO trans(username, ein, amount, description) values(\'%s\', \'%s\', \'%s\', \'%s\')' % (
        username,
        ein,
        amount,
        description
    )
    insert_db(query)

@app.route('/charity', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def charity():
    charity_info = request.get_json()
    print(charity_info)

    ein = charity_info['ein']

    charity_info = charity_navigator.get_rating_info(ein)
    mission_statement, tag_line = get_charity_statements(ein)

    '''
    if ein_to_account_id(ein) is not None:
        trans_history = galileo.get_trans_history(ein_to_account_id(ein))
        balance = galileo.get_balance(ein_to_account_id(ein))
    else:
        trans_history = 'No transaction history'
        balance = 'Not registered'
    '''

    query = 'SELECT * FROM trans WHERE trans.ein=\'%s\'' % (
        ein
    )
    rows = query_db(query)
    if len(rows) == 0:
        js['trans_history'] = {}
    else:
        js['trans_history'] = rows

    query = 'SELECT SUM(trans.amount) AS balance FROM trans WHERE trans.ein=\'%s\'' % (
        ein
    )
    rows = query_db(query)
    if len(rows) == 0:
        js['balance'] = 0
    else:
        js['balance'] = rows[0]['balance']

    js = {
        #'trans_history': trans_history,
        #'balance': balance,
        'charity_info': charity_info,
        'mission_statement': mission_statement,
        'tag_line': tag_line
    }
    return Response(json.dumps(js), mimetype='application/json')

@app.route('/charities', methods=['GET'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def charities():
    query = 'SELECT charity.ein, charity.tag_line, charity.charity_name, charity.rating FROM charity ORDER BY rating DESC LIMIT 1000'

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

def get_charity_statements(ein):
    query = 'SELECT charity.mission_statement, charity.tag_line FROM charity WHERE charity.ein=\'%s\'' % (
        ein
    )

    rows = query_db(query)

    return rows[0]['mission_statement'], rows[0]['tag_line']

def username_to_account_id(username):
    query = 'SELECT user.account_id FROM user WHERE user.username=\'%s\'' % (
        username
    )
    
    rows = query_db(query)
    
    if len(rows) == 0:
        return None

    return rows[0]['account_id']

def ein_to_account_id(ein):
    query = 'SELECT user.account_id FROM user WHERE user.ein=\'%s\'' % (
        ein
    )

    rows = query_db(query)
    
    if len(rows) == 0:
        return None

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

    #js['balance'] = blockchain.getBalance(user['username'])
    '''
    js['balance'] = galileo.get_balance(username_to_account_id(user['username']))
    '''

    query = 'SELECT SUM(trans.amount) AS balance FROM trans WHERE trans.username=\'%s\'' % (
        username
    )
    rows = query_db(query)
    if len(rows) == 0:
        js['balance'] = 0
    else:
        js['balance'] = rows[0]['balance']
    
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

