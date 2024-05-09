import requests
for i in range(15):
    cookie = "name="+str(i)
    headers = {}
    r = requests.get('http://titan.picoctf.net:50473/', headers=headers)
    print(r.text)