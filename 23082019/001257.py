# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:49:35 2019

@author: aniba
"""

# ciclos while, otra manera de hacer loop en python. similar al tema anterior de los ciclos for

total = 0

j = 1
while j < 5: #ciclo while con la condicion para le contrador j, minetras este sea menor que 5 se ejecutara el ciclo.
    total += j
    j += 1
print(total)

lista = [5, 4, 4, 3, 1, -2, -3, -5]

#con el objetivo de sumar solo los numeros positivos de la lista se hace el siguiente ciclo while donde se recorre la lista y se verifica cnla condicion si es ositivo o negativo.

total2 = 0
i = 0
while lista[i] > 0:
    total2 += lista[i]# si es positivo se suma a la variable auxiliar
    i += 1
print(total2)

lista2 = [5, 4, 4, 3, 1]

#con el objetivo de sumar solo los numeros positivos de la lista se hace el siguiente ciclo while donde se recorre la lista y se verifica cnla condicion si es ositivo o negativo.

total3 = 0
i = 0 #renuevo el contador
while i < 5 and lista2[i] > 0:
    total3 += lista2[i]# si es positivo se suma a la variable auxiliar
    i += 1
print(total3)

#retomando la lista = [5, 4, 4, 3, 1, -2, -3, -5] buscamos sumar los numeros positivo pero ahora con ciclo for y condicional if, luego se escribira como seria con ciclo while utilizando la herramienta break 

total4 = 0
for j in lista:
    if j <= 0:
        break
    total4 += j
    
print(total4)

 #ahora con ciclo while
 
total5 = 0
i = 0 #renuevo el contador
while True:
    total5 += lista[i]
    i += 1
    if lista[i] <= 0:
        break
print(total5)

#propuesto: sumar los numeros negativos de la lista3. usar ciclo for o ciclo while
lista3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total6 = 0
for k in lista3:
    if k < 0:
        total6 += k

print(total6)





