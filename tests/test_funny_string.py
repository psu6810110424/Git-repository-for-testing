import unittest
from coe_number.funny_string import funny_string

class FunnyStringTest(unittest.TestCase):
    def test_funny_lmnop(self):
        self.assertEqual(funny_string("lmnop"), "Funny")

    def test_not_funny_bcxz(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")

    def test_single_char(self):
        self.assertEqual(funny_string("a"), "Funny")

    def test_all_same_chars(self):
        self.assertEqual(funny_string("aaaaa"), "Funny")

    def test_mixed_case_long_string(self):
        self.assertEqual(funny_string("abccba"), "Funny")
