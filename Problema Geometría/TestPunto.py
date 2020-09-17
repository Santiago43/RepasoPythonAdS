# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:55:43 2020

@author: Santiago Pérez
"""
from Punto import Punto
import unittest

class TestPunto(unittest.TestCase):

    def test_distancia(self):
        punto1= Punto(0,0)
        punto2= Punto(3,4)
        self.assertEqual(5,punto1.calcularDistancia(punto2))

if __name__ == '__main__':
    unittest.main()