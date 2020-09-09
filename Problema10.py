# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:46:56 2020

@author: Santiago Pérez
"""
from random import randint
def juegoNumeroAleatorio(respuesta):
    continuar=True
    print("Hola, bienvenido al juego adivina el numero. Debes adivinar un número entre 1 y 1000\nEl programa dará pistas para encontrarlo")
    while continuar:
        valor = int(input("Digite un número: "))
        if (valor<1 or valor>1000):
            print("Debe digitar números entre 1 y 1000")
        elif (valor>respuesta):
            print("El número es menor a "+str(valor))
        elif(valor<respuesta):
            print("El número es mayor a "+str(valor))
        else:
            continuar=False
    print("Has adivinado el número. El resultado es: "+str(respuesta))
    
def juego():
    juegoNumeroAleatorio(randint(1,1000))