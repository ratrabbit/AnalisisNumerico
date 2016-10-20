# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:00:44 2016

@author: francisco
"""
import numpy as np
def elimGauss(m,b):
    n = len(m)
    for i in range(0,n-1):
        for a in range(i+1,n):
            p = m[a][i]/m[i][i]
            for j in range(i+1,n):
                m[a][j] -= p*m[i][j]
            m[a][i] = 0
            b[a] -= p*b[i]
    cero = np.float32(0)
    ceros = [cero]*n
    for i in range(n-1,-1,-1):
        aux = 0
        for j in range (i+1,n):
            aux += m[i][j]*ceros[j]
        ceros[i] = (b[i]-aux)/m[i][i]
    return ceros
"""Inciso a)"""
A=np.array([[21.0, 67.0, 88.0, 73.0], [76.0, 63.0, 7.0, 20.0], [0.0, 85.0, 56.0, 54.0], [19.3, 43.0, 30.2, 29.4]],dtype='f')
b=np.array([141.0, 109.0, 218.0, 93.7],dtype='f')
solucion=elimGauss(A,b)
print "Solucion: ",solucion
print "\n"
"""Inciso b)"""
cero = np.float64(0)
ceros = [cero]*len(A)
suma = np.float64(0)
residuo = b - np.dot(A,solucion)
print "Residuo= ",residuo
print "\n"
z = elimGauss(A,residuo)
improved = [0.0]*len(A)
for i in range(0,len(A)):
    improved[i] = solucion[i] + z[i]
print "Improved= ",improved
print "\n"
for i in range(0,30):
    solucion = improved
    residuo = b - np.dot(A,solucion)
    res = elimGauss(A,residuo)
    for l in range(0,len(A)):
        improved[l] = solucion[l] + res[l] 
    print "Iteracion ",i
    if solucion == improved:
        break
    print "\n"
    
    
                