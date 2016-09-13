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
b) Con una lista de diez .1, la formula de 2 pasadas nos dice que la desviacion es aprox 1.42x10^-17
mientras que con una pasada nos muestra una desviacion de 2.48x10^-9. Como la desviacion nos dice
que tanto estan variando nuestros datos con respecto a la media, como la media ya nos esta dando un
valor equivocado entonces vemos que la mejor aproximacion es la formula de 2 pasadas (el error es mas chico)
esto se debe a que en la primer formula ya desde la distancia obtenemos algo muy cercano a cero, basicamente solo
cargamos el error de la representacion y lo elevamos al cuadrado para despues obtener una raiz.
En la segunda formula restamos la media al cuadrado pero tambien acarreamos el error y lo quitamos n veces de nuestro
valor, por lo que, al contrario de la formula anterior, estamos aumentando el error y eso nos aleja mas del resultado real
"""