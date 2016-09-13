# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:34:56 2016

@author: francisco
"""

"""
1.17 (python usa double por default)
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
        lista[i]=111 - (1130-(3000/float(lista[i-2])))/float(lista[i-1])
    plt.plot(equis, lista, 'ro')
    plt.show()
    return lista
print eq(1.0*11/2,1.0*61/11,20)
"""
Se cumple la convergencia a 6 hasta el valor de k = 13, despues de ahi el crecimiento se dispara 
llegando a 100 en el ultimo valor de k
"""