import requests
import json

def createDevice(nametype):
    req = requests.post('http://ptin2018.herokuapp.com/api/devices',  data = nametype)
    retorn = json.loads(req.content)
    return retorn["id"]

def updateDevice(id, dades):
    req = requests.put('https://ptin2018.herokuapp.com/api/devices/'+id, data = dades)
    #print (req.status_code, req.reason)
