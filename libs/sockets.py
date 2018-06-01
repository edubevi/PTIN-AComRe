from socketIO_client_nexus import SocketIO

'''
#Falta testejar
def createsocket(id):
    with SocketIO('https://ptin2018.herokuapp.com', params={"query":id}) as socketIO:
        #socketIO.wait(seconds=3)
        return socketIO

##Falta testejar
def socketsend(alarmtype, lat, long, socket):
    socket.emit({"type":alarmtype, "latitude": lat, "longitude": long})
    #socket.wait(seconds=3)

##Falta testejar
def socketreceive(socket):
    recv = []
    socket.wait_for_callbacks({"requester": recv[0],"latitude": recv[1],"longitude": recv[2]})
    return recv
'''
#from socketIO_client import SocketIO, LoggingNamespace

def functionSocket(id, longitude, latitude, argument):

   #Function to receive position of pacient
   def location(*args):
       print ('data received')
       print (args)

   #Function to send second emit with token received and confirm general alarm
   def general(*args):
       print ('general received')
       print(args[0])
       socketIO.wait(seconds=5)
       socketIO.emit('generalAuthentication', {'requester': id, 'token': args[0]})

   #Function to receive confirmation OK with general signal
   def response(*args):
       print('Response')
       print (args)


   #Create socket
   socketIO = SocketIO('https://ptin2018.herokuapp.com', params={'id':id})

   #Functions to socket and endpoints
   socketIO.on('pacientLocation', location)
   socketIO.on('generalAuthentication', general)
   socketIO.on('generalResponse', response)

   if (argument == 'pacientEmitAlarm'):
       # Pacient send alarm
       socketIO.wait(seconds=5)
       socketIO.emit('alarm', {'type': 1, 'longitude': longitude, 'latitude': latitude})
       print("Emit OK")

   elif (argument == 'doctorListen'):
       # Doctor listen to pacientLocation
       socketIO.on('pacientLocation', location)
       socketIO.wait()

   elif (argument == 'pacientEmitGeneral'):
       # Pacient emit alarm general and confirm with token
       socketIO.wait(seconds=5) #wait for emit
       socketIO.emit('alarm', {'type': 2, 'longitude': longitude, 'latitude': latitude})
       socketIO.on('generalAuthentication', general)
       socketIO.on('generalResponse', response)
       socketIO.wait(seconds=10)
       print("Emit OK")

   elif (argument == 'fire'):
       socketIO.wait(seconds=3)
       socketIO.emit('fire')
       print("Emit OK")

   else:
       print('Error in argument [create, pacientEmitAlarm, doctorListen or pacientEmitGeneral]')