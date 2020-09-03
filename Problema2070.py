# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:16:25 2020

@author: Santiago Pérez
"""
def edadFutura(edad,año):
    return (2070-añoActual)+edad
continuar = True
while (continuar):
    try:
        edad=int(input("Digite su edad: "))
        if (edad<0):
            raise Exception("Su edad no puede ser negativa")
        añoActual=int(input("Digite el año actual: "))
        if (añoActual<0):
            raise Exception("El año no puede ser negativo")
        elif (añoActual>2070):
            raise Exception("La idea es que digite un año inferior al 2070")
        edadFutura=edadFutura(edad,añoActual)
        print("Su edad futura es de: "+str(edadFutura)+" años")
        continuar=False
    except Exception as e:
        print(e)

