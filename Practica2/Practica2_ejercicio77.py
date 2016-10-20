# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:25:38 2016

@author: francisco
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sin
def elimGauss(m,b):
    n = len(m)
    for i in range(0,n-1):
        for a in range(i+1,n):
            p = m[a][i]/m[i][i]
            for j in range(i+1,n):
                m[a][j] -= p*m[i][j]
            m[a][i] = 0
            b[a] -= p*b[i]
    cero = np.float32(0)
    ceros = [cero]*n
    for i in range(n-1,-1,-1):
        aux = 0
        for j in range (i+1,n):
            aux += m[i][j]*ceros[j]
        ceros[i] = (b[i]-aux)/m[i][i]
    return ceros
#inciso a)
t1 = np.array([1900.0,1910.0,1920.0,1930.0,1940.0,1950.0,1960.0,1970.0,1980.0])
N = 9
#esquema 1
v1 = np.vander(t1, N)
cond1 = np.linalg.cond(v1,np.inf)
print v1
print "Condicion 1:",cond1
#esquema 2
t2 = t1-1900.0
v2 = np.vander(t2, N)
cond2 = np.linalg.cond(v2,np.inf)
print v2
print "Condicion 2:",cond2
#esquema 3
t3 = t1-1940.0
v3 = np.vander(t3, N)
cond3 = np.linalg.cond(v3,np.inf)
print v3
print "Condicion 3:",cond3
#esquema 4
t4 = t1-1900.0
t4 = t2/40.0
v4 = np.vander(t4, N)
cond4 = np.linalg.cond(v4,np.inf)
print v4
print "Condicion 4:",cond4
#inciso b)
y = np.array([76212168,92228496,106021537,123202624,132164569,151325798,179323175,203302031,226542199])
coeficientes = np.linalg.solve(v4,y)
print coeficientes
#metodo de Horner
reverseCoef = np.flipud(coeficientes)
valores = np.zeros(81)
k=0
for anio in range(1900,1981):
    valores[k] = np.polynomial.polynomial.polyval((anio-1900.0)/40.0,reverseCoef)
    k+=1
print valores
#inciso c)
cs = sin.spline(range(1900,1981,10),y,range(1900,1981))
plt.figure(figsize=(10,10))
plt.plot(range(1900,1981),valores,'r',label ='interpolacion')
plt.plot(range(1900,1981,10),y,'bs',label ='datos')
plt.plot(range(1900,1981),cs,'g',label = 'spline')
plt.legend(loc='lower right',ncol=2)
plt.show()
#inciso d)
aprox1 = np.polynomial.polynomial.polyval((1990-1900.0)/40.0,reverseCoef)
#cs1 = sin.spline(range(1900,1981,10),y,range(1900,1991))

        
