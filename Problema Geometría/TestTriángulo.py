# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:15:31 2020

@author: Santiago Pérez
"""
from Triángulo import Triángulo
from Punto import Punto
import unittest
import math
class TestRectángulo(unittest.TestCase):
    def test_area_triangulo(self):
        punto1= Punto(-1,0)
        punto2= Punto(1,0)
        punto3= Punto(1,1)
        puntos = [punto1,punto2,punto3]
        triángulo = Triángulo(puntos)
        self.assertEqual(1,triángulo.calcularArea())
    def test_perimetro_triangulo(self):
        punto1= Punto(-1,0)
        punto2= Punto(1,0)
        punto3= Punto(1,1)
        triángulo = Triángulo([punto1,punto2,punto3])
        self.assertEqual(3+math.sqrt(5),triángulo.calcularPerimetro())
    def test_tipo_triangulo_equilatero(self):
        punto1=Punto(0,0)
        punto2=Punto(0.5,math.sqrt(3)/2)
        punto3=Punto(1,0)
        triángulo=Triángulo([punto1,punto2,punto3])
        self.assertEqual("Equilátero",triángulo.tipoTriangulo())
    def test_tipo_triangulo_isósceles(self):
        punto1=Punto(-1,0)
        punto2=Punto(1,-1)
        punto3=Punto(1,1)
        triángulo=Triángulo([punto1,punto2,punto3])
        self.assertEqual("Isósceles",triángulo.tipoTriangulo())
    def test_tipo_triangulo_escaleno(self):
        punto1=Punto(-1,0)
        punto2=Punto(1,0)
        punto3=Punto(1,-1)
        triángulo=Triángulo([punto1,punto2,punto3])
        self.assertEqual("Escaleno",triángulo.tipoTriangulo())
if __name__ == '__main__':
    unittest.main()