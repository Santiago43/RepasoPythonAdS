# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:39:07 2020

@author: Santiago Pérez
"""

import unittest
from ProblemaNumeroPar import numeroPar
class TestNumeroPar(unittest.TestCase):

    def test_numero_par(self):
        self.assertEqual(True, numeroPar(2))

test = TestNumeroPar()
test.test_numero_par()