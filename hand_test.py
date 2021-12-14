import unittest
from hand import *


class TestsHandWorksAsExpected(unittest.TestCase):
    def test_hand_nothing_returns_type_nothing_and_correct_sequence(self):
        actual = hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])
        expected = ('nothing', ['A', 'K', 'Q', 'J', '9'])
        self.assertEqual(actual, expected)


    def test_a_different_nothing_resulting_in_a_different_nothing(self):
        actual = hand(["10♠", "5♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"])
        expected = ('nothing', ['Q', 'J', '10', '9', '5'])
        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main()
