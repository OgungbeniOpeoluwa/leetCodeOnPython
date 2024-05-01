import unittest

from practise import group_anagram


class MyTestCase(unittest.TestCase):
    def test_anagram(self):
        value = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertEqual(result, group_anagram.groupAnagrams(value))  # add assertion here

    def test_empty_string(self):
        value = ["", ""]
        result = [["", ""]]
        self.assertEqual(result, group_anagram.groupAnagrams(value))  # add assertion here

    def test_something_empty_string_and_value(self):
        value = ["b", ""]
        result = [["b"], [""]]
        self.assertEqual(result, group_anagram.groupAnagrams(value))  # add assertion here

    def test_something_new(self):
        value = ["ddddddddddg", "dgggggggggg"]
        result = [["dgggggggggg"], ["ddddddddddg"]]
        self.assertEqual(result, group_anagram.groupAnagrams(value))  # add assertion here


if __name__ == '__main__':
    unittest.main()
