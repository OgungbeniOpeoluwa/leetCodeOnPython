import unittest

from practise import divisible_non_divisible_diffrence


class MyTestCase(unittest.TestCase):
    def test_something(self):
        number = 10
        divisible_number = 3
        result = 19
        self.assertEqual(19, divisible_non_divisible_diffrence.return_diffrences(number,divisible_number))

    def test_another_input(self):
        number = 5
        divisible_number = 6
        result = 15
        self.assertEqual(result, divisible_non_divisible_diffrence.return_diffrences(number, divisible_number))

    def test_another_input_2(self):
        number = 5
        divisible_number = 1
        result = -15
        self.assertEqual(result, divisible_non_divisible_diffrence.return_diffrences(number, divisible_number))


if __name__ == '__main__':
    unittest.main()
