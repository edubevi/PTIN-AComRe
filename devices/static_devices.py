class Static_Device:

    def __init__(self):
        # Location
        self.__lat = None
        self.__lon = None

    # Getters
    def getLatitude(self):
        return self.__lat

    def getLongitude(self):
        return self.__lon

    # Setters
    def setLatitude(self, lat):
        self.__lat = lat

    def setLongitude(self, lon):
        self.__lon = lon


class Smoke_detector(Static_Device):

    def __init__(self):
        super(Smoke_detector, self).__init__()
        self.__status = 0

    # Getters
    def getStatus(self):
        if self.__status == 0:
            return 'OK'
        else:
            return 'FIRE DETECTED'

    def getInfo(self):
        print 'STATIC DEVICE INFO:'
        print 'type = smoke_detector'
        print
        print 'STATUS:'
        print self.getStatus()

    # Setters
    def setStatus(self, status):
        self.__status = status