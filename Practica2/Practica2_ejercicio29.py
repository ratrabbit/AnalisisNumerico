# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:48:19 2016

@author: francisco
"""

from scipy.linalg import lu
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
    
for k in range(1,11):
    epsilon = 10**(-2*k)
    a = np.array([[epsilon,1.0],[1.0,1.0]])
    b = np.array([1.0+epsilon,2.0])
    x = elimGauss(a,b)
    print "\nIteracion ",k    
    print x
    
"""Inciso b)"""

for k in range(1,11):
    epsilon = 10**(-2*k)
    a = np.array([[epsilon,1.0],[1.0,1.0]])
    b = np.array([1.0+epsilon,2.0])
    x = elimGauss(a,b)
    residuo = b-np.dot(a,x)
    print "residuo ",residuo
    y = elimGauss(a,residuo)
    resultado = [0.0]*len(a)
    for i in range(0,len(a)):    
        resultado[i] = x[i] + y[i]
    print "\nIteracion con refinamiento",k    
    print resultado
    
    
