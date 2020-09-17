#!/usr/bin/python
#-*- coding: utf-8 -*-

from FiguraGeométrica import FiguraGeométrica

class Circulo(FiguraGeométrica):
    def __init__(self,punto,radio):
        self.radio = radio
        self.puntos.append(punto)

