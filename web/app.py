#!/usr/bin/python3

from flask import Flask, g
from flask import request
from flask import jsonify
import requests
from xml.dom.minidom import parseString
import string
import sqlite3
import random
import blockchain

app = Flask(__name__)

@app.route('/', methods=['GET']) 
def info():
    return "It's running!"

@app.route('/register', methods=['POST'])
def register():
    register_info = request.get_json()
    print(register_info)

    query = 'INSERT INTO users(username, password) values(\'%s\', \'%s\')' % (
        register_info['username'],
        register_info['password']
    )
    insert_db(query)

    js = get_user_data(register_info['username'])
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
        'username' : user['username'],
        'password' : user['password'],
        'balance' : blockchain.getBalance(user['username'])
     }
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

