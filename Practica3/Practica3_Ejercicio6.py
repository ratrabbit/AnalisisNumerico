# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 04:16:32 2016

@author: francisco
"""

from scipy import integrate
from math import cos,exp,pi

f = lambda x : exp(-1.0*x)*cos(x)
a = 0
b = 2*pi
espacio = b/32
arregloX = [0.0]*33
arregloY = [0.0]*33
for i in range(33):
    arregloX[i] = a + i*espacio
    arregloY[i] = f(arregloX[i])
#print arregloX
#trapecio
trapecio = integrate.cumtrapz(arregloY,arregloX)
print "Trpecio:",trapecio[-1]
#punto medio
total = 0.0
for k in range(1,32):
    total += f(a + (k*espacio))
total *= espacio
pmedio = total
print "Punto medio",pmedio
#gauss
f1 = lambda y : [ exp(-1.0*x)*cos(x) for x in y ]
total = 0.0
for k in range(1,33):
    total += integrate.fixed_quad(f1,a+((k-1)*espacio),a+(k*espacio),n=2)[0]
gauss = total
print "Gauss",gauss
#simpson
simpson = integrate.simps(arregloY,arregloX)
print simpson
print "El resultado del libro es de 0.499066278634"