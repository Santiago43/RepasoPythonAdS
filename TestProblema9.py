# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:15:30 2020

@author: Santiago Pérez
"""

import unittest
from Problema9 import serieDeNumeros
class TestProblema9(unittest.TestCase):

    def test_problema9(self):
        self.assertEqual(True,serieDeNumeros(5))

if __name__ == '__main__':
    unittest.main()