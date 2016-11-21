# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:45:28 2016

@author: francisco
"""
from math import sin,cos
from scipy.optimize import fsolve
##### INCISO B ###########
def eme(e):
    return e-0.5*sin(e)
    
def ge(m,e):
    return m + 0.5*sin(e)
resultados = []
e0 = 1.0
m = 1.0
iteraciones = 100
tolerancia = 0.00000001
print e0,"aaaaaaaaaaaaa"
yn = eme(e0)
error = tolerancia + 1.0
i = 0
resultados.append([i,e0,yn,error])
while yn != 0 and error > tolerancia and i < iteraciones:
    xn = ge(1,e0)
    print xn
    yn = eme(xn)
    print yn
    error = abs((xn-e0)/xn)
    i+=1
    e0 = xn
    resultados.append([i,xn,yn,error])

if yn == 0:
    print e0,"Es raiz"
elif error < tolerancia:
    print e0,"Es una aproximacion"
else:
    print "Error, prueba con mas iteraciones"
for r in resultados:
    print r,"\n"

############## INCISO C ############
f = lambda e : (e - 0.5*sin(e))-1
df = lambda x : 1 - 0.5*cos(x)
epsilon = 0.000001
x1 = 1.0
delta = abs(0-f(x1))
while delta > epsilon:
    x1 = x1 - f(x1)/df(x1)
    delta = abs(0-f(x1))
print "-------------Inciso C-----------"
print x1," es la raiz encontrada con el metodo de Newton"
############## INCISO D ############
#buscamos m = 1
print "-------------Inciso D-----------"
f1 = lambda e : (e - 0.5*sin(e))-1
e0 = fsolve(f1,1.0)
print e0," es la solucion"
    