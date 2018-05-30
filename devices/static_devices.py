from faker import Faker


class Static_Device:

    def __init__(self):
        # Location
        self.__idDev = None
        self.__lat = None
        self.__lon = None
        self.__building = None
        fake = Faker()
        self.__name = fake.mac_address()
        self.__token = None


    # Getters
    def getIdDev(self):
        return self.__idDev

    def getLatitude(self):
        return float(self.__lat)

    def getLongitude(self):
        return float(self.__lon)

    def getBuilding(self):
        return self.__building

    def getName(self):
        return self.__name

    def getToken(self):
        return self.__token


    # Setters
    def setIdDev(self, idDev):
        self.__idDev = idDev

    def setLatitude(self, lat):
        self.__lat = lat

    def setLongitude(self, lon):
        self.__lon = lon

    def setBuilding(self, b):
        self.__building = b

    def setToken(self, t):
        self.__token = t


class Smoke_detector(Static_Device):

    def __init__(self):
        super(Smoke_detector, self).__init__()
        self.__status = 0
        self.__type = 3

    # Getters
    def getType(self):
        return int(self.__type)

    def getStatus(self):
        if self.__status == 0:
            return "OK"
        else:
            return "FIRE DETECTED"

    def getInfo(self):
        print("STATIC DEVICE INFO:")
        print("type = smoke_detector")
        print()
        print("STATUS:")
        print(self.getStatus())

    # Setters
    def setStatus(self, status):
        self.__status = status

    def jsonRegSmoke(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonSmoke(self):
        return {'id': self.getIdDev(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'status': self.getStatus()}


class AirQuality(Static_Device):
    def __init__(self):
        super(AirQuality, self).__init__()
        self.__id = None
        self.__no2 = 4
        self.__no2_unit = "µg/m³"
        self.__pm10 = 14
        self.__pm10_unit = "µg/m³"
        self.__type = 6

    def getType(self):
        return int(self.__type)

    def set_no2(self, n):
        self.__no2 = n

    def set_pm10(self, p):
        self.__pm10 = p

    def jsonRegAir(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonAir(self):
        return {'id': self.getIdDev(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'no2': self.__no2,
                'pm10': self.__pm10}


class WeatherStation(Static_Device):

    def __init__(self):
        super(WeatherStation, self).__init__()
        self.__id = None
        self.__temp = None
        self.__temp_unit = "C"
        self.__hum = None
        self.__hum_unit = "%"
        self.__air = None
        self.__air_unit = "hPa"
        self.__type = 5

    def set_temperature(self, t):
        self.__temp = t

    def set_humidity(self, h):
        self.__hum = float(h) * 100

    def set_air_pressure(self, a):
        self.__air = a

    def getType(self):
        return int(self.__type)

    def get_info(self):
        print("Weather station:")
        print()
        print("Temperatura: %d C" % self.__temp)
        print("Humitat: %d %%" % self.__hum)
        print("Pressio aire: %d hPa" % self.__air)

    def jsonRegWheather(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonWeather(self):
        return {'id': self.getIdDev(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'temperature': self.__temp,
                'humidity': self.__hum,
                'air': self.__air}
