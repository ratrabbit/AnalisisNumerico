# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 02:07:30 2016

@author: francisco
"""
from math import cos

def pfalsa(f, a, b, iters, tolerancia):
    result = 0.0
    fr = 0.0
    side = 0.0
    fa = f(a)
    fb = f(b)
    for i in range(iters):
        r = (f(a)*b - f(b)*a) / (f(a)-f(b))
        if abs(b-a)<tolerancia*abs(b+a):
            break
        fr = f(r)
        if fr * fb > 0:
            b = r
            fb = fr
            if side == -1:
                fa /= 2
            side = -1
        elif fa * fr > 0:
            a = r
            fa = fr
            if side == 1:
                fb /= 2
            side = 1   
        else:
            break
    return r
    print "Con regula falsi, la raiz se aproximo a ",result
def bisection(f, a, b, iters, tolerancia):
    c = (a+b)/2
    i = 0
    while (b-a)/2 > tolerancia or i<iters:
        if f(c) == 0:
            print "El metodo de biseccion tomo %d iteraciones" % (i)
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
        c = (a+b)/2
        i+=1
    print "Se cumplio el limite de iteraciones"
    return c
    
f = lambda x : x**5 - 1
print pfalsa(f,0.0,2.0,1000,0.00001)
print bisection(f,0.0,2.0,1000,0.00001)
f = lambda x : cos(x) - x**3
print pfalsa(f,0.0,2.0,1000,0.00001)
print bisection(f,0.0,2.0,1000,0.00001)
f = lambda x : x**3 + x**2 + 5*x + 3
print pfalsa(f,-5.0,2.0,1000,0.00001)
print bisection(f,-5.0,2.0,1000,0.00001)

    