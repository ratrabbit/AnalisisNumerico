# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:55:16 2016

@author: francisco
"""
import numpy as np
import time
def multiplica1(m,n):
    start = time.clock()
    matrizA = m
    matrizB = n
    matrizC = np.zeros((len(matrizA),len(matrizB[:,0])))
    #inciso a)
    for i in range(0,len(matrizA)):
        for j in range(0,len(matrizB[:,0])):
            matrizC[i][j]=np.dot(matrizA[i],matrizB[:,j])
    end = time.clock()
    print "Matriz A\n",matrizA
    print
    print "Matriz B\n",matrizB
    print
    print "Matriz C\n",matrizC
    print "Tiempo de ejecucion en segundos",end-start

def multiplica2(m,n):
    start = time.clock()
    matrizA = m
    matrizB = n
    matrizC = np.zeros((len(matrizA),len(matrizB[:,0])))
    #inciso b)
    for i in range(0,len(matrizA)):
        for j in range(0,len(matrizB[:,0])):
            x = 0
            for l in range(0,len(matrizA[:,0])):
                x+=matrizA[i][l]*matrizB[l][j]
            matrizC[i][j] = x
    end = time.clock()
    print "Matriz A\n",matrizA
    print
    print "Matriz B\n",matrizB
    print
    print "Matriz C\n",matrizC
    print "Tiempo de ejecucion en segundos:",end-start
matrizA = np.array([[ 0.62184398,0.97892254],[ 0.30882306,0.15281587]])
matrizB = np.array([[ 0.52759676,0.1577132 ],[ 0.9522512,0.51829775]])
multiplica1(matrizA,matrizB)
multiplica2(matrizA,matrizB)
matrizA = np.random.random((100,100))
matrizB = np.random.random((100,100))
multiplica1(matrizA,matrizB)
multiplica2(matrizA,matrizB)
"""
Matriz A
[[ 0.62184398  0.97892254]
 [ 0.30882306  0.15281587]]

Matriz B
[[ 0.52759676  0.1577132 ]
 [ 0.9522512   0.51829775]]

Matriz C
[[ 1.26026303  0.60544636]
 [ 0.30845315  0.1279096 ]]
Matriz A
[[ 0.04175764  0.77279487]
 [ 0.95385425  0.97903584]]

Matriz B
[[ 0.86882163  0.03691113]
 [ 0.59911439  0.06803753]]

Matriz C
[[ 0.49927247  0.05412037]
 [ 1.41528367  0.10181902]]
 """
 