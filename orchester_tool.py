#!/usr/bin/env python

import time, docker, subprocess, sys, json

#List of allowed devices with their type id.
devices = {"doctor":1, "patient":2, "ambulance":3,"smoke":4,"weather":5}
#stores the number of devices by type.
num_devices = {"doctor":0, "patient":0, "ambulance":0,"smoke":0,"weather":0}


def usage():
    p1 = subprocess.Popen(['dpkg','--get-selections'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep','docker-ce[[:space:]]*install$'],stdin=p1.stdout,stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['wc','-l'],stdin=p2.stdout, stdout=subprocess.PIPE)
    output = p3.communicate()[0].decode('utf-8').split()
    if output[0] != '1':
        print("Docker is not installed. Please install it")
        sys.exit()


def menu():
    subprocess.run(["clear"], shell=True)
    print("    ORCHESTER TOOL   ")
    print("------------------------------------")
    print("Option Menu")
    print("------------------------------------")
    print("[1] Run container/s.")
    print("[2] Stop container/s.")
    print("[3] Show running containers.")
    print("[4] Stop all running containers.")
    print("[5] Delete all stopped containers.")
    print("[6] Show container stats.")
    print("")
    print("[7] Exit.")
    print("------------------------------------")


def create_container(client, type, num):
    count = 0
    while count != num:
        c_name = type + "_%d" % (num_devices[type])
        c_type = "-t "+str(devices[type])
        container = client.containers.run("peremontpeo/virtualdevices:latest",c_type, detach=True, name=c_name, auto_remove=True)
        print("+ Container with short_id=" + container.short_id + " has been created.")
        num_devices[type]+=1
        count+=1


def stop_all(client):
    container_list = client.containers.list()
    if len(container_list) == 0: print("There are no containers to stop.")
    else:
        print("+ Stopping container/s....")
        for container in container_list:
            container.stop()
            print("+ Container with short_id=" + container.short_id + " has been stopped.")
        for key in num_devices.keys(): num_devices[key]=0 #updates the number of all devices to 0


def stop_containers(client, num, type):
    # container_list = client.containers.list(filters={'name':'doctor_*'})
    # llista amb el short_id dels contenidors que executa el host.
    container_list = [container.short_id for container in client.containers.list(filters={'name':type+"*"})]
    if len(container_list) == 0 or num == 0:print("There are no containers to stop.")
    elif len(container_list) <= num:
        # stop all running containers
        print("+ Stopping container/s....")
        for item in container_list:
            container = client.containers.get(item)
            container.stop()
            print("+ Container with short_id="+item+" has been stopped.")
        num_devices[type]=0 #updates the number of devices
    elif len(container_list) > num:
        # stop the latest num of containers.
        print("+ Stopping container/s....")
        stopped_container = 0
        while stopped_container != num:
            container = client.containers.get(container_list[0])
            container.stop()
            print("+ Container with short_id=" + container_list[0] + " has been stopped.")
            container_list.pop(0)
            num_devices[type] -= 1
            stopped_container += 1


def list_running_containers(client):
    print("------------------------------------")
    print("List of running containers")
    print("------------------------------------")
    container_list = client.containers.list()
    if len(container_list) == 0: print("There are no running containers.")
    else:
        print("SHORT_ID\tTYPE\t\tNAME")
        for container in container_list:
            print(container.short_id, end='\t')
            if "doctor" in container.name: print("doctor",end='\t\t')
            elif "patient" in container.name: print("patient",end='\t\t')
            elif "ambulance" in container.name: print("ambulance",end='\t\t')
            elif "smoke" in container.name: print("smoke",end='\t\t')
            elif "weather" in container.name: print("weather",end='\t\t')
            else: print("-",end='\t\t')
            print(container.name)


def init_num_devices(client):
    doc_list = client.containers.list(filters={'name': "doctor_*"})
    if len(doc_list) != 0: num_devices["doctor"] = len(doc_list)
    pat_list = client.containers.list(filters={'name': "patient_*"})
    if len(pat_list) != 0: num_devices["patient"] = len(pat_list)
    amb_list = client.containers.list(filters={'name': "ambulance_*"})
    if len(amb_list) != 0: num_devices["ambulance"] = len(amb_list)
    smo_list = client.containers.list(filters={'name': "smoke_*"})
    if len(smo_list) != 0: num_devices["smoke"] = len(smo_list)
    wea_list = client.containers.list(filters={'name': "weather_*"})
    if len(wea_list) != 0: num_devices["weather"] = len(wea_list)


def show_stats():
    subprocess.call(['docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.Container}}" --no-stream'], shell=True)


if __name__ == '__main__':
    # instantiate a client to talk with Docker daemon.
    usage()
    client = docker.from_env()
    #Inicialitza el nombre de dispositius que hi ha en execució per tipus.
    init_num_devices(client)
    op = 0
    while op != 7:
        menu()
        try:
            op = int(input("Please select an option: "))
            if op < 0 or op > 7:
                raise ValueError
        except (ValueError, TypeError):
            print("ERROR: Invalid option.")
            time.sleep(1)
        if op == 1:
            try:
                print("")
                print("Allowed device type:")
                print("------------------------------------")
                print(list(devices.keys()))
                print("------------------------------------")
                type = input("Device type: ")
                if type in devices:
                    num = int(input("Number of replicas: "))
                    if num < 0: raise ValueError
                    subprocess.run(["clear"], shell=True)
                    create_container(client, type, num)
                else: raise ValueError
                print("")
                input("Press ENTER to continue...")
            except(ValueError, TypeError):
                print("ERROR: Invalid Input.")
                time.sleep(1)

        elif op == 2:
            try:
                print("")
                print("Allowed device type:")
                print("------------------------------------")
                print(list(devices.keys()))
                print("------------------------------------")
                type = input("Device type: ")
                if type in devices:
                    num = int(input("Number of containers to stop: "))
                    if num < 0: raise ValueError
                    subprocess.run(["clear"], shell=True)
                    stop_containers(client, num, type)
                    print("")
                    input("Press ENTER to continue...")
                else: raise ValueError
            except (ValueError, TypeError):
                print("ERROR: Invalid Input.")
                time.sleep(1)
        elif op == 3:
            subprocess.run(["clear"], shell=True)
            list_running_containers(client)
            print("")
            input("Press ENTER to continue...")
        elif op == 4:
            subprocess.run(["clear"], shell=True)
            stop_all(client)
            print("")
            input("Press ENTER to continue...")
        elif op == 5:
            subprocess.run(["clear"], shell=True)
            client.containers.prune()
            print("All stopped containers removed.")
            print("")
            input("Press ENTER to continue...")
        elif op == 6:
            subprocess.run(["clear"], shell=True)
            show_stats()
            print("")
            input("Press ENTER to continue...")

        elif op == 7:
            pass
