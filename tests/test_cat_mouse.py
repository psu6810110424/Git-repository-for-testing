import unittest
from coe_number.cat_mouse import cat_and_mouse

class CatMouseTest(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(2, 5, 3), 'Cat A')

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(1, 5, 4), 'Cat B')

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), 'Mouse C')

    def test_negative_boundary(self):
        self.assertEqual(cat_and_mouse(-1, 1, 0), 'Mouse C')

    def test_max_boundary(self):
        self.assertEqual(cat_and_mouse(0, 100, 99), 'Cat B')