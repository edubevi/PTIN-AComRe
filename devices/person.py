
class Person:

    def __init__(self, name):
        # Personal info
        self.__name = name
        self.__personal_id = None
        # Location
        self.__lat = None
        self.__lon = None
        self.__building = None
        self.__movement = None

    # Getters
    def getName(self):
        return self.__name

    def getPersonalid(self):
        return self.__personal_id

    def getLatitude(self):
        return float(self.__lat)

    def getLongitude(self):
        return float(self.__lon)

    def getBuilding(self):
        return self.__building

    def getMovement(self):
        return self.__movement

    # Setters
    def setName(self, name):
        self.__name = name

    def setPersonalid(self, p_id):
        self.__personal_id = p_id

    def setLatitude(self, lat):
        self.__lat = lat

    def setLongitude(self, lon):
        self.__lon = lon

    def setBuilding(self, b):
        self.__building = b

    def setMovement(self, m):
        self.__movement = m

class Patient(Person):

    def __init__(self, name):
       super(Patient, self).__init__(name)
       self.__temp = 38.0
       self.__heart_rate = 90.0
       self.__b_pressure = 60.0
       self.__doc_proximity = 0
       self.__type = 2

    # Getters
    def getType(self):
        return self.__type

    def getRoom(self):
        return self.__name

    def getDate_entry(self):
        return self.__date_entry

    def getTemp(self):
        return self.__temp

    def getHeart_rate(self):
        return self.__heart_rate

    def getBlood_pressure(self):
        return self.__b_pressure

    def getDoc_proximity(self):
        return "%.2f m" % self.__doc_proximity

    def getInfo(self):
        print("PERSONAL INFO:")
        print("Name = " + self.getName())
        print("Personal ID = " + self.getPersonalid())
        print()
        print("PATIENT INFO:")
        print("Room = " + self.__room)
        print("Date of entry: " + self.__date_entry)
        print("Nearest doctor at %f m" % (self.__doc_proximity))
        print()
        print("STATUS:")
        print(self.getTemp(), self.getHeart_rate(), self.getBlood_pressure())

    # Setters
    def setRoom(self, room):
        self.__room = room

    def setDate_entry(self, date):
        self.__date_entry = date

    def setTemp(self, temp):
        self.__temp = temp

    def setHeart_rate(self, rate):
        self.__heart_rate = rate

    def setBlood_pressure(self, pressure):
        self.__b_pressure = pressure

    def setDoc_proximity(self, prox):
        self.__doc_proximity = prox

    def jsonRegPac(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonPac(self):
        return {'id': self.getPersonalid(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'temp': self.getTemp() ,
                'heart': self.getHeart_rate(),
                'bloodD': self.getBlood_pressure()}


class Doctor(Person):
    def __init__(self, name):
        super(Doctor, self).__init__(name)
        self.__availability = 0
        self.__type = 1

    # Getters
    def getType(self):
        return self.__type

    def getDoc_id(self):
        return self.__doc_id

    def getAvailability(self):
        if self.__availability == 0:
            return "Available"
        else:
            return "Occupied"

    def getInfo(self):
        print("PERSONAL INFO:")
        print("Name = " + self.getName())
        print("Personal ID = " + self.getPersonalid())
        print()
        print("DOC INFO:")
        print("doc id =  " + self.__doc_id)
        print()
        print("STATUS:")
        print(self.getAvailability())

    # Setters
    def setDoc_id(self, id):
        self.__doc_id = id

    def setAvailability(self, status):
        self.__availability = status

    def jsonRegDoc(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonDoc(self):
        return {'id': self.getPersonalid(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude()}
