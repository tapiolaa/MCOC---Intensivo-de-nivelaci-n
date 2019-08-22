# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:30:20 2019

@author: aniba
"""

#Introduction to Listis

#En este codigo se recordo contenidos de listas y arreglos en lenguaje python

#minuto

a = [3, 10, -1] #se crea la lista llamada a
print(a)#printeo

a.append(1)# .append se usa para agragar elementos a la lista

print(a)

a.append("hola")#puede ser siferentes tipo de elementos [str, int, float, otras listas, etc]

print(a)

a.append([1, 2])

print(a)

a.pop()# .pop se utiliza para borrar elementos de la lista, si se utiliza .pop() se borrara el ultimo elemento de la lista

a[0] = 100 #cambiando el primer elemento de la lista que es un 3 por un 100. 

print(a)

a.pop(1)#poniendo dentro del parentesis el indice del elemento que se quiere borrar. En este caso en la posicion 1 de la lista se encontraba el numero 10, el cual fue eliminado
print(a)

