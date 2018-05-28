from socketIO_client_nexus import SocketIO


def createsocket(id):
    with SocketIO('https://ptin2018.herokuapp.com', params={"query":id}) as socketIO:
        socketIO.wait(seconds=3)
        return socketIO

def socketsend(alarmtype, lat, long, socket):
    socket.emit({"type":alarmtype, "latitude": lat, "longitude": long})
    socket.wait(seconds=3)

##No esta acabat
def socketreceive(socket):

    socket.wait_for_callbacks({"requester": "All the user data","latitude": 0,"longitude": 0})