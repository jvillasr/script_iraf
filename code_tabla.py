#! /usr/bin/env python

archivo=open("Hdelta-splot.log","r")
salida=open("salida.dat","w")  

linea=archivo.readlines()

while linea not EOF:                  #not End Of File, es decir que siga hasta que se acaben las l´ineas que lee en el archivo "Hdelta-splot.log" 
	if linea != '':
		linea=linea.split('') # ('') es espacio vac`io
		nombre=linea[3]       #la posicion 0 en la primera linea es April, la posicion 1 es el dia, la posicion 2 es la hora y la posicion 3 es el nombre de la estrella
			for i in range(4)     # range(4)=(0,1,2,3)
				dato=archivo.readlines().split('')
				error_dato=   #falta extraer el error aca
				if i=0:
					lambda1.write(dato)   #y escribir error_dato (falta revisar)
				elif i=1:
					lambda2.write(dato)   #y escribir error_dato (falta revisar)
				elif i=2:
					lambda3.write(dato)   #y escribir error_dato (falta revisar)
				elif i=3:
					lambda4.write(dato)   #y escribir error_dato (falta revisar)
	linea=archivo.readlines()

archivo.close()
lambda1.close()
lambda2.close()
lambda3.close()
lambda4.close()
