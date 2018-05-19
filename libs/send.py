import requests
import json

def createDevice(nametype):
    req = requests.post('http://ptin2018.herokuapp.com/api/devices',  data = nametype)
    retorn = json.loads(req.content)
    vdata = [retorn["id"], retorn["token"]]
    return vdata

def updateDevice(id, dades, token):
    headers = {"Authorization": "Bearer "+token}
    req = requests.put('https://ptin2018.herokuapp.com/api/devices/'+id, data = dades, headers = headers)
    #print (req.status_code, req.reason)
