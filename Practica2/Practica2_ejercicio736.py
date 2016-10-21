# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:40:48 2016

@author: francisco
"""
import numpy as np
def tri(d,b):
    n = len(d)
    x = np.zeros(n)
    for i in range(1,n):
        xmult = d[i][i-1]/d[i-1][i-1]
        d[i][i] -= xmult*d[i-1][i]
        b[i] -= xmult*b[i-1]
    x[n-1] = b[n-1]/d[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = (b[i]-d[i][i+1]*x[i+1])/d[i][i]
    print x

A = np.zeros((50,50))
print A
b = range(1,51)
bactual = np.zeros(50)
j = 0

for i in range(0,50):
    for i in range(0,49):
        A[i][i]=5
        A[i+1][i]=-1
        A[i][i+1]=-1
    for k in range(0,50):
        bactual[k]=b[(j+k)%len(b)]
    j = (j + 1) % len(b)
    #print bactual
    tri(A,bactual)