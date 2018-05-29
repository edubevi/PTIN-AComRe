from socketIO_client_nexus import SocketIO


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