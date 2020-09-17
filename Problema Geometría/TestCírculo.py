# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:16:26 2020

@author: Santiago Pérez
"""

from Circulo import Circulo
from Punto import Punto

import unittest
import math

class TestCírculo(unittest.TestCase):

    def test_area_circulo(self):
        circulo=Circulo(Punto(0,0),3)
        self.assertEqual(9*math.pi,circulo.calcularArea())
    
    def test_perimetro_circulo(self):
        circulo=Circulo(Punto(0,0),3)
        self.assertEqual(6*math.pi,circulo.calcularPerimetro())

if __name__ == '__main__':
    unittest.main()