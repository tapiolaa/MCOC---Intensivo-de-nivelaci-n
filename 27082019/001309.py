# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:26:36 2019

@author: aniba
"""

#Trabajando imagenes como arreglos 

from skimage import io
foto = io.imread('Belen_Anibal_Manquehue2_FULL.jpg')#leyendo imagen como arreglo
print(type(foto))

print(foto.shape)

import matplotlib.pyplot as plt
plt.imshow(foto)#mostrando imagen
plt.show()
plt.imshow(foto[::-1])#mostrando foto invertida
plt.show()
plt.imshow(foto[:, ::-1])#mostrando foto con efecto espejo
plt.show()
plt.imshow(foto[300:1100, 2000:3000])#mostrando una seccion de la imagen
plt.show()
plt.imshow(foto[::2, ::2])#comprimiendo imagen
plt.show()

print(foto)
foto_seno = np.sin(foto)
print(foto_seno)

import numpy as np
#se puede trabajar matematicamente la foto como arreglo pudiendo concretar operaciones como la siguientes:

print(np.sum(foto))
print(np.prod(foto))
print(np.mean(foto))
print(np.std(foto))
print(np.var(foto))
print(np.min(foto))
print(np.max(foto))
print(np.argmin(foto))
print(np.argmax(foto))

z = np.array([1,2,3,4,5])
print(z < 3)#im,prime un arreglo con true or false segun corresponda 
print(z > 3)
print([z < 3])#imprime solo aquellos valores que cumplen con la condicion de adentro de los corchetes

#Editando la imagen

foto_masked = np.where(foto > 100, 255, 0)#alterando colores de la imagen
plt.imshow(foto_masked)

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

#trabanjando con arreglos y op matematicas
print(a+b)
print(a+30)
print(a*b)

plt.imshow(foto[:,:,0].T)
plt.show()

x = np.array([2,1,3,4,5])
no.sort(x) #ordenando el arrglos de menor a mayor










