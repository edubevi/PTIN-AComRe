import requests

def post(varjson):
    req = requests.post('https://ptin2018.herokuapp.com/api/devices',  data = varjson)
    print (req.status_code, req.reason)
