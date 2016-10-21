# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:18:16 2016

@author: francisco
"""
import numpy as np

def naiveGauss(n,a,b,x):
    for k in range(0,n-1):
        for i in range(k+1,n):
            xmult = a[i][k]/a[k][k]
            a[i][k] = xmult
            for j in range(k+1,n):
                a[i][j]-=xmult*a[k][j]
            b[i] -= xmult*b[k]
    x[n] = b[n]/a[n][n]
    for i in range(n-2,-1,-1):
        suma = b[i]
        for j in range(i+1,n):
            suma -= a[i][j]*x[j]
        x[i] = suma/a[i][i]
        
n = 2
matrizA = np.zeros(shape=(n,n))
for i in range(0,n):
    for j in range(0,n):
        matrizA[i][j]=i+j
matrizB = np.zeros(n)
for i in range(0,n):
    matrizB[i]=i+1
matrizX = np.zeros(n)
naiveGauss(n,matrizA,matrizB,matrizX)
print matrizB
#Resolver usando naive Gauss

        
        