import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2,result)

    def test_sub(self):
        result = rpn.calculate("1 1 -")
        self.assertEqual(0,result)

    def test_divide(self):
        result = rpn.calculate("4 2 /")
        self.assertEqual(2,result)
        #comment lul

    def test_exponent(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8,result)
