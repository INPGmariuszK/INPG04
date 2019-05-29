#!/usr/bin/python
# -*- coding: utf-8 -*-

import someSimpleFile
import unittest

class FibTest(unittest.TestCase):
    def test_fib0(self):
        self.assertEqual(2, someSimpleFile.fib(2))
        
    def test_fib1(self):
        self.assertEqual(120, someSimpleFile.fib(5))
