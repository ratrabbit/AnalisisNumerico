# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:12:39 2016

@author: francisco
"""
import numpy as np
def f(n):
    return np.float32(float(1.0/float(n)))

def g(n):
    result = np.float32(0.0)
    for i in range(0,n):
        result += f(n)
    return result

def h(n):
    return np.float32((1.0*n)*f(n))

for i in range (1,51):
    print "Con n = "+repr(i)
    print repr(f(i))+" "+repr(g(i))+" "+repr(h(i))