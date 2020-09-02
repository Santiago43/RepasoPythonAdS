# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 08:56:37 2020

@author: Santiago Pérez
"""
continuar=True
while continuar:
    try:
       numero=int(input("Digite un número (entero) para saber si es par o no: "))
       if numero%2==0:
           print("Número par")
       else:
           print("Número impar") 
       continuar=False
    except ValueError:
        print("El valor digitado debe ser un número entero")