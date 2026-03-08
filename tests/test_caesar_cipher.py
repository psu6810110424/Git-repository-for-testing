import unittest
from coe_number.caesar_cipher import caesar_cipher

class CaesarCipherTest(unittest.TestCase):
    def test_normal_shift(self):
        self.assertEqual(caesar_cipher("middle-Outz", 2), "okffng-Qwvb")

    def test_large_shift(self):
        self.assertEqual(caesar_cipher("abc", 87), "jkl")

    def test_no_shift(self):
        self.assertEqual(caesar_cipher("Hello-World!", 0), "Hello-World!")

    def test_symbols_and_numbers(self):
        self.assertEqual(caesar_cipher("123!@#", 10), "123!@#")

    def test_wrap_around(self):
        self.assertEqual(caesar_cipher("xyzXYZ", 3), "abcABC")
