# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:57:28 2019

@author: aniba
"""

# Sumar algunos elemenctos de una lista

#MINUTO

total = 0 #creo una variable auxiliar
for i in range(1, 8):# en este ciclo estoy recorriendo un arreglo del 1 al 7
    if i % 2 == 0:#con esta condicion estoy sumando todos los numeros pares del arreglo ya que el operador % hace referancia al resto de la division de cada elemento entre 2.
        total += i # si la condicion de cumple entonces de suma el numero y se agraga a la variable total, generando la suma de todos los nuemros pares.
print(total)

#Respuesta al desafia de sumar todos los multiplis de 3 y 5 menores a 100

sum_mult_de_3 = 0 # secrean variables auxiliares
sum_mult_de_5 = 0
sum_mult_de_3_y_5 = 0

#primer ciclo, encontrando la suma de los multiplos de 3 y 5 por separado menores a 100 considerando el 100 
for j in range(1, 101):
    if j % 3 == 0:
        sum_mult_de_3 += j
    elif j % 5 == 0:
        sum_mult_de_5 += j
        
#segunto ciclo, encontrando la suma de los multiplos de 3 y 5 menores a 100 considerando el 100
for k in range(1, 101):
    if k % 3 == 0 and k % 5 == 0: #condicion doble
        sum_mult_de_3_y_5 += k# esto ocurrira si solo si se cumplen ambas condiciones al mismo tiempo.
        
print('La suma de los multiplos de 3 menores a 100 es: ', sum_mult_de_3)
print('La suma de los multiplos de 5 menores a 100 es: ', sum_mult_de_5)
print('La suma de los multiplos de 3 y 5 menores a 100 es: ', sum_mult_de_3_y_5 )
