import random
import numpy
from libs.real_weather import *

# Patient sensors

def body_thermometer(prev_temp=36.0):
    max_temp = 43.0
    min_temp = 34.0
    temp = ((random.random() * (max_temp - min_temp)) + min_temp)
    diff = abs(prev_temp - temp)
    if diff > 1:
        diff = random.random() * 1
    if temp > prev_temp:
        final_temp = prev_temp + diff
    else:
        final_temp = prev_temp - diff
    return round(final_temp, 1)


def heart_rate_monitor(prev_hr=50):
    max_hr = 190
    min_hr = 40
    hr = random.uniform(max_hr, min_hr)
    diff = abs(prev_hr - hr)
    if diff > 10:
        diff = random.random() * 10
    if hr > prev_hr:
        final_hr = prev_hr + diff
    else:
        final_hr = prev_hr - diff
    return int(round(final_hr, 0))


def blood_pressure_monitor(prev_sys=100, prev_dia=70):
    max_sys_pr = 160
    min_sys_pr = 80
    max_dia_pr = 100
    min_dia_pr = 50
    sys_pr = random.uniform(max_sys_pr, min_sys_pr)
    dia_pr = random.uniform(max_dia_pr, min_dia_pr)
    sys_diff = abs(prev_sys - sys_pr)
    dia_diff = abs(prev_dia - dia_pr)
    if sys_diff > 10:
        sys_diff = random.random() * 10
    if dia_diff > 10:
        dia_diff = random.random() * 10

    if sys_pr > prev_sys:
        final_sys_pr = prev_sys + sys_diff
    else:
        final_sys_pr = prev_sys - sys_diff

    if dia_pr > prev_sys:
        final_dia_pr = prev_dia + dia_diff
    else:
        final_dia_pr = prev_dia - dia_diff

    final_pr = int(round(final_sys_pr, 0)), int(round(final_dia_pr, 0))
    return final_pr

# Location sensors

def gps_coordinates():
    #latitude range
    min_lat = 41.2200556
    max_lat = 41.2246389

    #longitude range
    min_lon = 1.728472
    max_lon = 1.73716

    return random.uniform(min_lat, max_lat), random.uniform(min_lon,max_lon)

def ips_coordinates(building):
    internal_lat = internal_long = 0.0
    if building == 'A':
        internal_lat = random.uniform(41.221814, 41.220892)
        internal_long = random.uniform(1.730924, 1.729499)
    elif building == 'B':
        internal_lat = random.uniform(41.223351, 41.223314)
        internal_long = random.uniform(1.736664, 1.734798)
    elif building == 'Neapolis':
        internal_lat = random.uniform(41.223760, 41.222952)
        internal_long = random.uniform(1.734363, 1.732982)
    return internal_lat, internal_long



# Doc sensors

def doc_availability():
    return random.randrange(2)

# vehicle sensors


def gas_tank(prev_level=100,distance=0):
    # liters consumption per 100km (100000 meters)
    consumption = 7.4

    if distance is 0:
        return prev_level
    else:
        distance = distance / 100000
        consumed = distance * consumption
        remaining_level = prev_level - consumed
        #refuel
        if prev_level < consumed:
            prev_level = 100
            remaining_level = prev_level - consumed

        return remaining_level


def amb_availability():
    return random.randrange(2)

def tyre_pressure_alarm():
    return numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05])

# physical devices sensors

def smoke_detector():
    return numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05])


# weather

def thermometer():
    current = get_current_data()
    return current.temperature


def hygrometer():
    current = get_current_data()
    return current.humidity


def barometer():
    current = get_current_data()
    return current.pressure

