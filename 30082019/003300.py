# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:59:40 2019

@author: aniba
"""

#Tutorial Matplotlib

from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()#agrega un efecto al grafico, resalta las curvas

print(plt.style.available)#para mostrar los estilos de graficos disponibles
plt.style.use('ggplot')#para usar un estilo
edades = list(range(25,36))#creo lista eje x

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]#creo lista eje y
plt.plot(edades, dev_y, color='c', marker='o', label="All Devs")#ploteo un graficio. la funcion plot tiene definido por posiciones las listas en eje x y en eje y de manera que .plot(x, y)


py_dev_y = [33496, 35000, 44782, 47620, 51200, 54500, 59816, 63988, 65417, 66828, 70752]#creo lista eje y
plt.plot(edades, py_dev_y, linestyle='--', marker='.', label="Python")#label es otra manera de poner leyendas en el grafio. Se le da nombre inmediatamente a la curva

#'k--' le da formato y color a la curva, tambin se puede hacer por separado con color y linestyle.

#marker es para remarcar los puntos graficados pertenecientes a las listas

#color puede ser escrito o llamado en formato RGB, donde se pondran numeros como #444444, donde los dos primeros son para el rojo, luego verde y azul
#Poner titulos a los ejes del grafico

js_dev_y = list(np.random.randint(30000,72000, 11))
js_dev_y.sort()

plt.plot(edades, js_dev_y, marker='.', label="JavaScript")
#linewidth configura el groso de la linea que aparecera en el grafico

plt.ylabel("Salario (USD)")
plt.xlabel("Edades")

#titulo de grafico
plt.title("Salario promedio por rango de edades")

#colocar leyenda de grafico, para muchas curvas
plt.legend()

plt.grid(True)#agrega la grilla al graf
plt.tight_layout()#reodena los parametros del grafico. se le puede entregar pads de diferentes largos

plt.savefig('plot.png')
plt.show()
















