#! /usr/bin/python
#usage: python gps.py 1
import os
from time import *
import time
import linecache
import datetime
import sys

def dd2dms(dd):
    is_positive = dd >= 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    degrees = degrees if is_positive else -degrees
    return (degrees,minutes,seconds)

def get_eta(fname): #in seconds
    line = open(fname).readlines()[:6][-1]
    time = line.split(',')[-1]
    hours,minutes = time.split(':')
    hours=float(hours)
    minutes=float(minutes)
    hours = hours +2
    if hours>0:
        minutes += hours*60
    return minutes*60

def file_lines(fname):
    with open(fname) as f:
                for i, l in enumerate(f):
                        pass
    return i + 1


if __name__ == '__main__':

    if sys.argv[1]=='1':
        routename = 'ruta-1.txt'
    if sys.argv[1]=='2':
        routename = 'ruta-2.txt'
    points = file_lines(routename) - 5
    try:
        fakegps =  open(routename)
        for i in xrange(6): #saltarse primeres 6 linies
            fakegps.next()
        while True:
            line = fakegps.next()
            column = line.split()
            glatitude = dd2dms(float(column[1]))
            glongitude = dd2dms(float(column[2]))

            os.system('clear')
            print()
            print(" Posicio GPS ")
            print("----------------------------------------")
            print("latitud  %f " % glatitude)
            print("longitud %f " % glongitude)
            print("diahora      " + time.strftime("%Y/%m/%d") + time.strftime("%H:%M:%S"))
            print("----------------------------------------")

            time.sleep(2) #temps updates

    except (StopIteration):
         pass
    except (KeyboardInterrupt, SystemExit): #ctrl+c
       print("Done.\nExiting.")