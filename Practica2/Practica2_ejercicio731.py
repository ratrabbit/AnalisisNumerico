# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 23:40:23 2016

@author: francisco
"""
"""
for i in range(1,n):
        xmult = d[i][i-1]/d[i-1][i-1]
        d[i][i] -= xmult*d[i-1][i]
        b[i] -= xmult*b[i-1]
    x[n-1] = b[n-1]/d[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = (b[i]-d[i][i+1]*x[i+1])/d[i][i]
"""
import numpy as np
def tri(a,d,c,b):
    if len(a)==len(c) and len(a)==len(d)-1:
        n = len(d)
        x = np.zeros(n)
        for i in range(1,n):
            xmult = a[i-1]/d[i-1]
            d[i] -= xmult * c[i-1]
            b[i] -= xmult * b[i-1]
        x[n-1] = b[n-1]/d[n-1]
        for i in range(n-2,-1,-1):
            x[i] = (b[i]-c[i]*x[i+1])/d[i]
        return x
#Simetrico
matrizA = np.array([[1.0,2.0,0.0],[2.0,1.0,2.0],[0.0,2.0,1.0]])
d = np.array([1.0,1.0,1.0])
c = np.array([2.0,2.0])
a = np.array([2.0,2.0])
b = np.array([3,2,5])
print tri(a,d,c,b)
#No simetrico
matrizA1 = np.array([[1.0,2.0,0.0],[3.0,1.0,2.0],[0.0,3.0,1.0]])
d1 = np.array([1.0,1.0,1.0])
c1 = np.array([2.0,2.0])
a1 = np.array([3.0,3.0])
b1 = np.array([3,2,5])
print tri(a1,d1,c1,b1)