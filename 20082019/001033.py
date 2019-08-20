# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:56:26 2019

@author: aniba
"""

#se introduce el concepto de funcion dependiente de dos variables.
# se hace diferencia entre los print dentro de la funcion y los return de la funcion

#minuto 10:33
def funcion3(x, y):#defieniendo func de dos variables
    return x + y #lo que devolvera

e = funcion3(1, 2)#llamando a la func
print(e) #printeando


def funcion4(4):
    print(x)
    print("still in this function")
    return 3*x
#se hace la diferencia entre print y return, lo return no aparecen en consola sino que entregan un valor y lo gurdan en una variable que es lo que suceda en la sgte linea de codigo

f = funcion4(4)

print(f)

def funcion5(algo):#da lo mismo como se le nombre a la varible dependiente
    print(algo)
    print("weee")

