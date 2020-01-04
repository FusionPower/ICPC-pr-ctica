#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:50:20 2019

@author: samuel
"""

#!/bin/python3
import math


q=int(input())

for i in range(q):
    v,a=list(map(int,input().split()))
    
    matriz=[]
    
    for i in range (v):
		#ponemos -infinito para decir que no hay
		#arista porque es con peso. Si no hubiera
		#peso es mejor poner bool.
        matriz.append([-math.inf]*v)
    
    for arista in range(a):
        v1,v2,peso=list(map(int,input().split()))
        matriz[v1-1][v2-1]=peso
        matriz[v2-1][v1-1]=peso
    
    empiezo=int(input())
    
    visitados=[False]*v
    
    visitados[empiezo-1]=True

    costo=[-math.inf]*v
    costo[empiezo-1]=0
    
    cola=[empiezo-1]
    
    while len(cola)!=0:
        fila=cola.pop(0)
        for index,valor in enumerate(matriz[fila]):
            if visitados[index]==False and valor!=-math.inf:
				if costo[index]==-math.inf:
					costo[index]=0
                costo[index]+=valor
                cola.append(index)
                visitados[index]=True
    
    for i in costo:        
        if i>0:
            print(i,end=" ")
        if i==-math.inf:
            print(end=" Imposible")


