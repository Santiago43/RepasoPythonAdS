# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:27:12 2020

@author: Santiago Pérez
"""

import unittest
from Problema3 import primeraLetra
from Problema3 import últimaLetra
class TestProblema3(unittest.TestCase):
    palabra = 'Pera'
    def test_primeraLetra(self):
        self.assertEqual('P', primeraLetra(self.palabra))
    def test_ultimaLetra(self):
        self.assertEqual('a',últimaLetra(self.palabra))
if __name__ == '__main__':
    unittest.main()