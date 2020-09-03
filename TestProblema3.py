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
        
if __name__ == '__main__':
    unittest.main()