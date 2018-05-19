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
        print(data)
        updateDevice(dev.getPersonalid(), data)

    elif type == 2:
        if dev.getMovement() is 1:
            x, y = ips_coordinates(dev.getBuilding())
            dev.setLatitude(x)
            dev.setLongitude(y)
        dev.setTemp(body_thermometer(dev.getTemp()))
        dev.setHeart_rate(heart_rate_monitor(dev.getHeart_rate()))
        dev.setBlood_pressure(blood_pressure_monitor(dev.getBlood_pressure()[0],dev.getBlood_pressure()[1]))

        data = dev.jsonPac()
        print(data)
        updateDevice(dev.getPersonalid(), data)

    elif type == 3:
        f = dev.getFuelAmount()
        x,y,f,d = gps(dev.getRoute())
        dev.setLatitude(x)
        dev.setLongitude(y)
        dev.setFuelAmount(gas_tank(f, d))
        dev.setTirePressure(tyre_pressure_alarm())

        data = dev.jsonAmb()
        print(data)
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
        print(data)
        updateDevice(dev.getIdDev(), data)

    elif type == 6:
        data = dev.jsonAir()
        print(data)
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
        print(deviceID)
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID))
        print(jsonfy_data(deviceID, type, device.getName()))
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
        device.setTemp(body_thermometer(device.getTemp()))
        device.setHeart_rate(heart_rate_monitor(device.getHeart_rate()))
        device.setBlood_pressure(blood_pressure_monitor(device.getBlood_pressure()[0], device.getBlood_pressure()[1]))

        deviceID = createDevice(device.jsonRegPac())
        print(deviceID)
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID))
        print(jsonfy_data(deviceID, type, device.getName()))
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
        print(deviceID)
        print("API: device type %d with name %s registered with ID %s" % (type, device.getPlate(), deviceID))
        print(jsonfy_data(deviceID, type, device.getName()))
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
        print(deviceID)
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID))
        print(jsonfy_data(deviceID, type, device.getName()))
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
        print(deviceID)
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setIdDev(deviceID)

        if interval is None:
            interval = 900
        stay_alive(device, interval) # 900 seconds = 15 min to limit api calls

    elif type == 6:
        device = AirQuality()
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)

        deviceID = createDevice(device.jsonRegAir())
        print(deviceID)
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setIdDev(deviceID)

        if interval is None:
            interval = 300
        stay_alive(device, interval)
        # 300 seconds = 5 min

    else:   # default, no type defined
        usage()
