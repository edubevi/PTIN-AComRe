from socketIO_client_nexus import SocketIO


def socketsend(alarmtype, lat, long, id):
    with SocketIO('https://ptin2018.herokuapp.com', params={'id': id}) as socketIO:
        socketIO.emit(alarmtype)
        socketIO.wait(seconds=3)
