import requests
from xml.dom.minidom import parseString
import string
import random

def galileo_cert_auth():
	data = {'apiLogin':'','apiTransKey':'','providerId':'','transactionId':'30323-random-string-86881'}
	r = requests.post('https://sandbox-api.gpsrv.com/intserv/4.0/ping', data=payload, cert='galileo148.pem')
