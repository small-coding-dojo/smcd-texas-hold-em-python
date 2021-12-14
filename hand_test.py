import unittest
from hand import *

class Tests_Hand_worksAsExpected(unittest.TestCase):
    def test_hand_nothing_returns_type_nothing_and_correct_sequence(self):
        actual = hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])
        expected = ('nothing', ['A', 'K', 'Q', 'J', '9'])
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
