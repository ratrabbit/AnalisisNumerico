# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:36:21 2016

@author: francisco
"""

def reciprocos(n,limite):
    if limite == 0:
        return 10.0/(n+1), 10.0/n
    else:
        if n > 0:
            inf,sup = 1.0/n,1.0/n
        else:
            inf,sup = 0,0
        for i in range(10*n+1,10*n+10):
                l,u = reciprocos(i,limite-1) #exapndimos los digitos
                inf += l
                sup += u
        return inf,sup
        
def rec(k):
    suma = 0.0
    for i in range(1,k):
        if '0' not in str(i):
            suma += 1.0/float(i)
    return suma
    
for i in range(1,6):
    print reciprocos(0,i)
    
print rec(9999999)