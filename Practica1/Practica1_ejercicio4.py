# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:26:22 2016

@author: francisco
"""
"""
Ejercicio 1.13
"""
"""
If an amount a is invested at interest rate r compounded n times per year, then the final 
value f at the end of one year is given by f = a(1 + r/n)^n
This is the familiar formula for compound interest. With simple interest, n = 1. Typically,
compounding is done quarterly, n = 4, or perhaps even daily, n = 365. Obviously, the more
frequent the compounding, the greater the final amount, because more interest is paid on
previous interest. But how much difference does this frequency actually make? Write a
program that implements the compound interest formula. Test your program using an
initial investment of a = 100, an interest rate of 5 percent (i.e., r = 0.05), and the following
values for n: 1, 4, 12, 365, 10,000, and 20,000.Implement the compound interest formula in
two different ways:
(a) If the programming language you use does not have an operator for exponentiation (e.g.,
C), then you might implement the compound interest formula using a loop that repeatedly
multiplies a by (1+r/n) for a total of n times.Even if your programming language does have
an operator for exponentiation (e.g., Fortran),try implementing the compound interest for-
mula using such a loop and print your results for the input values. Does the final amount al-
ways grow with the frequency of compounding,as it should? Can you explain this behavior?
"""
from math import exp,log
def potencia(x,n):
    prod = 1.0
    for i in range(0,n):
        prod*=x
    return prod

def interes(a,r,n):
    return a*potencia((1+float(r/n)),n)

print "a = 100, r = 0.05, n = 1 "+repr(interes(100,.05,1))
print "a = 100, r = 0.05, n = 4 "+repr(interes(100,.05,4))
print "a = 100, r = 0.05, n = 12 "+repr(interes(100,.05,12))
print "a = 100, r = 0.05, n = 365 "+repr(interes(100,.05,365))
print "a = 100, r = 0.05, n = 10000 "+repr(interes(100,.05,10000))
print "a = 100, r = 0.05, n = 20000 "+repr(interes(100,.05,20000))
"""
Podemos ver que cumple la formula del interes porque nunca deja de crecer y siempre es mayor
que la formula anterior, por lo que tiene el comportamiento esperado. En los ultimos dos ejemplos
con n=10000 y n = 20000 son muy parecidos porque al ser n muy grande el valor de la potencia empieza
a tender a 1.
b) Usando las funciones del paquete math. A partir de n = 365 empiezan a ser ligeramente mayores los resultados
de las funciones precargadas, lo que nos muestra la optimizacion de estas funciones contra nuestro loop para
obtener las potencias
"""
def interes1(a,r,n):
    return a*(exp(n*log(1.0+r/n)))
    
print "Valores con funcion exponencial y logaritmo"    
print "a = 100, r = 0.05, n = 1 "+repr(interes1(100,.05,1))
print "a = 100, r = 0.05, n = 4 "+repr(interes1(100,.05,4))
print "a = 100, r = 0.05, n = 12 "+repr(interes1(100,.05,12))
print "a = 100, r = 0.05, n = 365 "+repr(interes1(100,.05,365))
print "a = 100, r = 0.05, n = 10000 "+repr(interes1(100,.05,10000))
print "a = 100, r = 0.05, n = 20000 "+repr(interes1(100,.05,20000))