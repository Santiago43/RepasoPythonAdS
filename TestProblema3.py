# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:27:12 2020

@author: Santiago Pérez
"""

import unittest
from Problema3 import primeroYUltimo

class TestProblema3(unittest.TestCase):

    def test_primeroYUltimo(self):
        self.assertEqual('Bo', primeroYUltimo('Banano'))
        
test = TestProblema3()
test.test_primeroYUltimo();