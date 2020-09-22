# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:37:53 2020

@author: Santiago Pérez
"""
from Punto import Punto
from Rectángulo import Rectángulo
import unittest

class TestRectángulo(unittest.TestCase):

    def test_area_rectangulo(self):
        punto1= Punto(-1,0)
        punto2= Punto(1,0)
        punto3= Punto(1,1)
        punto4= Punto(-1,1)
        puntos = [punto1,punto2,punto3,punto4]
        rectangulo = Rectángulo(puntos)
        self.assertEqual(2,rectangulo.calcularArea())
    def test_perimetro_rectangulo(self):
        punto1= Punto(-1,0)
        punto2= Punto(1,0)
        punto3= Punto(1,1)
        punto4= Punto(-1,1)
        rectangulo = Rectángulo([punto1,punto2,punto3,punto4])
        self.assertEqual(6,rectangulo.calcularPerimetro())

if __name__ == '__main__':
    unittest.main()