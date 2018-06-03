import requests
import json

#Amb activació
def createDevice(nametype):
    req = requests.post('http://ptin2018.herokuapp.com/api/devices',  data = nametype)
    #print(req.status_code,req.reason)
    retorn = json.loads(req.content)
    vdata = [retorn["id"], retorn["token"]]
    return vdata

def updateDevice(id, dades, token):
    headers = {"Authorization": "Bearer "+token}
    req = requests.put('https://ptin2018.herokuapp.com/api/devices/'+id+'/info', data = dades, headers = headers)
    #print(req.status_code, req.reason)

def enableDevice(id, token):
    dades = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"enabled\"\r\n\r\nTrue\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    dade = {'enabled' : True }

    caps = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Bearer "+token, 'Cache-Control': "no-cache" }
    response = requests.request("PUT", "https://ptin2018.herokuapp.com/api/devices/"+id, data=dade, headers=caps)
    #print(response.text)


