# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:45:15 2020

@author: Santiago Pérez
"""

import unittest
from Problema2070 import edadFutura
class TestProblema1(unittest.TestCase):

    def test_edad_futura(self):
        self.assertEqual(70,edadFutura(20,2020))

if __name__ == '__main__':
    unittest.main()