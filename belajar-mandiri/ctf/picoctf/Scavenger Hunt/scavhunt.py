import requests
req = requests.get('http://mercury.picoctf.net:5080/')
print(req.headers)