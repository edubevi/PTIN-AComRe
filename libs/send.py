import requests
import json

def createDevice(nametype):
    req = requests.post('http://ptin2018.herokuapp.com/api/devices',  data = nametype)
    retorn = json.loads(req.content)
    vdata = [retorn["id"], retorn["token"]]
    return vdata

def updateDevice(id, dades):
    ##INCLOURE EN EL HEADER EL TOKEN
    req = requests.put('https://ptin2018.herokuapp.com/api/devices/'+id, data = dades)
    #print (req.status_code, req.reason)
