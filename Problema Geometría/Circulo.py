#!/usr/bin/python
#-*- coding: utf-8 -*-

from FiguraGeométrica import FiguraGeométrica
import math
class Circulo(FiguraGeométrica):
    def __init__(self,punto,radio):
        self.radio = radio
        self.puntos.append(punto)
        
    def calcularArea(self):
        return math.pi*self.radio**2
    
    def calcularPerimetro(self):
        return 2*math.pi*self.radio
