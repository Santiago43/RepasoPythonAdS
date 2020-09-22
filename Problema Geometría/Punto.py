#!/usr/bin/python
#-*- coding: utf-8 -*-
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calcularDistancia(self, otroPunto):
        return ((self.x-otroPunto.x)**2+(self.y-otroPunto.y)**2)**(1/2)

    def determinarDentro(self, circulo):
        return self.calcularDistancia(circulo.puntos[0])<=circulo.radio