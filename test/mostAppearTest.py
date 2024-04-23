import unittest

from practise import mostAppear


class MyTestCase(unittest.TestCase):
    def test_something(self):
        inputs = [2, 1, 1, 2, 2]
        expected = 2
        self.assertEqual(expected, mostAppear.returnMostAppear(inputs)) # add assertion here

    def test_another(self):
        inputs = [3, 4, 5, 5, 5]
        expected = 5
        self.assertEqual(expected, mostAppear.returnMostAppear(inputs))


if __name__ == '__main__':
    unittest.main()
