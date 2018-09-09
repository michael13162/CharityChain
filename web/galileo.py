import requests
from xml.dom.minidom import parseString
import uuid
import json 

api_login = '4m8qNd-9999'
api_transKey = 'MvV5cJxkVR'
provider_id = 550
url = 'https://sandbox-api.gpsrv.com/intserv/4.0/'
product_id = 5094
headers = {'response-content-type': 'json'}

# returns a string uuid for each transaction id
def trans_id():
    return str(uuid.uuid4());

def get_trans_history(account_id):
    data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id(),
            'accountNo': account_id, 'startDate': '2018-09-08', 'endDate': '2020-05-20'}
    r = requests.post(url + 'getAllTransHistory', data=data, cert='galileo148.pem', headers=headers)
    json_response = r.json()

    trans_history = {}
    trans_count = 0
    for transaction in json_response['response_data']['transactions']:
        if 'formatted_merchant_desc' not in transaction:
            merchant = 'None'
        else:
            merchant = transaction['formatted_merchant_desc']
        amount = transaction['amt']
        time = transaction['post_ts']
        description = transaction['details']
        trans_map = {'merchant': merchant, 'amount': amount, 'time':time, 'description':description}
        trans_history['transaction' + str(trans_count)] = trans_map

    return trans_history

def test():
    id1 = create_account('grrrrr')
    id2 = create_account('mooooboooo')
    print(id1)
    print(id2)

    print(get_balance(id1))


    create_transaction(id1, id2, 10.00, 'lol')

    get_trans_history(id1)

def create_transaction(sender, recipient, amount, description):
    data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id(),
                   'accountNo': sender, 'amount': amount, 'transferToAccountNo': recipient, 'message': description}
    r = requests.post(url + 'createAccountTransfer', data = data, cert='galileo148.pem', headers=headers)

def create_account(name):
    data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id(),
               'prodId': product_id, 'firstName': name, 'loadAmount': 100.00}
    r = requests.post(url + 'createAccount', data=data, cert='galileo148.pem', headers=headers)
    json = r.json()
    # returns the generated account ID
    return json['response_data']['new_account\\1']['pmt_ref_no']

def get_balance(account_id):
    data = {'apiLogin': api_login, 'apiTransKey': api_transKey, 'providerId': provider_id, 'transactionId': trans_id(),
            'accountNo': account_id}
    r = requests.post(url + 'getBalance', data=data, cert='galileo148.pem', headers=headers)
    return r.json()['response']['response_data']['balance']

# if __name__ == '__main__':
#     test()
