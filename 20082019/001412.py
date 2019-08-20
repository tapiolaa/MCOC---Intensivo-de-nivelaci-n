# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:11:01 2019

@author: aniba
"""

# calculadora de indice de masa corporal

#minuto 14:12
#definiedo variables
name1 = "anibal"
height_m1 = 2
weight_kg1 = 90

name2 = "bro"
height_m2 = 1.8
weight_kg2 = 70

name3 = "sis"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg): #defino mi funcion con sus varibles
    bmi = weight_kg / (height_m**2) #formula para calcular el indice de masa corporal
    print("bmi: ")
    print(bmi)
    if bmi < 25:#condicional
        return name + " not overweight"#si se cumple condicion la funcion retornara este valor y lo guaardara en la varible dispuesta
    else:
        return name + " is overweight"#sino retorna esto

#llamando a la funcion
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

#mostrando resultados
print(result1)
print(result2)
print(result3)