# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 00:59:39 2016

@author: francisco
"""

import numpy as np

def bi_diagonal(n,a,d,b):
    if n%2 == 0:
        return
    x = np.zeros(n)
    x[0] = b[0]/d[0]
    x[n-1]= b[n-1]/d[n-1]
    for i in range(1,n/2):
        x[i] = (b[i]-(x[i-1]*a[i-1]))/d[i]
    for i in range(n-2,n/2,-1):
        x[i] = (b[i]-(x[i+1]*a[i-1]))/d[i]
    x[n/2] = (b[n/2]-a[n/2]*x[n/2+1]-a[n/2-1]*x[n/2-1])/d[n/2]
    print x

a = np.array([[1.0,0.0,0.0],[2.0,3.0,2.0],[0.0,0.0,4.0]])
b = np.array([1.0,2.0,3.0])
diag = np.array([1.0,3.0,4.0])
aaa = np.array([2.0,2.0,2.0])
bi_diagonal(3,aaa,diag,b)