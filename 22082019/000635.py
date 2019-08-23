# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:37:32 2019

@author: aniba
"""

#introduction to for loops

#minuto 6:35

a = ['lambo', 'rari', 'mclaren']

for elemento in a: #ciclo que recorre la lista por posiciones. en este caso 'elemento' representa los indices de la lista el cual va de menor a mayor, ie, desde el 0 al ultimo termino de la lista.
    print(elemento)
    
b = [1, 2, 3]
total = 0
for i in b: #da igual lo que ponga en el ciclo, es simplemente un contador que representa los indices de la lista
    #print(i)
    total = total + i #creo una variable que me guardara la suma de los elementos de la lista, mientras se ejecute el ciclo for
print(total)#muestro la suma final de los elementos de la listas.

c = list(range(1, 6)) #creo un arreglo con el comando range con numeros dell 1 al 6, sin incluir el 6, ie, tendre una arreglo con numeros del 1 al 5. Luego convierto este arreglo a una lista con al comnado list y lo guardo e  la variable c.
print(c)

total1 = 0
for j in range(1, 6):#con este ciclo recorro los elementos del arreglo
    #print(j)
    total1 += j#aqui se suman los elementos, uno por uno mientras avanza el ciclo, de igual manera que el ciclo anterior
print(total1)


    










