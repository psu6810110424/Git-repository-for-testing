import unittest
from coe_number.number_utils import is_prime_list

class PrimeListTest(unittest.TestCase):
    def test_give_2_3_5_is_prime(self):
        prime_list = [2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_4_6_is_not_prime(self):
        self.assertFalse(is_prime_list([2, 4, 6]))

    def test_give_1_is_not_prime(self):
        self.assertFalse(is_prime_list([1]))

    def test_give_large_prime(self):
        self.assertTrue(is_prime_list([17, 19, 23]))

    def test_give_empty_list(self):
        self.assertFalse(is_prime_list([]))