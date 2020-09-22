#!/usr/bin/python
#-*- coding: utf-8 -*-
import abc
class FiguraGeométrica:
    def __init__(self,puntos,lados):
        self.lados = lados
        self.puntos = puntos
    @abc.abstractmethod
    def calcularArea(self):
        pass
    @abc.abstractmethod
    def calcularPerimetro(self):
        pass

