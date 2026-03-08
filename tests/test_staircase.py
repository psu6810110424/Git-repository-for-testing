import unittest
from coe_number.staircase import staircase

class StaircaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = '#'
        expected_output = " #\n##"
        
        result = staircase(n, pattern)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_1_with_star_should_be_star(self):
        n, pattern = 1, '*'
        expected = "*"
        self.assertEqual(staircase(n, pattern), expected, f'Should be {expected}')

    def test_give_3_with_A_should_be_stair_A(self):
        n, pattern = 3, 'A'
        expected = "  A\n AA\nAAA"
        self.assertEqual(staircase(n, pattern), expected, f'Should be {expected}')

    def test_give_31_should_be_out_of_range(self):
        self.assertEqual(staircase(31, '#'), "Out of range", f'Should be Out of range')

    def test_give_0_should_be_out_of_range(self):
        self.assertEqual(staircase(0, '#'), "Out of range", f'Should be Out of range')