from tkinter import *
import time, docker, subprocess, sys, json

devices = {"doctor": 1, "patient": 2, "ambulance": 3, "smoke": 4, "weather": 5}
num_devices = {"doctor": 0, "patient": 0, "ambulance": 0, "smoke": 0, "weather": 0}


def runcontainers():
    def boton_ok():
        dada1 = text_info2.get()
        dada2 = int(text2.get())
        if dada1 in devices:
            create_container(client, dada1, dada2)


    def create_container(client, type, num):
        count = 0

        finestra = Toplevel()
        finestra.title('Creating Container/s')
        finestra.geometry("450x205+440+300")
        Button(finestra, text='Close', command=finestra.destroy).place(x=200, y=165)

        t = Text(finestra, height=10)

        while count != num:
            c_name = type + "_%d" % (num_devices[type])
            c_type = "-t " + str(devices[type])
            container = client.containers.run("peremontpeo/virtualdevices:latest", c_type, detach=True, name=c_name,
                                              auto_remove=True)
            text_ = "+ Container with short_id=" + container.short_id + " has been created.\n"

            t.insert(INSERT, text_)
            t.pack()

            print (text_)

            num_devices[type] += 1
            count += 1

    dialeg1 = Toplevel(window)
    dialeg1.title("Run Container/s")
    dialeg1.geometry("270x165+550+300")

    runcont = StringVar()
    runcont.set("Allowed device type:")
    Label(dialeg1, textvariable=runcont).place(x=10, y=10)

    text_info2 = StringVar()

    Radiobutton(dialeg1, text="Patient", variable=text_info2, value='patient').place(x=10, y=30)
    Radiobutton(dialeg1, text="Doctor", variable=text_info2, value='doctor').place(x=10, y=50)
    Radiobutton(dialeg1, text="Ambulance", variable=text_info2, value='ambulance').place(x=90, y=30)
    Radiobutton(dialeg1, text="Smoke", variable=text_info2, value='smoke').place(x=90, y=50)
    Radiobutton(dialeg1, text="Weather", variable=text_info2, value='weather').place(x=180, y=50)

    runcont2 = StringVar()
    runcont2.set("Number of replicas:")
    Label(dialeg1, textvariable=runcont2).place(x=10, y=80)

    text2 = StringVar()
    Entry(dialeg1, textvariable=text2, width=30).place(x=10, y=100)

    Button(dialeg1, text='Create', command=boton_ok).place(x=60, y=130)

    Button(dialeg1, text='Close', command=dialeg1.destroy).place(x=150, y=130)


# def stop_all(client):
#     container_list = client.containers.list()
#     if len(container_list) == 0:
#         print("There are no containers to stop.")
#     else:
#         print("+ Stopping container/s....")
#         for container in container_list:
#             container.stop()
#             print("+ Container with short_id=" + container.short_id + " has been stopped.")
#         for key in num_devices.keys(): num_devices[key] = 0  # updates the number of all devices to 0
#
#
# def stop_containers(client, num, type):
#     # container_list = client.containers.list(filters={'name':'doctor_*'})
#     # llista amb el short_id dels contenidors que executa el host.
#     container_list = [container.short_id for container in client.containers.list(filters={'name': type + "*"})]
#     if len(container_list) == 0 or num == 0:
#         print("There are no containers to stop.")
#     elif len(container_list) <= num:
#         # stop all running containers
#         print("+ Stopping container/s....")
#         for item in container_list:
#             container = client.containers.get(item)
#             container.stop()
#             print("+ Container with short_id=" + item + " has been stopped.")
#         num_devices[type] = 0  # updates the number of devices
#     elif len(container_list) > num:
#         # stop the latest num of containers.
#         print("+ Stopping container/s....")
#         stopped_container = 0
#         while stopped_container != num:
#             container = client.containers.get(container_list[0])
#             container.stop()
#             print("+ Container with short_id=" + container_list[0] + " has been stopped.")
#             container_list.pop(0)
#             num_devices[type] -= 1
#             stopped_container += 1


# def list_running_containers(client):
#     print("------------------------------------")
#     print("List of running containers")
#     print("------------------------------------")
#     container_list = client.containers.list()
#     if len(container_list) == 0:
#         print("There are no running containers.")
#     else:
#         print("SHORT_ID\tTYPE\t\tNAME")
#         for container in container_list:
#             print(container.short_id, end='\t')
#             if "doctor" in container.name:
#                 print("doctor", end='\t\t')
#             elif "patient" in container.name:
#                 print("patient", end='\t\t')
#             elif "ambulance" in container.name:
#                 print("ambulance", end='\t\t')
#             elif "smoke" in container.name:
#                 print("smoke", end='\t\t')
#             elif "weather" in container.name:
#                 print("weather", end='\t\t')
#             elif "air" in container.name:
#                 print("airq", end='\t\t')
#             else:
#                 print("-", end='\t\t')
#             print(container.name)


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
    if len(wea_list) != 0: num_devices["air"] = len(air_list)


# def show_stats():
#     subprocess.call(
#         ['docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.Container}}" --no-stream'],
#         shell=True)


# def show_types(client):
#     print("------------------------------------")
#     print("Devices per type")
#     print("------------------------------------")
#     container_list = client.containers.list()
#     if len(container_list) == 0:
#         print("There are no running containers.")
#     else:
#         if num_devices["doctor"] != 0:
#             print('Doctors:', num_devices["doctor"], end='\t')
#         if num_devices["patient"] != 0:
#             print('Patients:', num_devices["patient"], end='\t')
#         if num_devices["ambulance"] != 0:
#             print('Ambulances:', num_devices["ambulance"], end='\t')
#         if num_devices["smoke"] != 0:
#             print('Smoke:', num_devices["smoke"], end='\t')
#         if num_devices["weather"] != 0:
#             print('Weather:', num_devices["weather"], end='\t')
#         if num_devices["air"] != 0:
#             print('Air quality:', num_devices["air"], end='\t')


# def button_push(client):
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

    # boton2 = Button(window, text="Show running containers", command=list_running_containers, height=1, width=22).place(x=10, y=60)
    #
    # boton3 = Button(window, text="Show containers stats", command=runcontainers, height=1, width=22).place(x=10, y=90)
    #
    # boton4 = Button(window, text="Stop container/s", command=stop_containers, height=1, width=22).place(x=10, y=120)
    #
    # boton5 = Button(window, text="Stop all running containers", command=runcontainers, height=1, width=22).place(x=10, y=150)
    #
    # boton6 = Button(window, text="Delete all stopped containers", command=runcontainers, height=1, width=22).place(x=10, y=180)
    #
    # boton7 = Button(window, text="Show devices pertype", command=runcontainers, height=1, width=22).place(x=10, y=180)
    #
    # boton8 = Button(window, text="Push emergency button", command=runcontainers, height=1, width=22).place(x=10, y=210)

    boton9 = Button(window, text="Exit", command=window.destroy, height=1, width=22).place(x=10, y=240)

    window.mainloop()
