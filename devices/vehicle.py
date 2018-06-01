import random


class Vehicle:

    def __init__(self):
        # Vehicle info
        self.__v_id = None
        # Location
        self.__lat = None
        self.__lon = None
        self.__plate = self.random_plate()
        self.__route = None
        self.__token = None

    # Getters
    def getId(self):
        return self.__v_id

    def getLatitude(self):
        return float(self.__lat)

    def getLongitude(self):
        return float(self.__lon)

    def getRoute(self):
        return self.__route

    def getPlate(self):
        return self.__plate

    def getToken(self):
        return self.__token

    # Setters
    def setId(self, id):
        self.__v_id = id

    def setLatitude(self, lat):
        self.__lat = lat

    def setLongitude(self, lon):
        self.__lon = lon

    def setRoute(self, r):
        self.__route = r

    def setToken(self, t):
        self.__token = t

    def random_plate(self):
        plate = []
        for _ in range(4):
            plate.append(random.randint(0, 9))
        for _ in range(3):
            plate.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        plate = ''.join(str(e) for e in plate)
        return plate


class Ambulance(Vehicle):

    def __init__(self):
        super(Ambulance, self).__init__()
        self.__fuel = 100
        self.__t_pressure = None
        self.__availability = 1
        self.__type = 2

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

    def getType(self):
        return int(self.__type)

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

    def jsonRegAmb(self):
        return {'name': self.getPlate(),
                'type': self.getType()}

    def jsonAmb(self):
        return {'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'fuel': self.getFuelAmount(),
                'pressure': self.getTirePressure()}

class Stretcher(Vehicle):

    def __init__(self):
        super(Stretcher, self).__init__()
        self.__availability = 1
        self.__battery_level = 100.0
        self.__building = None
        self.__type = 7

    # Getters

    def getAvailability(self):
        if self.__availability == 1:
            return "Available"
        else:
            return "Occupied"

    def getBuilding(self):
        return self.__building

    def getBatterylevel(self):
        return self.__battery_level

    def getType(self):
        return self.__type

    def getInfo(self):
        print("VEHICLE INFO:")
        print("id = " + self.getId())
        print("type = Stretcher")
        print("Battery = " + self.getBatterylevel() + "%")
        print()
        print("STATUS:")
        print(self.getAvailability())

    # Setters

    def setAvailability(self, status):
        self.__availability = status

    def setBatterylevel(self, level):
        self.__battery_level = level

    def setBuilding(self, building):
        self.__building = building

    def jsonRegStr(self):
        return {'name': self.getPlate(),
                'type': self.getType()}

    def jsonStr(self):
        return {'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'battery': self.getBatterylevel()}
