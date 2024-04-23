import unittest

from practise import seprated_by_space


class MyTestCase(unittest.TestCase):
    def test_string_with_three_length(self):
        input1 = 'abcd'
        input2 = 'defg'
        actual = seprated_by_space.return_seprated_string(input1, input2)
        expected = "decd abfg"
        self.assertEqual(expected, actual)
