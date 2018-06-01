#!/usr/bin/env python
import os, sys,datetime 
import docker

volumes =['/usr/local/volumes']

def emergency_report(nom_pacient,edifici,latitud,longitud,temperatura,ritme_cardiac,pessio_sang1,pressio_sang2,id_pacient):
	# funcio que genera un informe, per un pacient que ha sofert una emergencia.

	data =  datetime.datetime.now().strftime("%y/%m/%d-%H:%M")
	hora= datetime.datetime.now().strftime("%H:%M")
	#string = str (nom_informe)
	#print(nom_informe)

	nom_informe=nom_pacient				#nom del informe que es volgui donar al fitxer de sortida
	f=open('%s.txt' % nom_informe, 'w')		# creació del informe buit de nom nom_informe
	f.write("INFORME PACIENT: cas d'emergència \n")
	f.write("Data emergència: " + repr(data) + " a les " + repr(hora) + "\n") 
	f.write("\n")

	# COnjunt de paràmetres del pacient
	f.write("Paràmetres pacient + \n")
	f.write("Nom pacient : " + repr(nom_pacient) + "\n")
	f.write("Edifici: " + repr(edifici) + "\n")
	f.write("Latitud: " + repr(latitud) + "\n" )
	f.write("Longitud: " + repr(longitud) + "\n" )

	if temperatura < 36 or temperatura > 39:	# directives del valor anomal de la temperatura
		f.write("[ANÒMAL] Temperatura corporal: " + repr(temperatura) + " ºC" + "\n" )
	else:
		f.write("Temperatura corporal: " + repr(temperatura) + " ºC" + "\n" )

	if ritme_cardiac < 60 or ritme_cardiac > 130:	# directives del ritme cardiac
		f.write("[ANÒMAL] Ritme Cardíac: " + repr(ritme_cardiac) + " bpm" + "\n" )
	else:
		f.write("Ritme Cardíac: " + repr(ritme_cardiac) + " bpm" + "\n" ) 
	
	if pressio_sang1 < 80 or pressio_sang1 > 130 or pressio_sang2 < 80 or pressio_sang2 > 130:	# directives de la pression sanguinia
		f.write("[ANÒMAL]Pressió sanguínia: " + repr(pressio_sang1) + ", "+  repr(pressio_sang2) + " mmHg"+ "\n" )
	else:
		f.write("Pressió sanguínia: " + repr(pressio_sang1) + ", "+  repr(pressio_sang2) + " mmHg"+ "\n" )
	
	f.write("Id pacient virtual: " + repr(id_pacient) + "\n" )
	f.write("\n")
	f.close()		
		

if __name__ == '__main__':

	client = docker.from_env()
	
	# creació del volume en un directori concret.
	#volume = client.volumes.create(name='volume_reports',driver='local',driver_opts={'device':'/usr/local/'})
	nom_pacient="Adrià Pedraza"
	edifici='A'
	latitud=41.23
	longitud=41.07
	temperatura=36.6
	ritme_cardiac=90
	pressio_sang1=80
	pressio_Sang2=150
	id_pacient=21121212
	emergency_report(nom_pacient,edifici,latitud,longitud,temperatura,ritme_cardiac,pressio_sang1,pressio_sang2,id_pacient)
