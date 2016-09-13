# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:26:21 2016

@author: francisco
"""
import matplotlib.pyplot as plt
"""
1.16 (python usa double por default)
"""
def eq(x1,x2,n):
    lista = [None]*n
    lista[0]=x1
    lista[1]=x2
    equis = []
    equis.append(0)
    equis.append(1)
    for i in range(2,n):
        equis.append(i)
        lista[i]=(2.25*lista[i-1]) - (0.5*lista[i-2])
    plt.plot(equis, lista, 'ro')
    plt.show()
    return lista
print eq(1.0*1/3,1.0*1/12,60)
"""
De acuerdo al ejercicio, la solucion obtenida es xk = (4^(1-k))/3 lo que nos muestra que 
conforme k avance, el resultado ira decreciendo, sin embargo, al realizar la solucion con el codigo 
anterior vemos que aproximadamente desde k = 30 nuestra solucion empieza a incrementar llegando a
1.7 aprox para k = 59, lo cual se parece al problema 1.6, estamos acarreando los errores de representacion
y estamos obteniendo el siguiente termino a partir de los dos terminos anteriores ya mal representados.
Obviamente la solucion analitica sera exacta al usar numeros reales, pero no para flotantes.
"""
