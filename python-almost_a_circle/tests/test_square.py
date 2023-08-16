#!/usr/bin/python3

import unittest
from models square import Square


class TestSquare(unittest.TestCase):
    def test_intialization_success(self):
        s1=Sqauew(5)
        s2=Square(10)
        self assertEqual(s1.id,5)
        self assertEqual(s2.id,6)

    def test_intialization_without_arguments(self):

        self assertRaises(TypeError,Square)

if __name__ =='__main__':
    unittest.main()
