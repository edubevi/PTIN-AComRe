
class Vehicle:

    def __init__(self, id):
        # Vehicle info
        self.__v_id = id
        # Location
        self.__lat = None
        self.__lon = None

    # Getters
    def getId(self):
        return self.__v_id

    def getLatitude(self):
        return self.__lat

    def getLongitude(self):
        return self.__lon

    # Setters
    def setId(self, id):
        self.__v_id = id

    def setLatitude(self, lat):
        self.__lat = lat

    def setLongitude(self, lon):
        self.__lon = lon


class Ambulance(Vehicle):

    def __init__(self, id):
        super(Ambulance, self).__init__(id)
        self.__fuel = None
        self.__t_pressure = None
        self.__availability = 1

    # Getters
    def getFuelAmount(self):
        return self.__fuel

    def getTirePressure(self):
        return self.__t_pressure

    def getAvailability(self):
        if self.__availability == 1:
            return "Available"
        else:
            return "Occupied"

    def getInfo(self):
        print("VEHICLE INFO:")
        print("id = " + self.getId())
        print("type = Ambulance")
        print()
        print("STATUS:")
        print(self.getAvailability())
        print("Tyre pressure", self.getTirePressure())

    # Setters
    def setFuelAmount(self, fuel):
        self.__fuel = fuel

    def setTirePressure(self, pressure):
        self.__t_pressure = pressure

    def setAvailability(self, status):
        self.__availability = status

    def jsonAmb(self):
        return {'id': self.__v_id,
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'fuel': self.getFuelAmount(),
                'pressure': self.getTirePressure()}