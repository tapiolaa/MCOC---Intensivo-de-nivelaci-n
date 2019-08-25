# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:02:32 2019

@author: aniba
"""

#Diccionarios

#minuto

d = {} #creando diccionario vacio

#Asignando variables (keys) al diccionario con sus respectivos valores (values)
#ejemplo nombre y edad

d["Anibal"] = 23
d["Ana"] = 59
d["Sergio"] = 86

print(d["Sergio"])# se muestra la edad uqe tiene sergio

print(d)   

d["Ana"] = 57 #cambiando el valor de la variable Ana. Ahora sera 57

#Los nombres de la variables (keys) pueden ser tanto strings como numeros

d[10] = 100

#Para recorrer un diccionario se puede hacer con un ciclo for qie considere las keys y los values de este.

for key, value in d.items():
    print("key: ", key)
    print("value: ", value)
    print("")
    


