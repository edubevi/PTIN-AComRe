import requests

req = requests.post('https://ptin2018.herokuapp.com/api/devices', data = {'name': 'joan13','latitude':'13','longitude':'13'})
print (req.status_code, req.reason)
