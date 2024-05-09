import requests
cookie = "auth"+str(i)
headers = {'Cookie':'auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5ld191c2VyIiwicm9sZXMiOiJhZG1pbiIsImlhdCI6MTcxNDc4ODYwMCwiZXhwIjoxNzE0ODc1MDAwfQ.vftIhMMNiifdEiZ4yEWbnyVRRUwRcsf-W5Awm3BoMjI'}
r = requests.get('http://103.191.63.187:6060/', headers=headers)
print(r.text)