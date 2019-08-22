# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:16:04 2019

@author: aniba
"""

#minuto 9:37
#ejercicio acera de como cambiar el contenido de una lista a diferentes posiciones dentro de ella

b = ['auto','carrera','porsche'] #creando una lista

print(b)

temp = b[0]#creo una variable temporal
b[0] = b[2]#asigno a la posicion 0 el contenido de la posicion 2
b[2] = temp#asigno a la posicion 2 el contenido de la variable temporal antes creada
print(b)

b[0], b[2] = b[2], b[0]#mismo objetivo que las 3 lineas anteriores, pero escrito en una linea donde al la posicion 0 se le asigna lo de la posicion 2 y la 2 se le asigna lo de la 0
#vuelve a ser la lista inicial
print(b)