from devices.person import *
from devices.vehicle import *
from devices.static_devices import *
from libs.sensors import *
from libs.helper import *
from faker import Faker
from libs.send import *
import sys
import threading
import getopt


def stay_alive(dev, interval=10):
    threading.Timer(interval, stay_alive, [dev], {}).start()
    if type == 1:
        if dev.getMovement() is 1:
            x, y = ips_coordinates(dev.getBuilding())
            dev.setLatitude(x)
            dev.setLongitude(y)
        data = dev.jsonDoc()
        updateDevice(dev.getPersonalid(), data)

    elif type == 2:
        if dev.getMovement() is 1:
            x, y = ips_coordinates(dev.getBuilding())
            dev.setLatitude(x)
            dev.setLongitude(y)
        dev.setTemp(body_thermometer(dev.getTemp()))
        dev.setHeart_rate(heart_rate_monitor(dev.getHeart_rate()))
        dev.setBlood_pressure(blood_pressure_monitor())

        data = dev.jsonPac()
        updateDevice(dev.getPersonalid(), data)

    elif type == 3:
        x,y,_,d = gps(dev.getRoute())
        dev.setLatitude(x)
        dev.setLongitude(y)
        dev.setFuelAmount(gas_tank(d))
        dev.setTirePressure(tyre_pressure_alarm())

        data = dev.jsonAmb()
        updateDevice(dev.getId(), data)

    elif type == 4:
        dev.setStatus(smoke_detector())
        data = dev.jsonSmoke()
        print(data)
        updateDevice(dev.getIdDev(), data)

    elif type == 5:
        dev.set_temperature(thermometer())
        dev.set_humidity(hygrometer())
        dev.set_air_pressure(barometer())
        data = dev.jsonWeather()
        updateDevice(dev.getIdDev(), data)

def usage():
    print("usage: main.py -t <device_type> -i <time_interval>")
    sys.exit(2)

if __name__ == '__main__':

    #init
    fake = Faker('es_ES')

    try:
        opts, args = getopt.getopt(sys.argv[1:],"t:i:",["type=","interval="])
    except getopt.GetoptError:
        usage()
    interval = None
    for opt, arg in opts:
        if opt in ("-t", "--type"):
            type = int(arg)
        elif opt in ("-i", "--interval"):
            interval = int(arg)

    if type == 1:
        device = Doctor(fake.name())
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)
        #0 no te moviment es static, 1 es mou
        device.setMovement(random.randint(0, 1))

        deviceID = createDevice(device.jsonRegDoc())
        device.setPersonalid(deviceID)

        if interval is None:
            interval = 10
        stay_alive(device, interval)

    elif type == 2:
        device = Patient(fake.name())
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x, y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)
        device.setTemp(body_thermometer())
        device.setHeart_rate(heart_rate_monitor())
        device.setBlood_pressure(blood_pressure_monitor())

        deviceID = createDevice(device.jsonRegPac())
        device.setPersonalid(deviceID)

        if interval is None:
            interval = 10
        stay_alive(device, interval)

    elif type == 3:
        device = Ambulance()
        route = random.choice([1,2,3,4,5,6])
        device.setRoute(route)
        x,y,_,_ = gps(route)
        device.setLatitude(x)
        device.setLongitude(y)

        deviceID = createDevice(device.jsonRegAmb())
        device.setId(deviceID)

        if interval is None:
            interval = 5
        stay_alive(device, 5)

    elif type == 4:
        device = Smoke_detector()
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)

        deviceID = createDevice(device.jsonRegSmoke())
        device.setIdDev(deviceID)

        if interval is None:
            interval = 10
        stay_alive(device, interval)

    elif type == 5:
        device = WeatherStation()
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)

        deviceID = createDevice(device.jsonRegWheather())
        device.setIdDev(deviceID)

        if interval is None:
            interval = 900
        stay_alive(device, interval) # 900 seconds = 15 min to limit api calls

    else:   # default, no type defined
        usage()
