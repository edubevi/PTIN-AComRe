from devices.person import *
from devices.vehicle import *
from devices.static_devices import *
from libs.sensors import *
from libs.helper import *
from faker import Faker

import sys

if __name__ == '__main__':

#Doctor 1 pacient 2 ambulancia 3 smoke 4 wheather 5

    #init
    fake = Faker('es_ES')
    type = int(sys.argv[1])

    if type == 1:
        device = Doctor(fake.name(), random_dni())
        building = random.choice(['A', 'B', 'Neapolis'])
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)

    elif type == 2:
        device = Patient(fake.name(), random_dni())
        building = random.choice(['A', 'B', 'Neapolis'])
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)
        device.setTemp(body_thermometer())
        device.setHeart_rate(heart_rate_monitor())
        device.setBlood_pressure(blood_pressure_monitor())

    elif type == 3:
        device = Ambulance(random_plate())

    elif type == 4:
        pass


    device.getInfo()
    print()
    while True:




        # if sys.argv[1] == "patient":
        #     device = Patient("Marc Marquez","45018752A")
        # elif sys.argv[1] == "ambulance":
        #     device = Ambulance("GAX12569")
        # elif sys.argv[1] == "doctor":
        #     device = Doctor("Toni Casanova", "21056871B", "AX321256")
        # else:
        #     sys.exit(1)
        #
        #
        # p1 = Patient('Marc Marquez', '45018752A','215', '01/04/2018')
        # lat, lon = ips_coordinates('Neapolis')
        # p1.setLatitude(lat)
        # p1.setLongitude(lon)
        # p1.setTemp(body_thermometer())
        # p1.setTemp(body_thermometer(p1.getTemp()))
        # p1.setTemp(body_thermometer(p1.getTemp()))
        # p1.setHeart_rate(heart_rate_monitor())
        # p1.setHeart_rate(heart_rate_monitor(p1.getHeart_rate()))
        # p1.setBlood_pressure(blood_pressure_monitor())
        # d1 = Doctor('Toni Casanova', '21056871B', 'AX321256')
        # lat, lon = ips_coordinates('B')
        # d1.setLatitude(lat)
        # d1.setLongitude(lon)
        #
        # a1 = Ambulance('GAX12569')
        # lat, lon = gps_coordinates()
        # lat, lon, line, dist = gps(2)
        # print(lat,lon)
        # lat, lon, line, dist = gps(2,line,dist)
        # print(lat,lon)
        # lat, lon, line, dist = gps(2,line,dist)
        # print(lat,lon)
        # lat, lon, line, dist = gps(2,line,dist)
        #
        # a1.setFuelAmount(gas_tank())
        # a1.setTirePressure(tyre_pressure_alarm())
        #
        # dev1 = Smoke_detector()
        # dev1.setStatus(smoke_detector())
        #
        #
        # p1.getInfo()
        # print()
        # d1.getInfo()
        # print()
        # a1.getInfo()
        # print()
        # dev1.getInfo()
        #
        # w1 = WeatherStation()
        # w1.set_temperature(thermometer())
        # w1.set_humidity(hygrometer())
        # w1.set_air_pressure(barometer())
        # w1.get_info()
