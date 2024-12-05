import unittest
from fizzbuzz import FizzBuzz

class Testfizzbuzz(unittest.TestCase):

    def test_input_3_return_fizz(self):
        expected = "fizz"
        actual = FizzBuzz.getFizzBuzz(3)
        self.assertEqual(expected, actual)

    def test_input_5_return_fizz(self):
        expected = "buzz"
        actual = FizzBuzz.getFizzBuzz(5)
        self.assertEqual(expected, actual)

    def test_input_15_return_fizz(self):
        expected = "fizz_buzz"
        actual = FizzBuzz.getFizzBuzz(15)
        self.assertEqual(expected, actual)

    def test_input_7_return_7(self):
        expected = 7
        actual = FizzBuzz.getFizzBuzz(7)
        self.assertEqual(expected, actual)

    def test_input_kelipatan_3_harus_return_fizz(self):
        expected = "fizz"
        actual = FizzBuzz.getFizzBuzz(6)
        self.assertEqual(expected, actual)

        actual = FizzBuzz.getFizzBuzz(9)
        self.assertEqual(expected, actual)

    def test_input_kelipatan_5_harus_return_buzz(self):
        expected = "buzz"
        actual = FizzBuzz.getFizzBuzz(10)
        self.assertEqual(expected, actual)

        actual = FizzBuzz.getFizzBuzz(20)
        self.assertEqual(expected, actual)

    def test_input_kelipatan_3_dan_5_harus_return_fizz_buzz(self):
        expected = "fizz_buzz"
        actual = FizzBuzz.getFizzBuzz(15)
        self.assertEqual(expected, actual)

        actual = FizzBuzz.getFizzBuzz(30)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()