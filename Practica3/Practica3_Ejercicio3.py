# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 01:13:48 2016

@author: francisco
"""
from random import randint
from math import exp
from scipy import integrate
def fik(k):
    f = lambda x : (x**k)*exp(x)
    result,error = integrate.quad(f,0,1)
    return exp(-1)*result
#inciso a)
valores = []
for k in range(0,21):
    a = fik(k)
    valores.append(a)
    print a
print
#inciso b)
print "------------Inciso b---------------"
valores1 = [0]*21
icero = 1-exp(-1)
valores1[0] = icero
for i in range(1,21):
    valores1[i] = 1 - i*valores1[i-1]

for v in range(0,21):
    print v,valores[v],valores1[v],valores[v]==valores1[v],"error:",abs(valores[v]-valores1[v])

for v in range(0,21):
    if valores[v] != valores1[v]:
        print "Como podemos ver, no son iguales"
        break
    print "Al comparar los resultados, son iguales"
#inciso c)
print "------------Inciso c---------------"
rand = randint(21,100)
valores2 = [0]*rand
iene = 0.0
print rand," es nuestro valor de n"
valores2[rand-1] = iene
for i in range(rand-2,-1,-1):
    valores2[i] = (1.0 - valores2[i+1])/((i+1)*1.0)
for i in range(0,rand):
    print valores2[i]
#inciso d en reporte

    
    