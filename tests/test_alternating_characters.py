import unittest
from coe_number.alternating_characters import alternating_characters

class AlternatingCharactersTest(unittest.TestCase):
    def test_no_deletion_abab(self):
        self.assertEqual(alternating_characters("ABABABAB"), 0)

    def test_full_deletion_aaaaa(self):
        self.assertEqual(alternating_characters("AAAAA"), 4)

    def test_partial_deletion_aaabbb(self):
        self.assertEqual(alternating_characters("AAABBB"), 4)

    def test_short_strings(self):
        self.assertEqual(alternating_characters("A"), 0)
        self.assertEqual(alternating_characters("AB"), 0)
        self.assertEqual(alternating_characters("AA"), 1)

    def test_long_string_performance(self):
        s = "A" * 5000 + "B" * 5000
        self.assertEqual(alternating_characters(s), 9998)
