import unittest
from coe_number.grid_challenge import grid_challenge

class GridChallengeTest(unittest.TestCase):
    def test_normal_yes(self):
        grid = ["abc", "hjk", "mpq", "rtv"]
        self.assertEqual(grid_challenge(grid), "YES")

    def test_normal_no(self):
        grid = ["ebc", "hjk", "mpq", "rtv"]
        grid = ["ebafd", "trqps", "vtund", "ghsjz", "oiwuz"]
        self.assertEqual(grid_challenge(grid), "NO")

    def test_smallest_grid_1x1(self):
        self.assertEqual(grid_challenge(["a"]), "YES")

    def test_square_grid_5x5_yes(self):
        grid = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "uvwxy"
        ]
        self.assertEqual(grid_challenge(grid), "YES")

    def test_all_same_chars(self):
        grid = ["aaaa", "aaaa", "aaaa"]
        self.assertEqual(grid_challenge(grid), "YES")
