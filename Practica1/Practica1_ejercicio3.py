# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:48:50 2016

@author: francisco
"""

"""
Ejercicio 1.12 Write a program to compute the mean x and standar deviation o of a finite sequence
xi. Your program should accept a vector x of dimension n as input and produce the mean and 
standard deviation of the sequence as output. For the standard deviation, try both the two-pass
formula and the one-pass formula and compare the results for an input sequence of your choice.
"""
def mean(vector):
    n = len(vector)
    sum = 0.0
    for i in range(0,n):
        sum += vector[i]
    sum = sum/(n*1.0)
    return sum
    
def tpdev(vector):
    n = len(vector)
    m = mean(vector)
    sum = 0.0
    for i in range(0,n):
        sum += (vector[i]-m)**2
    sum = sum / ((n-1)*1.0)
    sum = sum**0.5
    return sum
    
def opdev(vector):
    n = len(vector)
    m = mean(vector)
    sum = 0.0
    for i in range(0,n):
        sum += (vector[i]**2)
    sum -= n*(m**2)
    sum = sum / ((n-1)*1.0)
    sum = sum**0.5
    return sum
def programa(vector):
    print "mean= "+repr(mean(vector))
    print "2-passDev= "+repr(tpdev(vector))
    print "1-passDev= "+repr(opdev(vector))
print programa([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])
"""
b)b)A pesar de la entrada, que podemos ver claramente que la media es .1 y la desviacion 0, las 
2 formulas devuelven cosas muy distintas.
"""