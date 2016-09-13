# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:26:21 2016

@author: francisco
"""

"""
1.16 (python usa double por default)
"""
def eq(x1,x2,n):
    lista = [None]*n
    lista[0]=x1
    lista[1]=x2
    for i in range(2,n):
        lista[i]=(2.25*lista[i-1]) - (0.5*lista[i-2])
    return lista
print eq(1.0*1/3,1.0*1/12,60)
#Falta hacer grafica y solucion general
