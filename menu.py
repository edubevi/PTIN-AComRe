#!/usr/bin/env python

from tkinter import *
import time, docker, subprocess, sys, json

# List of allowed devices with their type id.
devices = {"doctor":1, "patient":2, "ambulance":3,"smoke":4,"weather":5,"air":6, "nurse":7, "stretcher":8}
# stores the number of devices by type.
num_devices = {"doctor":0, "patient":0, "ambulance":0,"smoke":0,"weather":0,"air":0, "nurse":0, "stretcher":0}


def runcontainers():
    def boton_ok():
        dada1 = text_info2.get()
        dada2 = int(text2.get())
        if dada1 in devices:
            create_container(client, dada1, dada2)


    def create_container(client, type, num):
        count = 0
        # Create window for print containers creates
        finestra = Toplevel()
        finestra.title('Creating Container/s')
        finestra.geometry("450x205+440+300")
        # Add buttom close window
        Button(finestra, text='Close', command=finestra.destroy).place(x=200, y=165)

        # Add text for print
        t = Text(finestra, height=10)

        # While create containers and write on text
        while count != num:
            c_name = type + "_%d" % (num_devices[type])
            c_type = "-t " + str(devices[type])
            container = client.containers.run("peremontpeo/virtualdevices:latest", c_type, detach=True, name=c_name,
                                              auto_remove=True)
            text_ = " + Container with short_id=" + container.short_id + " has been created.\n"

            t.insert(INSERT, text_)
            t.pack()

            print (text_)

            num_devices[type] += 1
            count += 1

    # Create window menu create containers
    dialeg1 = Toplevel(window)
    dialeg1.title("Run Container/s")
    dialeg1.geometry("270x180+530+300")

    # Add label
    runcont = StringVar()
    runcont.set("Allowed device type:")
    Label(dialeg1, textvariable=runcont).place(x=10, y=10)

    text_info2 = StringVar()

    # Introduce radiobuttoms for select type devices
    Radiobutton(dialeg1, text="Patient", variable=text_info2, value='patient').place(x=10, y=30)
    Radiobutton(dialeg1, text="Doctor", variable=text_info2, value='doctor').place(x=10, y=50)
    Radiobutton(dialeg1, text="Ambulance", variable=text_info2, value='ambulance').place(x=90, y=30)
    Radiobutton(dialeg1, text="Smoke", variable=text_info2, value='smoke').place(x=90, y=50)
    Radiobutton(dialeg1, text="Weather", variable=text_info2, value='weather').place(x=190, y=30)
    Radiobutton(dialeg1, text="Air", variable=text_info2, value='air').place(x=190, y=50)
    Radiobutton(dialeg1, text="Nurse", variable=text_info2, value='nurse').place(x=50, y=70)
    Radiobutton(dialeg1, text="Stretcher", variable=text_info2, value='stretcher').place(x=140, y=70)

    # Add label
    runcont2 = StringVar()
    runcont2.set("Number of replicas:")
    Label(dialeg1, textvariable=runcont2).place(x=10, y=100)

    # Add text for introduce numbers
    text2 = StringVar()
    Entry(dialeg1, textvariable=text2, width=32).place(x=10, y=120)

    # Add buttoms for create this containers or close window
    Button(dialeg1, text='Create', command=boton_ok).place(x=65, y=150)
    Button(dialeg1, text='Close', command=dialeg1.destroy).place(x=155, y=150)


def stop_all():

    #Create window for print stopped all containers
    finestra = Toplevel()
    finestra.title('All container/s stopped')
    finestra.geometry("450x205+440+300")
    Button(finestra, text='Close', command=finestra.destroy).place(x=200, y=165)

    # Add text for print
    t = Text(finestra, height=10)
    text_ = ''

    # Containers list
    container_list = client.containers.list()
    if len(container_list) == 0:
        text_ = "There are no containers to stop."
        t.insert(INSERT, text_)
        t.pack()
        print(text_)
    else:
        print("+ Stopping container/s....")
        for container in container_list:
            container.stop()
            text_ = " + Container with short_id=" + container.short_id + " has been stopped.\n"
            t.insert(INSERT, text_)
            t.pack()
            print(text_)
        for key in num_devices.keys(): num_devices[key] = 0  # updates the number of all devices to 0

