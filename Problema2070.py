# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:16:25 2020

@author: Santiago Pérez
"""

edad=int(input("Digite su edad: "))
if (edad<0):
    #exit("La edad no puede ser negativa")
    print("Edad no puede ser negativa\n")
añoActual=int(input("Digite el año actual: "))
if (añoActual<0):
    print("Año no puede ser negativo\n")
    #exit("El año no puede ser negativo")
edadFutura=int((2070-añoActual)+edad)
print("Su edad futura es de: ")
print(edadFutura)