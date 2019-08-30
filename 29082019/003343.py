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
#si uno de los elementos es del tipo complejo, entoces el arreglo sera del tipo complex128

a = np.array([1,2,3,4.0+1j])
print(a.dtype)
print("")

#se puede escoger el tipo del arreglo con la variable dtype 
a = np.array([1,2,3,4], dtype='int8')
print(a.dtype)

##dos dimendiones

c = np.array([[10,11,12],[20,21,22]])
print(c.size) #imprime la cantidad de elemetenrtos totales, en todas las dimensiones
print("")
print(c.nbytes)#cuantas memoria usa el arreglo
print("")

#Slicing
a = np.array([10,11,12,13,14])

#imprime los numeros 11 y 12.
#las posiciones del arreglo son: 0,1,2,3,4
# y alreves son: -5,-4,-3,-2,-1

print(a[1:3])#seimprime las posiciones 1 al 3 son contar el 3. Nunca imprimira la ultima
print(a[1:-2])
print(a[-4:3])
print("")
#si se omite una frontera, se asume que se nesecita desde el inicio o desde el final segun seea el caso

print(a[:3])
print(a[-2:])
print(a[::2])
print("")






