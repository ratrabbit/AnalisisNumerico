# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:01:09 2016

@author: francisco
"""

from scipy.linalg import hilbert
import numpy as np
n=1
error = 0
z = []
while error*100 <= 100:
    print "n= ",n
    h = hilbert(n)
    print "Matriz de hilbert de dimension ",n
    print h
    x = np.ones(n)
    b = np.dot(h,x)
    condicion = np.linalg.cond(h)
    xgorro = np.linalg.solve(h,b)
    print "\nSolucion (x gorro) = ",xgorro
    residuo = b-np.dot(h,xgorro)
    normainf = np.linalg.norm(residuo,np.inf)
    error = np.linalg.norm(xgorro - x)
    print "\nError ",error
    n+=1
print "n solo llego hasta el valor de ",n-1
print "el error en este valor de n es de ",error
print "la solucion en este valor de n es ",xgorro