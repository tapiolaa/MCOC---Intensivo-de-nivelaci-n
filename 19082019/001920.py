# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:10:18 2019

@author: aniba
"""

#minuto 19:20
name = 'YK' #se definen variables de un problema, [nombre, altura, peso] de una persona 
height_m = 2 
weight_kg = 110

# se queire saber si la persona esta con sobrepeso o no
# por lo tanto se utiliza la siguiente formula que corresponde al indice de masa corporal de la persona
# esta estara en sobrepeso si el indice (bmi) es mayor a 25
# y sera una persona sana si el indice (bmi) es menor a 25

bmi = weight_kg / (height_m**2) #fomrula bmi
print('bmi: ')
print(bmi) #entregando resultado del bmi
if bmi < 25: #condiciona para evaluar sobrepeso o no
    print(name)
    print('is not overweight') #se cumple condicion, por lo  tanto la persona esta saludable
else: #no se cumple condicion
    print(name)
    print('is overweight') #por lo tanto la persona esta con sobrepeso