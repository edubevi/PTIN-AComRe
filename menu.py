from tkinter import *
import time, docker, subprocess, sys, json

devices = {"doctor": 1, "patient": 2, "ambulance": 3, "smoke": 4, "weather": 5}
num_devices = {"doctor": 0, "patient": 0, "ambulance": 0, "smoke": 0, "weather": 0}


def create_container(client, type, num):
    count = 0
    while count != num:
        c_name = type + "_%d" % (num_devices[type])
        c_type = "-t " + str(devices[type])
        container = client.containers.run("peremontpeo/virtualdevices:latest", c_type, detach=True, name=c_name,
                                          auto_remove=True)
        print("+ Container with short_id=" + container.short_id + " has been created.")
        num_devices[type] += 1
        count += 1


def runcontainers():

    def boton_sure():
        dialeg3 = Toplevel(dialeg1)
        dialeg3.title("SURE ?")
        dialeg3.geometry("140x50")

        boton = Button(dialeg3, text='Yes', command=boton_ok).place(x=15, y=10)
        boton = Button(dialeg3, text='No', command=dialeg3.destroy).place(x=80, y=10)


    dialeg1 = Toplevel(window)
    dialeg1.title("Run Container/s")
    dialeg1.geometry("270x165")

    text_info = list(devices.keys())

    runcont = StringVar()
    runcont.set("Allowed device type:")
    etiquetaruncont = Label(dialeg1, textvariable=runcont).place(x=10, y=20)

    runcont1 = StringVar()
    runcont1.set(text_info)
    etiquetaruncont1 = Label(dialeg1, textvariable=runcont1).place(x=10, y=40)

    text = StringVar()
    text_device = Entry(dialeg1, textvariable=text).place(x=10, y=60)

    runcont2 = StringVar()
    runcont2.set("Number of replicas")
    etiquetaruncont2 = Label(dialeg1, textvariable=runcont2).place(x=10, y=80)

    text2 = StringVar()
    text_num = Entry(dialeg1, textvariable=text2).place(x=10, y=100)

    boton = Button(dialeg1, text='Tanca', command=dialeg1.destroy).place(x=100, y=130)

    botonok = Button(dialeg1, text='Create', command=boton_sure).place(x=10, y=130)

    def boton_ok():
        dada1 = text.get()
        dada2 = int(text2.get())
        if dada1 in devices:
            create_container(client, dada1, dada2)

def stopcontainers():
    dialeg2 = Toplevel()

    stopcont = StringVar()
    stopcont.set("Allowed device type:")
    etiquetastopcont = Label(dialeg2,
                             textvariable=stopcont)
    etiquetastopcont.grid(row=1, column=1)

    text = Text(dialeg2)
    text.config(bg="yellow", fg="black", width=10,
                height=1)

    text.grid(row=2, column=1)

    boton = Button(dialeg2, text='Tanca', command=dialeg2.destroy)

    boton.grid(row=3, column=1)


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

    window = Tk()  # Tk() Es la ventana principal
    # La variable ventana es del tipo Tk()

    window.config(bg="grey")
    window.geometry("205x220")
    window.title("MENU")

    miTitulo = StringVar()
    miTitulo.set("ORCHESTER TOOL")
    etiquetaTitulo = Label(window, textvariable=miTitulo)
    etiquetaTitulo.grid(row=2, column=1)

    boton1 = Button(window, text="Run container/s", command=runcontainers)
    boton1.grid(row=3, column=1)

    boton2 = Button(window, text="Stop container/s", command=stopcontainers)
    boton2.grid(row=4, column=1)

    boton3 = Button(window, text="Show running containers", command=runcontainers)
    boton3.grid(row=5, column=1)

    boton4 = Button(window, text="Stop all running containers", command=runcontainers)
    boton4.grid(row=6, column=1)

    boton5 = Button(window, text="Delete all stopped containers", command=runcontainers)
    boton5.grid(row=7, column=1)

    boton6 = Button(window, text="Show containers stats", command=runcontainers)
    boton6.grid(row=8, column=1)

    boton7 = Button(window, text="Exit", command=window.destroy)
    boton7.grid(row=9, column=1)

    window.mainloop()
