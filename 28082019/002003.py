# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:32:18 2019

@author: aniba
"""

#Especial de arreglos en Numpy 1D
#Diferencias entre listas y arreglos.
#Trabajar con arreglos es mucho mas rapido, los codigos son mas cortos y requieren menos memoria para ejecutarlos

#NumPy Data Types
#bool_
#int*, donde * es un numero que representa la cantidad de cifras significatvass del numero,8, 16, 32, 64
#float*, 16, 32, 64
#complex64
#complex128
import numpy as np

a = np.array([2,3,4])#crea un arreglo
print(a)
print("")
a = np.arange(1,12,2)#crea arreglo con numeros del 1 al 12 con un paso de 2
print(a)
print("")
a = np.linspace(1,12,6) #crea arreglo con numeros del 1 al 12 con 6 elementos flotantes
print(a)
print("")

a = a.reshape(3,2)#redimensiona el arreglo a. Ahora tendra 3 filas y dos columnas si se ve como una matriz. O mas bien tendra 3 listas de dos elementos cada una
print(a)
print("")

print(a.size)#entrega la cantidad de elementos
print("")
print(a.shape)#entrega las dimensiones
print("")
print (a.dtype)#entrega el tipo de los elementos del arreglo
print("")
print(a.itemsize)#entrega la cantidad de memoria en bits que requiere cada elementos del arreglo
print("")

b = np.array([(1.5,2,3), (4,5,6)])#crea un arreglo de dos dimesiones
print(a<4)#muestra los cuales elementos del arreglo cumple con la condicion. rpta booliana (True or False)
print("")
print(a*3)#multiplica cada elemento por 3
print("")

a = np.zeros((3,4))#crea arrecglo de solo ceros de dimensiones 3x4
print(a)
print("")

a = np.ones((2,3))#crea arreglo de solo unos de dimensiones 2x3
print(a)
print("")

a = np.ones(10)#crea arreglo con 10 unos en una dimension
print(a)
print("")

a = np.array([2,3,4], dtype = np.int16)#crea arreglo con elementos del tipo int16
print(a)
print("")
print(a.itemsize)#el resultado es 2, lo cual significa que ocupan menos memoria por lo tanto mas eficientes
print("")

a = np.random.random((2,3))# crea un arreglo con numeros al azar entre 0 y 1 de dimensiones 2x3
print(a)
print("")
np.set_printoptions(precision = 2, suppress = True)#configurando que imprima solo 2 decimales y no en notacion cientifica
print(a)
print("")

a = np.random.randint(0,10,5)#crea arreglo de 1 dimension con 5 elementos que son numeros al azar entre 1 y 10
print(a)
print("")

#datos estadisticos
print("suma total = ", a.sum())#suamndo los elementos
print("el minimo es: ", a.min())#entrega el minimo
print("el maximo es: ", a.max())#entrega el maximo
print("el promedio es igual a: ", a.mean())#enrtrega el promedio
print("Varianza = ", a.var())#varianza
print("Desv Estandar = ", a.std())#desv estandar

a = np.random.randint(1,10,6)
a = a.reshape(3,2)
print(a)
print("")
print(a.sum(axis=1))#muestra la suma de las listas interiores del arreglo. como este arreglo tiene 3 filas muestra la suma por filas, por lo tanto entrega un arreglo con tre elementos.
print("")
print(a.sum(axis=0))#muestra la suma por columnas
print("")

a = np.arange(10)#crea arreglo de 10 numeros
print(a)
print("")

np.random.shuffle(a)#reordena de manera al azar el arreglo a
print(a)
print("")

print(np.random.choice(a))#escoge un elemento al azar 
print("")

a = np.random.random_integers(5,10,2)#crea un arreglo de 2 elementos al azar entre los nuemros 5 y 10
print(a)
print("")

from io import StringIO

c = StringIO(u"0 1\n2 3")
print(np.loadtxt(c), type(c))

data = np.loadtxt("data1.txt", dtype = np.uint8, delimiter=',', skiprows=0)#importar archivo txt o csv de manera rapida y en lo parametros que se requieran
#skiprows es para saltarse las primeras lineas. si pongo 0 no se salta ninguna si pongo 1 se salta la primera.
#delimeter es para que reconozca el elemento que delimita cada elemento
#dtype le da el formato a los elementos del texto al momento de crear el arreglo en python

print(data)























