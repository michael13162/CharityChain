import requests
from xml.dom.minidom import parseString
import uuid

api_login = 4m8qNd-9999
api_transKey = MvV5cJxkVR
provider_id = 550
url = https://sandbox-api.gpsrv.com/intserv/4.0/

def galileo_cert_auth():
	data = {'apiLogin': api_login,'apiTransKey': api_transKey, 'providerId': provider_id,'transactionId': trans_id()}
	r = requests.post('https://sandbox-api.gpsrv.com/intserv/4.0/ping', data=payload, cert='galileo148.pem')

	dom = parseString(r.text)
	statusCode = dom.getElementsByTagName('status_code')
	print('ping response code=' + statusCode[0].firstChild.nodeValue)

def trans_id():
	return str(uuid.uuid4());
