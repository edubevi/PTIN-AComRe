
from devices.person import *
from devices.vehicle import *
from devices.static_devices import *
from libs.sensors import *
from libs.helper import *
from faker import Faker
from libs.send import *
from libs.sockets import *
import sys
import threading
import getopt
import signal, time


def capturing_emergency(dev):
    ''' Funcio que executara el dispositiu Doctor i Stretcher(Camilla) que capturara el missatge enviat pel Backend per Socket en el servei
    Doctor-Pacient per tal d'establir una ruta al pacient que te una emergencia.'''

    while 1:
        try:
            data = socketreceive(dev.getSocket())
            if data:
                patient_device_= data['requester']
                dev.setLatitude(data['latitude'])
                dev.setLongitude(data['longitude'])
                dev.setAvailability(1)
                time.sleep(600) # Establim que estara 10 minuts ocupat i despres torna a estar disponible
                dev.setAvailability(0)
        except:
            #print("Error al llegir del socket")
            pass


def receive_button(d):
    while True:
        # signal.signal(signal.SIGUSR1, receive_signal)
        signal.sigwait((signal.SIGUSR1,))
        print('¡Button pushed!')
        if d.getType() == 3: # Envia senyal d'alarma d'incendis
            #Descomentar quan socketsend estigui acabada
            #socketsend('fire', d.getLatitude(), d.getLongitude(), d.getSocket())
            print("Alarma d'incendi enviada!")
        elif d.getType() == 4: # Envia senyal d'alarma Pacient
            #Descomentar quan socketsend estigui acabada
            #socketsend(2, d.getLatitude(), d.getLongitude(), d.getSocket())
            print("Emergencia enviada!")


