#!/usr/bin/python
import random
import numpy


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

# Patient sensors

def heart_rate():
    return random.uniform(40.160)

def body_temp():
    return random.uniform(35.0, 42.0)

def blood_pressure():
    return random.uniform(60.0, 140.0)

def doc_proximity():
    return random.uniform(1, 20)

# Doc sensors

def doc_availability():
    return random.randrange(2)

# Ambulance sensors

def fuel_amount():
    return random.randrange(100)

def amb_availability():
    return random.randrange(2)

def tire_pressure():
    return random.randrange(3.0)

# physical devices sensors

def smoke_detector():
    return numpy.random.choice(numpy.arrange(0, 2), p=[0.95, 0.05])



