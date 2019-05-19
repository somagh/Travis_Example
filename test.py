import unittest
from calculator import *


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(4, -4), 0)

    def test_mult(self):
        self.assertEqual(mult(2, 3), 6)
        self.assertEqual(mult(4, -4), -16)
        self.assertEqual(mult(8, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(4, -4), -1)
        self.assertRaises(Exception, mult(8, 0))


if __name__ == '__main__':
    unittest.main()
