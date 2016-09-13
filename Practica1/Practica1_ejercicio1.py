# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:23:50 2016

@author: francisco
"""

"""
Ejercicio 1
1.6
a) Suppose you need to generate n+1 equally spaced points on the interval
[a,b] with spacing h = (b-a)/n. In floating point arithmetic, which of the following
methods is better and why?
x0 = a   xk = xk-1 + h k = 1,...,n
xk = a+kh k = 0,...,n

El metodo 2 es mejor porque en el primer metodo, hacemos uso del punto anterior
calculado para obtener el siguiente, si obtenemos numeros que no tienen representacion exacta
en nuestro sistema de punto flotante entonces estamos acarreando los errores, lo que hace que
en cada valor que calculemos nos alejemos cada vez mas de nuestro valor real esperado.
En el segundo metodo al calcular h vamos a obtener un unico error que no crecera de manera lineal
como en el primer caso, sino que permanecera a lo largo de nuestro calculo sin cambiar, lo que 
nos alejara menos de nuestro resultado real esperado.
b) Codigo
"""
a = 0.0
b = 10.0
n = 37
h = (b-a)/n
puntosA = []
puntosB = []
print "EJERCICIO 1.16"
#primer metodo
puntosA.append(a)
for i in range(0,n):
    xi = puntosA[i] + h
    puntosA.append(xi)
print "PRIMER METODO",puntosA
#segundo metodo
puntosB.append(a)
for i in range(1,n+1):
    yi = a + (i*h)
    puntosB.append(yi)
print "SEGUNDO METODO",puntosB
print len(puntosA),len(puntosB)
"""
Con este ejemplo podemos ver como en el primer caso no llegamos al numero exacto b, que seria el limite 
de nuestro intervalo y en el segundo si conseguimos algo mas exacto que es justo lo que queremos
