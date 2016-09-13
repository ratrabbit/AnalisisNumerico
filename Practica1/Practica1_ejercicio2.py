# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:02:31 2016

@author: francisco
"""
from math import exp
#Calculo de la exponencial, inciso a)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def exp1(x):
    actual = 0.0
    anterior = 0.0
    i = 0
    while True:
        anterior = actual
        #print actual
        actual += (x**i) / (factorial(i)*1.0)
        if actual == anterior:
            break
        i+=1
    return actual
    
"""
b) El criterio que debemos usar para detener el programa es que el resultado actual sea igual al
resultado previo en las iteraciones de la funcion, ya que estamos en un sistema de punto flotante
y llegara un momento en el que no nos alcance los numeros para representar el resultado de la
funcion

c) Prueba el programa con +-1,+-5,+-10,+-15,+-20 y compare con la funcion ex de python
"""
print "Resultado con +1: "+repr(exp1(1))+" vs python:"+repr(exp(1))
print "Resultado con -1 "+repr(exp1(-1))+" vs python:"+repr(exp(-1))
print "Resultado con +5 "+repr(exp1(5))+" vs python:"+repr(exp(5))
print "Resultado con -5 "+repr(exp1(-5))+" vs python:"+repr(exp(-5))
print "Resultado con +10 "+repr(exp1(10))+" vs python:"+repr(exp(10))
print "Resultado con -10 "+repr(exp1(-10))+" vs python:"+repr(exp(-10))
print "Resultado con +15 "+repr(exp1(15))+" vs python:"+repr(exp(15))
print "Resultado con -15 "+repr(exp1(-15))+" vs python:"+repr(exp(-15))
print "Resultado con +20 "+repr(exp1(20))+" vs python:"+repr(exp(20))
print "Resultado con -20 "+repr(exp1(-20))+" vs python:"+repr(exp(-20))
"""
d) si puedo porque podemos obtener el inverso de la positiva
"""
print "invirtiendo la exp para obtener mejores resultados"
print "Resultado con -1 "+repr(1/exp1(1))+" vs python:"+repr(exp(-1))
print "Resultado con -5 "+repr(1/exp1(5))+" vs python:"+repr(exp(-5))
print "Resultado con -10 "+repr(1/exp1(10))+" vs python:"+repr(exp(-10))
print "Resultado con -15 "+repr(1/exp1(15))+" vs python:"+repr(exp(-15))
print "Resultado con -20 "+repr(1/exp1(20))+" vs python:"+repr(exp(-20))
"""
e) Podemos agrupar los terminos con exponente impar, sumarlos todos como positivos pero desde el termino
mas pequeño por la acumulacion de errores y despues restar el resultado al resto de los terminos
aunque seria mas facil solo invertir la exponencial negativa
"""