from coe_number import example
import unittest
from unittest import mock


class RandomNumberTest(unittest.TestCase):
    def test_random_should_0_20(self):
        result = example.random_integer()

        self.assertIn(result, range(0, 20))


class IsEvenNumberTest(unittest.TestCase):
    @mock.patch("coe_number.example.random_integer", return_value=2)
    def test_random_give_2_should_return_true(self, random_integer_mock):
        result = example.is_even_number()

        self.assertTrue(result)

    @mock.patch("coe_number.example.random_integer", return_value=5)
    def test_random_give_5_should_return_false(self, random_integer_mock):
        result = example.is_even_number()

        self.assertFalse(result)


class IsEvenNumberRangeTest(unittest.TestCase):
    def test_random_should_return_true_or_false(self):
        expected_result = [True, False]

        result = example.is_even_number()

        self.assertIn(result, expected_result)

    @mock.patch("coe_number.example.random_integer", return_value=0)
    def test_random_give_0_should_return_true(self, random_integer_mock):
        result = example.is_even_number()
        self.assertTrue(result)

class MoreRandomNumberTest(unittest.TestCase):
    @mock.patch("coe_number.example.random.randint", return_value=10)
    def test_randint_is_called(self, randint_mock):
        result = example.random_integer()
        self.assertEqual(result, 10)
        randint_mock.assert_called_once_with(0, 20)
