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
	r = requests.post(url + 'getTransHistory', data=data, cert='galileo148.pem', headers=headers)
	json = r.json()

	trans_history = {}
	

	print(json)

def test():
	create_account('Cole')

def create_transaction(sender, recipient, amount, description):
	data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id(),
				   'accountNo': sender, 'amount': amount, 'transferToAccountNo': recipient, 'message': description}
	r = requests.post(url + 'createAccountTransfer', data = data, cert='galileo148.pem', headers=headers)

def create_account(name):
	data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id(),
			   'prodId': product_id, 'firstName': name}
	r = requests.post(url + 'createAccount', data=data, cert='galileo148.pem', headers=headers)
	json = r.json()
	# returns the generated account ID
	return json['response_data']['new_account\\1']['pmt_ref_no']

if __name__ == '__main__':
	#galileo_cert_auth()
	#get_trans_history('0090909', '2018-09-08')
	get_trans_history('999900089841')
	#create_transaction('test1', 'test2', 20.00, 'hello')
	#create_account('test')
