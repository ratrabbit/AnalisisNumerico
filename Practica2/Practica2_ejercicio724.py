# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 21:35:10 2016

@author: francisco
"""

import numpy as np
from scipy.linalg import hilbert
def gauss(A):
    n = len(A)
    for i in range(0, n): 
        maximo = abs(A[i][i])
        filamax = i
        for j in range(i+1, n):
            if abs(A[j][i]) > maximo:
                maximo = abs(A[j][i])
                filamax = j
        #-------OJO ------ INTERCAMBIO DE FILAS AQUI
        for j in range(i,n+1):
            tmp = A[filamax][j]
            A[filamax][j] = A[i][j]
            A[i][j] = tmp
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i,n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c*A[i][j] 
    x=np.zeros(10)
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x
#sin pivoteo
def solve(m,b):
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
    
A = hilbert(10)
B = hilbert(10)
b = np.zeros(10)
c = np.zeros(10)
for i in range(0,10):
    b[i] = np.sum(A[i])
    c[i] = np.sum(A[i])
z = np.zeros((10,1))
for i in range(0,10):
    z[i][0]=c[i]
B = np.append(B,z,axis = 1)
print solve(A,b)
print gauss(B)

