import unittest

from practise import MaximizeHappiness


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [12, 1, 42]
        k = 3
        expected = 4
        self.assertEqual(expected, MaximizeHappiness.maximumHappinessSum(array, k))  # add assertion here


if __name__ == '__main__':
    unittest.main()
