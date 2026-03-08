import unittest
from coe_number.fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_return_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_give_5_should_return_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_give_15_should_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_give_2_should_return_none(self):
        self.assertIsNone(fizzbuzz(2))

    def test_give_0_should_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")