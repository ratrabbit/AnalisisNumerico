# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 05:12:30 2016

@author: francisco
"""

import numpy as np
import matplotlib.pyplot as plot

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y=[29.9,29.0,28.1,27.1,26.2,25.3,24.4,23.6,22.7,21.8,21.0,20.1,19.3,
   18.5,17.7,16.9]

plot.plot(x,y,'o')
plot.axis([0, 20, 0, 35])
plot.title('Grafiquita :v',color='m',fontsize=14)
plot.xlabel("x", fontsize= 10,color = 'b')
plot.ylabel("f(x)",fontsize= 10,color = 'b')
plot.grid(True)
plot.grid(color = '0.5', linestyle = ':', linewidth = 1)

prom_x = np.average(x)   
prom_y = np.average(y)
numerador = np.sum((x-prom_x)*(y-prom_y))
denominador = np.sum((x-prom_x)**2)
b= numerador/denominador
a = prom_y - (b*prom_x)

ynueva = np.zeros(len(y))
for i in range(len(y))  :
    ynueva[i] = a + (b*x[i])
print ynueva
#Grafica
p1 = plot.plot(x,ynueva,':',label = 'Ajuste por minimos cuadrados')
p2 = plot.plot(x,y,'o',label = 'Datos originales')
legend = plot.legend(loc='upper right', shadow=True, fontsize='large')
legend.get_frame().set_facecolor('#FFAAFF')
plot.axis([0, 20, 0, 35])
plot.title('Grafica',color='m',fontsize=14)
plot.xlabel("x", fontsize= 10,color = 'b')
plot.ylabel("f(x)",fontsize= 10,color = 'b')
plot.grid(True)
plot.grid(color = '0.5', linestyle = ':', linewidth = 1)
