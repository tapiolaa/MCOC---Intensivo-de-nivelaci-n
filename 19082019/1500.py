# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:08:44 2019

@author: aniba
"""

#minuto 15:00
e = 20 # definiendo variables
f = 8
if e < f: #condicional
    print('e is less than f')#se imrpime si e < f
elif e == f:# nueva condicion que verifica si e es igual a f
    print('e is equal to f')#si se cumple que e es igual a f se imprime esto
elif e > f + 10:# una segunda condicion para verificar
    print('e is greater than f by more than 10')
else:#sino se cumple ninguna condicion anterior, ie e es mayor que f
    print('e is greater than f')#se imprime esto