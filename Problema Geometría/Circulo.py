#!/usr/bin/python
#-*- coding: utf-8 -*-

from FiguraGeométrica import FiguraGeométrica
import math
class Circulo(FiguraGeométrica):
    def __init__(self,punto,radio):
        self.radio = radio
        FiguraGeométrica.__init__(self,punto,0)
        
    def calcularArea(self):
        return math.pi*float(self.radio)**2
    
    def calcularPerimetro(self):
        return 2*math.pi*float(self.radio)
