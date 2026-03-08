import unittest
from coe_number.two_characters import two_characters

class TwoCharactersTest(unittest.TestCase):
    def test_normal_beabeefeab(self):
        self.assertEqual(two_characters("beabeefeab"), 5)

    def test_single_char_impossible(self):
        self.assertEqual(two_characters("a"), 0)

    def test_no_valid_pair(self):
        self.assertEqual(two_characters("aaaa"), 0)

    def test_already_valid_abab(self):
        self.assertEqual(two_characters("abab"), 4)

    def test_high_diversity_random(self):
        self.assertEqual(two_characters("asdcbsdcagfsdgad"), 5)
