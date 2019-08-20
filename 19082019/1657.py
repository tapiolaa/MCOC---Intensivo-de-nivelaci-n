# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:09:15 2019

@author: aniba
"""

#minuto 16:57
g = 7 #definiendo variables
h = 8
if g < h:#condicional 1
    print('g is less than h')#se imprime esto si se cumple la condicion anterior
else: #si la cond anterior no se cumple se entra al condicional que sigue
    if g == h: #condicional 2
        print('g is equal to h') # si no se cumple el condicional 1, pero si el condicional 2, se imprime esto
    else:# sino se cumple ninguno de los dos condicionales 
        print('g is greater than h')#se imprime esto