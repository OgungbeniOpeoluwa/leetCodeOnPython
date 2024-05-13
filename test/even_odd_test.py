import unittest

from practise import even_odd


class MyTestCase(unittest.TestCase):
    def test_something(self):
        inputs = [4, 5, 8, 8, 8, 2, 9]
        output = [False, True, False, False, False, False, True]
        self.assertEqual(output, even_odd.return_even_and_odd_in_zero_and_one(inputs))  # add assertion here


if __name__ == '__main__':
    unittest.main()