def stopped_containers():

    def boton_stop():
        dada1 = text_info3.get()
        num = int(text2.get())
        if dada1 in devices:
            stop_containers(client, dada1, num)

    def stop_containers(client, type, num):

        # Create window for print containers creates
        finestra = Toplevel()
        finestra.title('Stopping container/s')
        finestra.geometry("450x205+440+300")
        # Add buttom close window
        Button(finestra, text='Close', command=finestra.destroy).place(x=200, y=165)

        # Add text for print
        t = Text(finestra, height=10)

        # container_list = client.containers.list(filters={'name':'doctor_*'})
        # llista amb el short_id dels contenidors que executa el host.
        container_list = [container.short_id for container in client.containers.list(filters={'name': type + "*"})]
        if len(container_list) == 0 or num == 0:
            text_ = "There are no containers to stop.\n"
            t.insert(INSERT, text_)
            t.pack()
            print(text_)
        elif len(container_list) <= num:
            # stop all running containers
            print("+ Stopping container/s....")
            for item in container_list:
                container = client.containers.get(item)
                container.stop()
                text_ = " + Container with short_id=" + item + " has been stopped.\n"
                t.insert(INSERT, text_)
                t.pack()
                print(text_)
            num_devices[type] = 0  # updates the number of devices
        elif len(container_list) > num:
            # stop the latest num of containers.
            print("+ Stopping container/s....")
            stopped_container = 0
            while stopped_container != num:
                container = client.containers.get(container_list[0])
                container.stop()
                text_ = " + Container with short_id=" + container_list[0] + " has been stopped.\n"
                t.insert(INSERT, text_)
                t.pack()
                print(text_)
                container_list.pop(0)
                num_devices[type] -= 1
                stopped_container += 1

    # Create window menu create containers
    dialeg2 = Toplevel(window)
    dialeg2.title("Stop container/s")
    dialeg2.geometry("280x180+530+300")

    # Add label
    runcont = StringVar()
    runcont.set("Allowed device type:")
    Label(dialeg2, textvariable=runcont).place(x=10, y=10)

    text_info3 = StringVar()

    # Introduce radiobuttoms for select type devices
    Radiobutton(dialeg2, text="Patient", variable=text_info3, value='patient').place(x=10, y=30)
    Radiobutton(dialeg2, text="Doctor", variable=text_info3, value='doctor').place(x=10, y=50)
    Radiobutton(dialeg2, text="Ambulance", variable=text_info3, value='ambulance').place(x=90, y=30)
    Radiobutton(dialeg2, text="Smoke", variable=text_info3, value='smoke').place(x=90, y=50)
    Radiobutton(dialeg2, text="Weather", variable=text_info3, value='weather').place(x=190, y=30)
    Radiobutton(dialeg2, text="Air", variable=text_info3, value='air').place(x=190, y=50)
    Radiobutton(dialeg2, text="Nurse", variable=text_info3, value='nurse').place(x=50, y=70)
    Radiobutton(dialeg2, text="Stretcher", variable=text_info3, value='stretcher').place(x=140, y=70)

    # Add label
    runcont2 = StringVar()
    runcont2.set("Number of containers to stop:")
    Label(dialeg2, textvariable=runcont2).place(x=10, y=100)

    # Add text for introduce numbers
    text2 = StringVar()
    Entry(dialeg2, textvariable=text2, width=32).place(x=10, y=120)

    # Add buttoms for create this containers or close window
    Button(dialeg2, text='Stop', command=boton_stop).place(x=65, y=150)
    Button(dialeg2, text='Close', command=dialeg2.destroy).place(x=155, y=150)


def list_running_containers():
    # Create window for print stopped all containers
    finestra = Toplevel()
    finestra.title("List of running container/s")
    finestra.geometry("350x205+490+300")
    Button(finestra, text='Close', command=finestra.destroy).place(x=150, y=165)

    # Add text for print
    t = Text(finestra, height=10)
    text_ = ''

    print("List of running containers")
    container_list = client.containers.list()
    if len(container_list) == 0:
        text_ = "There are no running containers."
        t.insert(INSERT, text_)
        t.pack()
        print(text_)
    else:
        text_ = "SHORT_ID\t\tTYPE\t\tNAME\n"
        t.insert(INSERT, text_)
        t.pack()
        print(text_)
        for container in container_list:
            text_ = container.short_id + '\t'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
            if "doctor" in container.name:
                text_ = "\tdoctor" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "patient" in container.name:
                text_ = "\tpatient" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "ambulance" in container.name:
                text_ = "\tambulance" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "smoke" in container.name:
                text_ = "\tsmoke" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "weather" in container.name:
                text_ = "\tweather" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "air" in container.name:
                text_ = "\tairq" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "air" in container.name:
                text_ = "\tair" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "nurse" in container.name:
                text_ = "\tnurse" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            elif "stretcher" in container.name:
                text_ = "\tstretcher" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            else:
                text_ = "\t-" + '\t\t'
                t.insert(INSERT, text_)
                t.pack()
                print(text_, end='\t')
            text_ = container.name + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_)


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
    air_list = client.containers.list(filters={'name': "air_*"})
    if len(air_list) != 0: num_devices["air"] = len(air_list)
    nur_list = client.containers.list(filters={'name': "nurse_*"})
    if len(nur_list) != 0: num_devices["nurse"] = len(nur_list)
    stre_list = client.containers.list(filters={'name': "stretcher_*"})
    if len(stre_list) != 0: num_devices["stretcher"] = len(stre_list)


