import requests
from xml.dom.minidom import parseString
import uuid
import json 

api_login = '4m8qNd-9999'
api_transKey = 'MvV5cJxkVR'
provider_id = 550
url = 'https://sandbox-api.gpsrv.com/intserv/4.0/'

# returns a string uuid for each transaction id
def trans_id():
	return str(uuid.uuid4());

def get_trans_history(ein):
	data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id(), 'accountNo': ein, 'startDate': '2018-09-08', 'endDate': '2020-05-20'}
	r = requests.post(url + 'getTransHistory', data=data, cert='galileo148.pem')
	print(r.text)

	# xml parsing attempt
	# dom = parseString(r.text)
	# merchants = dom.getElementsByTagName('formatted_merchant_desc') # or merchant id?
	# balance = dom.getElementsByTagName('calculated_balance') #balance per
	#print(merchants)

def test():
	data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id(), 'accountNo':'074103447228','amount':'25.50','association':'visa','merchantName':'Fred Jones Bagels'}
	headers = {'Accept': 'application/json'}
	r = requests.post(url + 'createSimulatedCardAuth', data=data, cert='galileo148.pem', headers=headers)
	print(r.text)

	#json parsing attempt
	#data = r.json()
	# print(data)\

	# xml parsing attempt
	#dom = parseString(r.text)
	# merchants = dom.getElementsByTagName('response_data')
	#
	# print(merchants)

def galileo_cert_auth():
	data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id()}
	r = requests.post(url + 'ping', data=data, cert='galileo148.pem')

	dom = parseString(r.text)
	statusCode = dom.getElementsByTagName('status_code')
	print('ping response code=' + statusCode[0].firstChild.nodeValue)
	print(type(r))

if __name__ == '__main__':
	#galileo_cert_auth()
	#get_trans_history('0090909', '2018-09-08')
	test()
