from socketIO_client import SocketIO


def socketsend(type, latitude, longitude, id):
    with SocketIO('https://ptin2018.herokuapp.com') as socketIO:
        socketIO.emit('alarm', {'type': type, 'lat': latitude, 'long': longitude, 'pacient': id})
        socketIO.wait(seconds=1)
