# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:00:01 2019

@author: aniba
"""

#Aprendiendo Numpy en 5 minutos

import numpy as np

a = np.zeros(3) #creando un arreglo que contiene 3 numeros 0
print(a)
print(type(a))
print("")
z = np.zeros(10)#creando un arreglo que contiene 10 numeros 0
print(z.shape)#.shape entrega el largo del arreglo
print("")
z.shape = (10, 1) #forma un arreglo de arreglos. reformula un matriz
print(z)
print("")
z = np.ones(10)#crean arreglo de 10 numeros 1
print(z)
print("")
z = np.empty(3) #crea arreglo vacio. 3 numeros cero
print(z)
print("")
z = np.linspace(2, 10, 5) #crea un arreglo con 5 numeros entre 2 y 10
print(z)
print("")
z = np.array([10, 20])#volviendo arreglo a una lista
print(z)
print("")
lista = [1,2,3,4,5,6,7]#volviendo arreflo a una lista
z = np.array([lista])
print(z)
print("")
lista1 = [[9,8,7,6,5,4,3],[1,2,3,4,5,6,7]]
z = np.array([lista1])#crenado un arreglo con dos listas. arreglo con dos elementos
print(z)
print("")
print(z.shape)
print("")
np.random.seed(0)
z1 = np.random.randint(10, size=6)#creando un arreglo de 6 elementos aleatorios
print(z1)
print("")
#accediendo a elemnetos de los arreglos
print(z1[0])#los arreglos se manejanigual que una lista
print(z1[0:2])
print(z1[-1])













