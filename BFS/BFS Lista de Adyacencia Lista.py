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
    
    lista_de_adyacencia=[]
    
    for i in range (v):
        lista_de_adyacencia.append([]*v)
    
    for arista in range(a):
        v1,v2,peso=list(map(int,input().split()))
        lista_de_adyacencia[v1-1].append(v2-1)
		lista_de_adyacencia[v1-1].append(peso)

		
        lista_de_adyacencia[v2-1].append(v1-1)
		lista_de_adyacencia[v2-1].append(peso)
    
    empiezo=int(input())
    
    visitados=[False]*v
    
    visitados[empiezo-1]=True

    costo=[-math.inf]*v
    costo[empiezo-1]=0
    
    cola=[empiezo-1]
    
    while len(cola)!=0:
        fila=cola.pop(0)
		nodos=lista_de_adyacencia[fila]
        for index,nodo in enumerate(nodos[0:len(nodos):2]):
			peso=index*2+1
            if visitados[nodo]==False:
				if costo[nodo]==-math.inf:
					costo[nodo]=0
                costo[nodo]+=peso
                cola.append(nodo)
                visitados[nodo]=True
    
    for i in costo:        
        if i>0:
            print(i,end=" ")
        if i==-math.inf:
            print(end=" Imposible")


