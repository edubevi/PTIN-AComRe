import numpy, random

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
        self.__token = None

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

    def getToken(self):
        return self.__token

    # Setters
    def setToken(self, t):
        self.__token = t

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

    def setToken(self, t):
        self.__token = t

class Patient(Person):

    def __init__(self, name):
       temp_values = [35.0, 36.0, 37.0, 38.0, 39.0, 40.0]
       hrate_values = [random.randint(40,60),(random.randint(60,100)),(random.randint(100,140)),random.randint(140,191)]
       sys_values = [random.randint(70,90),random.randint(90,120),random.randint(120,140),random.randint(140,181)]
       dia_values = [random.randint(40,60),random.randint(60,80),random.randint(80,90),random.randint(90,101)]
       super(Patient, self).__init__(name)
       self.__temp = numpy.random.choice(temp_values,p=[0.05,0.3,0.3,0.2,0.1,0.05])
       self.__heart_rate = numpy.random.choice(hrate_values,p=[0.08,0.7,0.2,0.02])
       self.__sys = numpy.random.choice(sys_values,p=[0.05,0.7,0.2,0.05])
       self.__dia = numpy.random.choice(dia_values,p=[0.05,0.7,0.2,0.05])
       self.__doc_proximity = 0
       self.__type = 4

    # Getters
    def getType(self):
        return int(self.__type)

    def getRoom(self):
        return self.__name

    def getDate_entry(self):
        return self.__date_entry

    def getTemp(self):
        return self.__temp

    def getHeart_rate(self):
        return self.__heart_rate

    def getBlood_pressure(self):
        return self.__sys, self.__dia

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

    def setBlood_pressure(self, b_pressure):
        self.__sys = b_pressure[0]
        self.__dia = b_pressure[1]

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
        spec_list = ["GENERAL", "CARDIOLOGIST"]
        super(Doctor, self).__init__(name)
        self.__speciality = numpy.random.choice(spec_list,p=[0.5,0.5])
        self.__availability = 0
        self.__type = 1

    # Getters

    def getSpec(self):
        return self.__speciality

    def getType(self):
        return int(self.__type)

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
        print("Speciality = " + self.getSpec())
        print()
        print("DOC INFO:")
        print("doc id =  " + self.__doc_id)
        print()
        print("STATUS:")
        print(self.getAvailability())

    # Setters
    def setSpec(self, spec):
        self.__speciality = spec

    def setDoc_id(self, id):
        self.__doc_id = id

    def setAvailability(self, status):
        self.__availability = status

    def jsonRegDoc(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonDoc(self):
        return {'id': self.getPersonalid(),
                'speciality': self.getSpec(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude()}


class Nurse(Person):
    def __init__(self, name):
        super(Nurse, self).__init__(name)
        self.__availability = 0
        self.__type = 7

    # Getters
    def getType(self):
        return int(self.__type)

    def getAvailability(self):
        if self.__availability == 0:
            return "Available"
        else:
            return "Occupied"

    # Setters
    def setAvailability(self, status):
        self.__availability = status

    def jsonRegNur(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonNur(self):
        return {'id': self.getPersonalid(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude()}
