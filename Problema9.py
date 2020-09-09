# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:06:49 2020

@author: Santiago Pérez
"""

def serieDeNumeros(numero):
    if(numero<0):
        return False
    else:
        numero+=1;
        for i in range(numero):
            print(i*str(i))
        return True