def stay_alive(dev, timer):
    threading.Timer(timer, stay_alive, [dev, timer], {}).start()
    # Doctor
    if type == 1:
        if dev.getMovement() is 1:
            x, y = ips_coordinates(dev.getBuilding())
            dev.setLatitude(x)
            dev.setLongitude(y)
        data = dev.jsonDoc()
        print(data)
        updateDevice(dev.getPersonalid(), data, dev.getToken())
    # Patient
    elif type == 2:
        if dev.getMovement() is 1:
            x, y = ips_coordinates(dev.getBuilding())
            dev.setLatitude(x)
            dev.setLongitude(y)
        dev.setTemp(body_thermometer(dev.getTemp()))
        dev.setHeart_rate(heart_rate_monitor(dev.getHeart_rate()))
        dev.setBlood_pressure(blood_pressure_monitor(dev.getBlood_pressure()[0], dev.getBlood_pressure()[1]))

        data = dev.jsonPac()
        print(data)
        updateDevice(dev.getPersonalid(), data, dev.getToken())
    # Ambulance
    elif type == 3:
        f = dev.getFuelAmount()
        x,y,f,d = gps(dev.getRoute())
        dev.setLatitude(x)
        dev.setLongitude(y)
        dev.setFuelAmount(gas_tank(f, d))
        dev.setTirePressure(tyre_pressure_alarm())

        data = dev.jsonAmb()
        print(data)
        updateDevice(dev.getId(), data, dev.getToken())
    # Somoke detector
    elif type == 4:
        dev.setStatus(smoke_detector())
        data = dev.jsonSmoke()
        print(data)
        updateDevice(dev.getIdDev(), data, dev.getToken())
    # Thermometer
    elif type == 5:
        dev.set_temperature(thermometer())
        dev.set_humidity(hygrometer())
        dev.set_air_pressure(barometer())
        data = dev.jsonWeather()
        print(data)

        updateDevice(dev.getIdDev(), data, dev.getToken())
    # Air quality
    elif type == 6:
        data = dev.jsonAir()
        print(data)
        updateDevice(dev.getIdDev(), data, dev.getToken())
    # Nurse
    elif type == 7:
        data = dev.jsonNur()
        print(data)
        updateDevice(dev.getPersonalid(), data, dev.getToken())
    # Stretcher
    elif type == 8:
        data = dev.jsonStr()
        print(data)
        updateDevice(dev.getId(), data, dev.getToken())


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

    # Device is Doctor
    if type == 1:
        device = Doctor(fake.name())
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)
        # 0 no te moviment es static, 1 es mou
        device.setMovement(random.randint(0, 1))
        deviceID = createDevice(device.jsonRegDoc())
        socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0],deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setPersonalid(deviceID[0])
        device.setToken(deviceID[1])
        device.setSocket(socketID)

        if interval is None:
            interval = 10

        receive_emergency = threading.Thread(target=capturing_emergency, args=(device,), name='capturing_emergency')
        receive_emergency.setDaemon(True)
        receive_emergency.start()
        alive = threading.Thread(target=stay_alive, args=(device, interval,), name='stay_alive')
        alive.setDaemon(False)
        stay_alive(device, interval)

    # Device is Patient
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
        socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0],deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setPersonalid(deviceID[0])
        device.setToken(deviceID[1])
        #device.setSocket(socketID)

        if interval is None:
            interval = 10
        alive = threading.Thread(target=stay_alive, args=(device, interval,), name='stay_alive')
        alive.setDaemon(False)
        stay_alive(device, interval)

        # signal nomes pel main thread, passem stay_alive a un altre thread
        receive_button(device)

    # Device is Ambulance
    elif type == 3:
        device = Ambulance()
        route = random.choice([1,2,3,4,5,6])
        device.setRoute(route)
        x,y,_,_ = gps(route)
        device.setLatitude(x)
        device.setLongitude(y)
        deviceID = createDevice(device.jsonRegAmb())
        socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0],deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getPlate(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getPlate()))
        device.setId(deviceID[0])
        device.setToken(deviceID[1])
        device.setSocket(socketID)

        if interval is None:
            interval = 5
        stay_alive(device, 5)

    # Device is Smoke_Detector
    elif type == 4:
        device = Smoke_detector()
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)
        deviceID = createDevice(device.jsonRegSmoke())
        #socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0],deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setIdDev(deviceID[0])
        device.setToken(deviceID[1])
        #device.setSocket(socketID)

        if interval is None:
            interval = 10
        alive = threading.Thread(target=stay_alive, args=(device, interval,), name='stay_alive')
        alive.setDaemon(False)
        stay_alive(device, interval)

        # signal nomes pel main thread, passem stay_alive a un altre thread
        receive_button(device)

    elif type == 5:
        device = WeatherStation()
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)

        deviceID = createDevice(device.jsonRegWheather())
        socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0],deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setIdDev(deviceID[0])
        device.setToken(deviceID[1])
        device.setSocket(socketID)

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
        socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0],deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setIdDev(deviceID[0])
        device.setToken(deviceID[1])
        device.setSocket(socketID)

        if interval is None:
            interval = 300
        stay_alive(device, interval)
        # 300 seconds = 5 min

    elif type == 7:
        device = Nurse(fake.name())
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x,y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)

        deviceID = createDevice(device.jsonRegNur())
        socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0], deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getName(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getName()))
        device.setPersonalid(deviceID[0])
        device.setToken(deviceID[1])
        device.setSocket(socketID)

        if interval is None:
            interval = 10
        stay_alive(device, interval)

    elif type == 8:
        device = Stretcher()
        building = random.choice(['A', 'B', 'Neapolis'])
        device.setBuilding(building)
        x, y = spawn_position(building)
        device.setLatitude(x)
        device.setLongitude(y)
        deviceID = createDevice(device.jsonRegStr())
        socketID = createsocket(deviceID[0])
        print(deviceID[0])
        enableDevice(deviceID[0],deviceID[1])
        print("API: device type %d with name %s registered with ID %s" % (type, device.getPlate(), deviceID[0]))
        print(jsonfy_data(deviceID, type, device.getPlate()))
        device.setId(deviceID[0])
        device.setToken(deviceID[1])
        device.setSocket(socketID)

        if interval is None:
            interval = 300

        receive_emergency = threading.Thread(target=capturing_emergency, args=(device,), name='capturing_emergency')
        receive_emergency.setDaemon(True)
        receive_emergency.start()
        alive = threading.Thread(target=stay_alive, args=(device, interval,), name='stay_alive')
        alive.setDaemon(False)
        stay_alive(device, interval)

    else:   # default, no type defined
        usage()
