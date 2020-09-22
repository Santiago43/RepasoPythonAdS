#!/usr/bin/python
#-*- coding: utf-8 -*-

from FiguraGeométrica import FiguraGeométrica
from Punto import Punto
import math
class Rectángulo(FiguraGeométrica):
    def __init__(self,puntos):
        FiguraGeométrica.__init__(self,puntos,4)
        
    def calcularArea(self):
        d1 = self.puntos[0].calcularDistancia(self.puntos[1])
        d2= self.puntos[0].calcularDistancia(self.puntos[2])
        d3 = self.puntos[0].calcularDistancia(self.puntos[3])
        if d1>d2 and d1>d3:
            return math.fabs(float(d2*d3))
        elif d2>d1 and d2>d3:
            return math.fabs(float(d1*d3))
        else:
            return  math.fabs(float(d1*d2))
    def calcularPerimetro(self):
        d1 = self.puntos[0].calcularDistancia(self.puntos[1])
        d2= self.puntos[0].calcularDistancia(self.puntos[2])
        d3 = self.puntos[0].calcularDistancia(self.puntos[3])
        if d1>d2 and d1>d3:
            return math.fabs(float(2*d2+2*d3))
        elif d2>d1 and d2>d3:
            return math.fabs(float(2*d1+2*d3))
        else:
            return  math.fabs(float(2*d1+2*d2))
