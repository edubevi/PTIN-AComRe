import random
import numpy
from libs.real_weather import *
from libs.helper import *
from pathlib import Path

# Patient sensors

def body_thermometer(prev_temp):
    max_temp = 43.0
    min_temp = 34.0
    options = [1,2,3] # Opcions de variacio temperatura. 1-> incrementa, 2-> disminueix, 3-> es queda igual.
    amounts = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0] # Quantiats amb les que pot variar la temperatura

    # Agafem l'opcio de variacio de la temperatura en funcio d'un %. (incrementa->40%, disminueix->40%, igual->20%)
    op = numpy.random.choice(options, p=[0.4,0.4,0.2])
    # Agafem la quantitat que variara la temperatura en funcio d'un %.
    amo = numpy.random.choice(amounts, p=[0.35,0.35,0.15,0.05,0.02,0.02,0.02,0.02,0.01,0.01])

    if op == 1:  #Augmenta temperatura.
        new_temp = amo + prev_temp
        # Comprovem si el nou valor esta fora del rang del sensor.
        if new_temp > max_temp: new_temp = max_temp
    elif op == 2: #Disminueix temperatura.
        new_temp = prev_temp - amo
        # Comprovem si el nou valor esta fora del rang del sensor.
        if new_temp < min_temp: new_temp = min_temp
    elif op == 3: new_temp = prev_temp #La temperautra es mante.

    return round(new_temp,2)

def heart_rate_monitor(prev_hr):
    max_hr = 190
    min_hr = 40
    options = [1,2,3]  # Opcions de variacio ritme cardiac. 1-> incrementa, 2-> disminueix, 3-> es queda igual.
    amount = [2,4,6,8,10,15,20,25] # Possibles quantiats en les que pot variar el ritme cardiac.

    # Agafem l'opcio de variacio del ritme cardiac en funcio d'un %. (incrementa->25%, disminueix->25%, es mante->50%)
    op = numpy.random.choice(options, p=[0.25,0.25,0.5])
    # Agafem la quantitat que variara el ritme cardiac en funcio d'un %.
    amo = numpy.random.choice(amount, p=[0.2,0.2,0.15,0.15,0.1,0.1,0.05,0.05])

    if op == 1:  # Augmenta_ritme cardiac.
        new_hrate = amo + prev_hr
        # Comprovem si el nou valor esta fora del rang del sensor.
        if new_hrate > max_hr: new_temp = max_hr
    elif op == 2: #Disminueix ritme cardiac.
        new_hrate = prev_hr - amo
        # Comprovem si el nou valor esta fora del rang del sensor.
        if new_hrate < min_hr: new_hrate = min_hr
    elif op == 3: # El ritme cardiac es mante.
        new_hrate = prev_hr

    return new_hrate


def blood_pressure_monitor(prev_sys, prev_dia):
    max_sys = 180
    min_sys = 70
    max_dia = 100
    min_dia = 40

    options = [1, 2, 3]  # Opcions de variacio presio. 1-> incrementa, 2-> disminueix, 3-> es queda igual.
    amount_sys = [2, 4, 6, 8, 10, 20, 30, 40] # Possibles quantiats en les que pot variar sys.
    amount_dia = [2, 4, 6, 8, 10, 15, 20, 25] # Possibles quantiats en les que pot variar dia.

    op = numpy.random.choice(options, p=[0.25, 0.25, 0.5])
    amo_sys = numpy.random.choice(amount_sys, p=[0.25, 0.25, 0.15, 0.15, 0.1, 0.06, 0.02, 0.02])
    amo_dia = numpy.random.choice(amount_dia, p=[0.25, 0.25, 0.15, 0.15, 0.1, 0.05, 0.03, 0.02])

    if op == 1: # Augment de la presio arterial
        new_sys = prev_sys + amo_sys
        new_dia = prev_dia + amo_dia
        # Comprovem si el nou valor esta fora del rang del sensor.
        if new_sys > max_sys: new_sys = max_sys
        if new_dia > max_dia: new_dia = max_dia
    elif op == 2: # Disminueix la presio arterial
        new_sys = prev_sys - amo_sys
        new_dia = prev_dia - amo_dia
        # Comprovem si el nou valor esta fora del rang del sensor.
        if new_sys < min_sys: new_sys = min_sys
        if new_dia < min_dia: new_dia = min_dia
    elif op == 3: # No varia la presio arterial
        new_sys = prev_sys
        new_dia = prev_dia

    return new_sys, new_dia


# Location sensors
def gps(route, next_jump = 0, distance=0):
    folder = Path('libs/routes/')
    filename = 'route_'+str(route)
    file= folder / filename
    path = 'routes/route_'+str(route)
    n_coordinates = file_lines(file) - 5
    coordinates = open(file)

    line_offset = []
    offset = 0
    for line in coordinates:
        line_offset.append(offset)
        offset += len(line)
    coordinates.seek(0)

    #coordinates.seek(line_offset[n])

    try:
        for i in range(6 + next_jump):
            next(coordinates)
        line = next(coordinates)
        column = line.split()
        latitude = float(column[1])
        longitude = float(column[2])
        distance += float(column[4])
    except StopIteration:
        pass
    next_jump += 1
    return latitude, longitude, next_jump, distance


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


def ips_coordinates_range(x, y):
    internal_lat = internal_long = 0.0
    if 41.221814 < x < 41.220892 and 1.730924 < y < 1.729499:
        internal_lat = random.uniform(41.221814, 41.220892)
        internal_long = random.uniform(1.730924, 1.729499)
    elif 41.223351 < x < 41.223314 and 1.736664 < y < 1.734798:
        internal_lat = random.uniform(41.223351, 41.223314)
        internal_long = random.uniform(1.736664, 1.734798)
    elif 41.223760 < x < 41.222952 and 1.734363 < y < 1.732982:
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
    return numpy.random.choice(numpy.arange(0, 2), p=[0.98, 0.02])

# physical devices sensors

def smoke_detector():
    return numpy.random.choice(numpy.arange(0, 2), p=[0.99, 0.01])


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


# air quality