def show_stats():
    subprocess.call(
        ['docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.Container}}" --no-stream'],
        shell=True)


def show_types():
    # Create window for print stopped all containers
    finestra = Toplevel()
    finestra.title("List of running container/s")
    finestra.geometry("350x205+490+300")
    Button(finestra, text='Close', command=finestra.destroy).place(x=150, y=165)

    # Add text for print
    t = Text(finestra, height=10)
    text_ = ''

    print("Devices per type")
    container_list = client.containers.list()
    if len(container_list) == 0:
        text_ = "There are no running containers."
        t.insert(INSERT, text_)
        t.pack()
        print(text_)
    else:
        if num_devices["doctor"] != 0:
            text_ = 'Doctors:' + str(num_devices["doctor"]) + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
        if num_devices["patient"] != 0:
            text_ = 'Patients:' + str(num_devices["patient"]) + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
        if num_devices["ambulance"] != 0:
            text_ = 'Ambulances:' + str(num_devices["ambulance"]) + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
        if num_devices["smoke"] != 0:
            text_ = 'Smoke:' + str(num_devices["smoke"]) + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
        if num_devices["weather"] != 0:
            text_ = 'Weather:' + str(num_devices["weather"]) + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
        if num_devices["air"] != 0:
            text_ = 'Air quality:' + str(num_devices["air"]) + '\t'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
        if num_devices["nurse"] != 0:
            text_ = 'Nurse:' + str(num_devices["nurse"]) + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')
        if num_devices["stretcher"] != 0:
            text_ = 'Stretcher:' + str(num_devices["stretcher"]) + '\n'
            t.insert(INSERT, text_)
            t.pack()
            print(text_, end='\t')

# def button_push():
#     print("------------------------------------")
#     print("Select a patient")
#     print("------------------------------------")
#     container_list = client.containers.list()
#     i = 0
#     patient_list = list()
#     if num_devices["patient"] == 0:
#         print("There are no running containers.")
#     else:
#         print("NUM\tSHORT_ID\t\tNAME")
#         for container in container_list:
#             if "patient" in container.name:
#                 print(i, end='\t')
#                 print(container.short_id, end='\t\t')
#                 print(container.name)
#                 patient_list.append(container)
#                 i += 1
#
#         print("")
#         try:
#             op = int(input("Please select a container: "))
#             if op < 0 or op > i + 1:
#                 raise ValueError
#         except (ValueError, TypeError):
#             print("ERROR: Invalid option.")
#             time.sleep(1)
#
#         selected = patient_list[op]
#         print(selected)
#         try:
#             get_device_id(selected)
#             selected.kill("SIGUSR1")
#             print("Signal enviat")
#         except docker.errors.APIError:
#             pass
#

# def get_device_id(k):
#     # Decode bytes to Unicode
#     data = k.logs().decode('utf8')
#     data = data.splitlines()[0]
#     return data


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
    air_list = client.containers.list(filters={'name': "air_*"})
    if len(air_list) != 0: num_devices["air"] = len(air_list)
    nur_list = client.containers.list(filters={'name': "nurse_*"})
    if len(nur_list) != 0: num_devices["nurse"] = len(nur_list)
    stre_list = client.containers.list(filters={'name': "stretcher_*"})
    if len(stre_list) != 0: num_devices["stretcher"] = len(stre_list)


if __name__ == '__main__':
    client = docker.from_env()
    init_num_devices(client)

    window = Tk()
    window.config(bg="grey")
    window.geometry("225x275+550+250")
    window.title("MENU")

    miTitulo = StringVar()
    miTitulo.set("ORCHESTER TOOL")
    etiquetaTitulo = Label(window, textvariable=miTitulo).place(x=53, y=5)

    boton1 = Button(window, text="Run container/s", command=runcontainers, height=1, width=22).place(x=10, y=30)

    boton2 = Button(window, text="Show running containers", command=list_running_containers, height=1, width=22).place(x=10, y=60)

    boton3 = Button(window, text="Show devices per type", command=show_types, height=1, width=22).place(x=10, y=90)

    # boton4 = Button(window, text="Show containers stats", command=show_stats, height=1, width=22).place(x=10, y=120)

    boton5 = Button(window, text="Stop container/s", command=stopped_containers, height=1, width=22).place(x=10, y=150)

    boton6 = Button(window, text="Stop all running containers", command=stop_all, height=1, width=22).place(x=10, y=180)

    # boton7 = Button(window, text="Push emergency button", command=button_push, height=1, width=22).place(x=10, y=210)

    boton8 = Button(window, text="Exit", command=window.destroy, height=1, width=22).place(x=10, y=240)

    window.mainloop()
