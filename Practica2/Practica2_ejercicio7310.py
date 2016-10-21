# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 22:29:52 2016

@author: francisco
"""
import numpy as np
n = 7

def x_gauss(m,b):
    if len(m)%2 == 0:
        print "La n debe ser impar"
        return
    n = len(m)
    for i in range(0,n-1):
        for j in range(i+1,n):
            p = m[j][i]/m[i][i]
            for k in range(i+1,n):
                m[j][k] -= p*m[i][k]
            m[j][i] = 0
            b[j] -= p*b[i]
            
def x_solve(m,b):
    n = len(m)
    cero = np.float32(0)
    ceros = [cero]*n
    for i in range(n-1,-1,-1):
        aux = 0
        for j in range (i+1,n):
            aux += m[i][j]*ceros[j]
        ceros[i] = (b[i]-aux)/m[i][i]
    return ceros
matrizA = np.array([[1.0,0.0,3.0],[0.0,2.0,0.0],[5.0,0.0,4.0]])
b = np.array([12,3,7])
bfinal = np.array([12,3,7])
x_gauss(matrizA,b)
print "MATRIZ A\n",matrizA
print "VECTOR B\n",b
print "SOLUCION\n",x_solve(matrizA,bfinal)
