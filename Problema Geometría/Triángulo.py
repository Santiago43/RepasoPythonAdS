#!/usr/bin/python
#-*- coding: utf-8 -*-

from FiguraGeométrica import FiguraGeométrica
from Punto import Punto
import math
class Triángulo(FiguraGeométrica):
    def __init__(self,puntos):
        FiguraGeométrica.__init__(self,puntos,3)

    def calcularArea(self):
        s= self.calcularPerimetro()/2
        d1 = self.puntos[0].calcularDistancia(self.puntos[1])
        d2= self.puntos[0].calcularDistancia(self.puntos[2])
        d3 = self.puntos[1].calcularDistancia(self.puntos[2])
        return math.sqrt(s*(s-d1)*(s-d2)*(s-d3))
    def calcularPerimetro(self):
        d1 = self.puntos[0].calcularDistancia(self.puntos[1])
        d2 = self.puntos[0].calcularDistancia(self.puntos[2])
        d3 = self.puntos[1].calcularDistancia(self.puntos[2])
        return d1+d2+d3
    def tipoTriangulo(self):
        d1 = self.puntos[0].calcularDistancia(self.puntos[1])
        d2 = self.puntos[0].calcularDistancia(self.puntos[2])
        d3 = self.puntos[1].calcularDistancia(self.puntos[2])
        cond1=math.fabs(d1-d2)<1e-9
        cond2=math.fabs(d2-d3)<1e-9
        cond3=math.fabs(d1-d3)<1e-9
        if cond1 and cond2:
            return "Equilátero"
        elif cond1 or cond2 or cond3:
            return "Isósceles"
        else:
            return "Escaleno" 
