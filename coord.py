#!/usr/bin/env python

from tkinter import *
import time, docker, subprocess, sys, json, os

devices = {"doctor":1, "patient":2, "ambulance":3,"smoke":4,"weather":5,"air":6, "nurse":7, "stretcher":8}
# stores the number of devices by type.
num_devices = {"doctor":0, "patient":0, "ambulance":0,"smoke":0,"weather":0,"air":0, "nurse":0, "stretcher":0}


def create_coord(client):

	c_type="-t 2"
	c_name="patient_0"
    #c_type="-t 2" 					# type 2 = patient_0
	cpus_number='--cpus=.5'			# % number of % of core used
	# --cpuset-cpus         		# range of cores the container works with
	memoria_ram='-m 100m'			# mem_default=4mb / container, al indicar menys indicarà error el propi docker
	container = client.containers.run("peremontpeo/virtualdevices:latest",c_type,"-i 10","--cpuset-cpus 0,1", cpus_number,memoria_ram, detach=True, name=c_name, auto_remove=True)
		
if __name__ == '__main__':

	client=docker.from_env()
	create_coord(client)
