#!/usr/bin/env python

import time, docker, random, subprocess

#List of allowed devices.
devices = ["patient","doctor","ambulance","smoke","weather","air_quality"]

def usage():
    #TO IMPLEMENT
    return 0

def menu():
    subprocess.run(["clear"], shell=True)
    print("    ORCHESTER TOOL   ")
    print("------------------------------------")
    print("Option Menu")
    print("------------------------------------")
    print("[1] Run container/s.")
    print("[2] Stop container/s.")
    print("[3] Show running containers.")
    print("[4] Delete all stopped containers.")
    print("")
    print("[5] Exit.")
    print("------------------------------------")

def create_container(client, type, num):
    #TO IMPLEMENT
    #container = client.containers.run("", detach=True)
    return 0

def stop_containers(client, num):
    container_list = [container.short_id for container in client.containers.list()] # llista amb el short_id dels contenidors que executa el host.
    if len(container_list) == 0 or num == 0:
        print("There are no containers to stop.")
    elif len(container_list) <= num:
        # stop all running containers
        for item in container_list:
            container = client.containers.get(item)
            container.stop()
            print("+ Container with short_id="+item+" has been stopped.")

    elif len(container_list) > num:
        # stop a random num of containers.
        stopped_container = 0
        while stopped_container != num:
            index = random.randrange(len(container_list))
            container = client.containers.get(container_list[index])
            container.stop()
            print("+ Container with short_id="+container_list[index]+" has been stopped.")
            container_list.pop(index)
            stopped_container += 1

def list_running_containers(client):
    container_list = client.containers.list()
    if len(container_list) == 0:
        print("There are no running containers.")
    else:
        for container in container_list:
            print(container.short_id)


if __name__ == '__main__':
    # instantiate a client to talk with Docker daemon.
    client = docker.from_env()
    op = 0
    while op != 5:
        menu()
        try:
            op = int(input("Please select an option: "))
            if op < 0:
                raise ValueError
        except (ValueError, TypeError):
            print("ERROR: Invalid option.")
            time.sleep(1)
        if op == 1:
            try:
                print("")
                print("Allowed device type:")
                print("------------------------------------")
                print(devices)
                print("------------------------------------")
                type = input("Device type: ")
                if type in devices:
                    #TO IMPLEMENT
                    pass
                else:
                    raise ValueError
                num = int(input("Number of replicas: "))
                if num < 0:
                    raise ValueError
            except(ValueError, TypeError):
                print("ERROR: Invalid Input.")
                time.sleep(1)

        elif op == 2:
            try:
                n = int(input("Number of containers to stop: "))
                if n < 0:
                    raise ValueError
                time.sleep(1)
                subprocess.run(["clear"], shell=True)
                stop_containers(client, n)
                print("")
                input("Press ENTER to continue...")
            except (ValueError, TypeError):
                print("ERROR: Invalid Input.")
                time.sleep(1)
        elif op == 3:
            subprocess.run(["clear"], shell=True)
            print("------------------------------------")
            print("List of running containers id")
            print("------------------------------------")
            list_running_containers(client)
            print("")
            input("Press ENTER to continue...")
        elif op == 4:
            subprocess.run(["clear"], shell=True)
            client.containers.prune()
            print("All stopped containers removed.")
            print("")
            input("Press ENTER to continue...")
        elif op == 5:
            pass