# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:13:45 2016

@author: francisco
"""
import numpy as np
from math import pi
ra = np.float32(7000.0)
rb = ra + np.float32(0.000001)
va = np.float32(float(4/3)*pi*ra**3)
vb = np.float32(float(4/3)*pi*rb**3)
d1 = vb - va
d2 = np.float32(float(4/3)*pi*(rb-ra)*((rb**2) + (rb*ra) + (ra**2)))
h = rb - ra
d3 = np.float32(4.0*pi*(ra**2)*h)
print "Usando precision simple"
print ra
print rb
print va
print vb
print d1
print d2
print h
print d3
print "Usando doble precision"
ra1 = np.float64(7000.0)
rb1 = ra1 + np.float32(0.000001)
va1 = np.float64(float(4/3)*pi*ra1**3)
vb1 = np.float64(float(4/3)*pi*rb1**3)
d11 = vb1 - va1
d21 = np.float64(float(4/3)*pi*(rb1-ra1)*((rb1**2) + (rb1*ra1) + (ra1**2)))
h1 = rb1 - ra1
d31 = np.float64(4.0*pi*(ra1**2)*h1)
print ra1
print rb1
print va1
print vb1
print d11
print d21
print h1
print d31
