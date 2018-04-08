from devices.person import *
from devices.vehicle import *
from devices.static_devices import *
from libs.sensors import *

if __name__ == '__main__':

    p1 = Patient('Marc Marquez', '45018752A','215', '01/04/2018')
    lat, lon = ips_coordinates('Neapolis')
    p1.setLatitude(lat)
    p1.setLongitude(lon)
    p1.setTemp(body_thermometer())
    p1.setTemp(body_thermometer(p1.getTemp()))
    p1.setTemp(body_thermometer(p1.getTemp()))
    p1.setHeart_rate(heart_rate_monitor())
    p1.setHeart_rate(heart_rate_monitor(p1.getHeart_rate()))
    p1.setBlood_pressure(blood_pressure_monitor())
    d1 = Doctor('Toni Casanova', '21056871B', 'AX321256')
    lat, lon = ips_coordinates('B')
    d1.setLatitude(lat)
    d1.setLongitude(lon)

    a1 = Ambulance('GAX12569')
    lat, lon = gps_coordinates()
    a1.setFuelAmount(gas_tank())
    a1.setTirePressure(tyre_pressure_alarm())

    dev1 = Smoke_detector()
    dev1.setStatus(smoke_detector())


    p1.getInfo()
    print()
    d1.getInfo()
    print()
    a1.getInfo()
    print()
    dev1.getInfo()
