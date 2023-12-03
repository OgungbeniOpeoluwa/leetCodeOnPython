import unittest

from practise import check_if_two_equvilent


class MyTestCase(unittest.TestCase):
    def test_something(self):
        inputs = ["a", "bc"]
        inputs_two = ["ab", "c"]
        self.assertTrue(check_if_two_equvilent.string_equvilent_function(inputs, inputs_two))

    def test_for_another_inputs(self):
        inputs = ["a", "cb"]
        inputs_two = ["a", "bc"]
        self.assertFalse(check_if_two_equvilent.string_equvilent_function(inputs,inputs_two))

    def test_for_another_inputs_with_one_length_size_the_other_is_two(self):
        inputs = ["abc", "d", "defg"]
        inputs_two = ["abcddefg"]
        self.assertTrue(check_if_two_equvilent.string_equvilent_function(inputs, inputs_two))


if __name__ == '__main__':
    unittest.main()
