import unittest

from practise import buy_two_chocolate


class MyTestCase(unittest.TestCase):
    def test_something(self):
        prices = [1, 2, 2]
        money = 3
        expected = 0
        self.assertEqual(expected, buy_two_chocolate.buy_choco(prices,money))  # add assertion here


if __name__ == '__main__':
    unittest.main()
