import unittest
from quiz1 import (
    two_sum,
    is_palindrome,
    longest_common_prefix,
    length_of_longest_substring,
)

# можешь добавить свои тесты, эти варианты я взял из примеров и они не покрывают все случаи


class Quiz1Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(-121))
        self.assertFalse(is_palindrome(10))

    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longest_common_prefix([""]), "")

    def test_length_of_longest_substring(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)  # "abc"
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)  # "b"
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)  # "wke"
