import unittest
from unittest.mock import patch
from coe_number.guess_number import guess_int, guess_float

class GuessNumberTest(unittest.TestCase):

    @patch('coe_number.guess_number.random.randint')
    def test_guess_int_stub(self, mock_randint):
        mock_randint.return_value = 5 
        result = guess_int(1, 10)
        self.assertEqual(result, 5)
        mock_randint.assert_called_once_with(1, 10)

    @patch('coe_number.guess_number.random.randint')
    def test_guess_int_large_range(self, mock_randint):
        mock_randint.return_value = 500
        result = guess_int(1, 1000)
        self.assertEqual(result, 500)
        mock_randint.assert_called_with(1, 1000)

    @patch('coe_number.guess_number.random.uniform')
    def test_guess_float_stub(self, mock_uniform):
        mock_uniform.return_value = 2.5
        result = guess_float(1, 5)
        self.assertEqual(result, 2.5)
        mock_uniform.assert_called_once_with(1, 5)

    @patch('coe_number.guess_number.random.randint')
    def test_guess_int_boundary(self, mock_randint):
        mock_randint.return_value = 100
        result = guess_int(1, 100)
        self.assertEqual(result, 100)

    @patch('coe_number.guess_number.random.randint')
    def test_guess_int_multiple_values(self, mock_randint):
        mock_randint.side_effect = [1, 2, 3]
        
        self.assertEqual(guess_int(1, 10), 1)
        self.assertEqual(guess_int(1, 10), 2)
        self.assertEqual(guess_int(1, 10), 3)