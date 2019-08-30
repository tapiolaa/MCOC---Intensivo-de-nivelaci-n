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
print(a[::2])#IMPRIME CON PASO 2, ie las posiciones 0, 2 y 4
print("")

#Se debe tomar los arreglos del varias dimendsioens como una matriz. De esta manera, lograremos llegar a las posiciones de la matriz utilizando los indices y variandolos como si fueran filas y columnas

g = [1,2,3]
print(g[0]) #se imprime la posicion 0 pero se pierde la dimension, en este caso la lista
print(g[:1])#se conserva la dimension y se imprime la posicion 0

print("")

a = np.arange(25).reshape(5,5)
#primero se crea un arreglo con numeros del 1 al 25. Luego se redimensiona el arreglo en una matriz de 5 filas y 5 columnas
print(a)
print("")
print(a[:,1], a[:,3])#imprime columnas 1 y 3 por separado
print("")
print(a[1::2, :3:2])
print("")
print(a[1::2, :4:2])
print("")
print(a[1::2, :-1:2])
print("")
print(a[1::2, :-2:2])
print("")
print(a[4, :])#imprime ultima fila
print("")
print(a[:, 1::2])#imprime cols 1 y 3 juntas en una matriz
print("")
#Si creo una variable y guardo un trozo de la matriz (arreglo) llamado a en esta variable, luego modifico este trozo guardado. La modificacion tmbn se hara en la matriz original ya que se ha creado un enlace al crear la nueva variable.

#Fancy Indexing

#se crea un arreglo de 8 numeros del 0 al 80 con un paso de 10.
a = np.arange(0,80,10)
indices = [1,2,-3]
y = a[indices]
print(y)
print("")
#Imprimir numeros positivo o negativos de un arreglo

a = np.array([-3,4,5-7,3,6,-1,-2])
print(a<0)#entrega rspta booliana
print("")
negativos = a<0
print(a[negativos])#imprime numeros negativos
#otra manera
print("")
print(a[a<0])
print("")

#hacer que los negativos sean 0
a[a<0] = 0
print(a)

#verificar si algun numeros es menor que 8
print((a<8).any())
















