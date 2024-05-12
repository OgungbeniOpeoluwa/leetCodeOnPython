import unittest

from practise import Maximum_product_difference


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [5, 6, 2, 7, 4]
        expected = 34
        self.assertEqual(expected, Maximum_product_difference.maxProductDiffernce(nums))  # add assertion here


if __name__ == '__main__':
    unittest.main()
