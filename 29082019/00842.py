# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:08:58 2019

@author: aniba
"""

#Introduccion a la calculo numerico usando NumPy

#Igual que ne videos anteriores se hace referencia a las diferencias entre trabajar con listas y trabajar con arreglos. Siendo estos ultimos los mas rapidos para trabajar en python.

import numpy as np

g = list(range(1000000))
g_array = np.array(g)

a = [1,2,3,4]

a = np.array([1,2,3,4])
b = np.array([10,11,12,13])

#Introduccion a los arreglos NumPy

#numeros de dimensiones
print(a.ndim)

# tupla con cantidad de elementos de cada dimension del elemento
print(a.shape)
print("")
# se tiene una tupla cuando existen parentesis y comas juntos

#Se pueden aplicar las operaciones matematicas entre arreglos tal como sigue
print(a*b)
print("")
print(a+10)
print("")
print(a*100)
print("")
print(np.sin(a))
print("")

#Como saber el tipo de arreglo?
#el tipo por defecto es el int32 en so windows

print(a.dtype)
print("")
#si uno de los elementos dek arreglos es de tipo float, entonces el tipo del arreglos sera float64

a = np.array([1,2,3,4.0])
print(a.dtype)
print("")
#si uno de los elementos es de complejo, entoces el arreglo sera del tipo complex128

a = np.array([1,2,3,4.0+1j])
print(a.dtype)
print("")

a = np.array([1,2,3,4], dtype='int8')
print(a.dtype)



del tipo








