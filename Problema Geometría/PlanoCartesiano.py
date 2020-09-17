#!/usr/bin/python
#-*- coding: utf-8 -*-

class PlanoCartesiano:
    def __init__(self):
        self.figuras = []
        self.puntos = []

    def definir(self, punto):
        self.puntos.append(punto)

    def definir(self, figura):
        self.figuras.append(figura)

