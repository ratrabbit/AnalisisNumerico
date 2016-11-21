# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 04:00:59 2016

@author: francisco
"""
def newton(f,df,epsilon,x1):
    x = x1
    delta = abs(0-f(x))
    i = 0
    while delta > epsilon:
        x = x - f(x)/df(x)
        delta = abs(0-f(x))
        i+=1
    print "Newton normal utilizo %d iteraciones" % (i)
    return x

def dopenewton(f,df,epsilon,x1):
    x = x1
    delta = abs(0-f(x))
    i = 0
    while delta > epsilon:
        x = x - 2*f(x)/df(x)
        delta = abs(0-f(x))
        i+=1
    print "Newton dopado utilizo %d iteraciones" % (i)
    return x
    
f = lambda x : (x-8)**2
df = lambda x : 2*(x-8)

print(newton(f,df,0.000001,3))
print(dopenewton(f,df,0.000001,3))